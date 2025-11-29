import os
import sys

import joblib
import openai
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

# Ortam değişkenlerini yükle
load_dotenv()

# Proje kök dizinini PYTHONPATH'e ekle
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = CURRENT_DIR  # streamlit_app.py proje kökünde
sys.path.append(PROJECT_ROOT)

# Modül importları
from LLM.llm_report import GPTExplainer
from core.ISensorStream import SyntheticSensorStream
from src.blockchain.risk_writer import write_risk_to_stellar


# Model ve LLM yükleme
model = joblib.load("model/xgb_model.pkl")
llm = GPTExplainer(api_key=os.getenv("OPENAI_API_KEY"))


def main():
    st.set_page_config(page_title="BuildRiskLLM", page_icon="🏗️")
    st.title("🏗️ BuildRiskLLM: Deprem Sonrası Yapı Risk Değerlendirme")

    st.write(
        "Yapı bilgilerini girin, sistem size **risk skorunu**, sınıflandırma sonucunu "
        "ve GPT-4o destekli teknik açıklamayı versin. İsterseniz sonucu **Stellar testnet** "
        "üzerine de kaydedebilirsiniz."
    )

    st.markdown("---")

    # Proje kimliği (Stellar için kullanılacak)
    project_id = st.text_input(
        "📌 Proje ID / Proje Adı",
        help="Bu değer Stellar testnet üzerinde risk verisi için kimlik olarak kullanılacak. Örn: istanbul-bina-01",
        placeholder="örneğin: istanbul-bina-01",
    )

    st.markdown("### 🏢 Yapı Bilgilerini Girin")

    # Giriş alanları
    col1, col2 = st.columns(2)
    with col1:
        kat = st.slider("Kat Sayısı", 1, 30, 5)
        bina_yasi = st.slider("Bina Yaşı", 1, 100, 30)
        deprem_bolgesi = st.selectbox("Deprem Bölgesi", [1, 2, 3, 4, 5])
    with col2:
        yapi_turu = st.selectbox("Yapı Türü", ["betonarme", "çelik", "yığma", "ahşap"])
        zemin_sinifi = st.selectbox("Zemin Sınıfı", ["Z1", "Z2", "Z3", "Z4"])

    # DataFrame formatında input oluştur
    input_data = pd.DataFrame(
        {
            "kat": [kat],
            "yapi_turu": [yapi_turu],
            "zemin_sinifi": [zemin_sinifi],
            "bina_yasi": [bina_yasi],
            "deprem_bolgesi": [deprem_bolgesi],
        }
    )

    # Sonuçları tutmak için placeholder'lar
    analysis_placeholder = st.empty()
    stellar_placeholder = st.empty()
    sensor_placeholder = st.empty()

    if st.button("🚀 Analizi Başlat"):
        with st.spinner("Model tahmini yapılıyor..."):
            prediction = model.predict(input_data)[0]

            # Eğer modelin predict_proba'sı varsa, daha anlamlı risk skoru üret
            risk_score = None
            if hasattr(model, "predict_proba"):
                proba = model.predict_proba(input_data)[0][1]  # 1 = riskli sınıf
                risk_score = int(proba * 100)
            else:
                # Sınıflandırma sonucuna göre basit bir risk skoru
                risk_score = 80 if prediction == 1 else 20

            risk_label = "⚠️ Yüksek Risk" if prediction == 1 else "✅ Görece Güvenli"

        with analysis_placeholder.container():
            st.subheader("📊 Model Risk Sonucu")
            st.write(f"**Sınıflandırma:** {risk_label}")
            st.write(f"**Sayısal Risk Skoru (0-100):** `{risk_score}`")

            with st.spinner("🧠 GPT-4o açıklaması hazırlanıyor..."):
                explanation = llm.generate_explanation(input_data, risk_label)

            st.subheader("🧠 GPT-4o Teknik Değerlendirme")
            st.write(explanation)

        st.markdown("---")

        # Stellar entegrasyonu
        with stellar_placeholder.container():
            st.subheader("🔗 Sonucu Stellar Testnet Üzerine Kaydet")

            if not project_id:
                st.info(
                    "Stellar testnet'e yazmadan önce yukarıdaki **Proje ID / Proje Adı** alanını doldurmanız önerilir. "
                    "Boş bırakırsanız varsayılan olarak `project-unnamed` kullanılacaktır."
                )

            if st.button("💾 Sonucu Stellar Testnet'e Kaydet"):
                final_project_id = project_id.strip() or "project-unnamed"

                with st.spinner("Stellar testnet'e işlem gönderiliyor..."):
                    try:
                        tx_hash = write_risk_to_stellar(final_project_id, risk_score)
                        explorer_url = (
                            f"https://stellar.expert/explorer/testnet/tx/{tx_hash}"
                        )

                        st.success("Başarılı! Risk sonucu Stellar testnet'e kaydedildi ✅")
                        st.code(tx_hash, language="text")
                        st.markdown(
                            f"[🔍 Stellar Expert üzerinde görüntüle]({explorer_url})"
                        )

                    except Exception as e:
                        st.error(f"Stellar'a yazarken bir hata oluştu: {e}")
                        st.info(
                            "Lütfen `STELLAR_SECRET_KEY` ortam değişkeninin doğru tanımlandığından "
                            "ve hesabınızın testnet üzerinde fonlanmış olduğundan emin olun."
                        )

        st.markdown("---")

        # Opsiyonel: Sentetik sensör verisi
        with sensor_placeholder.container():
            if st.checkbox("📈 Sentetik Sensör Verisini Göster"):
                stream = SyntheticSensorStream()
                df_sensor = stream.generate()
                st.subheader("📈 Sentetik Sensör Zaman Serisi")
                st.line_chart(df_sensor.set_index("timestamp"))


if __name__ == "__main__":
    main()

