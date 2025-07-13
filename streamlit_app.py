import openai
import os
import sys
import streamlit as st
import pandas as pd
import joblib
from dotenv import load_dotenv

# Yol ayarları ve .env yükleme
load_dotenv()
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Modül importları
from LLM.llm_report import GPTExplainer
from core.ISensorStream import SyntheticSensorStream

# Model ve LLM yükleniyor
model = joblib.load("model/xgb_model.pkl")
llm = GPTExplainer(api_key=os.getenv("OPENAI_API_KEY"))

def main():
    st.title("🏗️ BuildRiskLLM: Deprem Sonrası Yapı Risk Değerlendirme")

    st.write("Yapı bilgilerini girin, sistem size risk skorunu ve GPT-4o destekli açıklamayı versin.")

    # Giriş alanları
    kat = st.slider("Kat Sayısı", 1, 30, 5)
    yapi_turu = st.selectbox("Yapı Türü", ["betonarme", "çelik", "yığma", "ahşap"])
    zemin_sinifi = st.selectbox("Zemin Sınıfı", ["Z1", "Z2", "Z3", "Z4"])
    bina_yasi = st.slider("Bina Yaşı", 1, 100, 30)
    deprem_bolgesi = st.selectbox("Deprem Bölgesi", [1, 2, 3, 4, 5])

    # DataFrame formatında input oluştur
    input_data = pd.DataFrame({
        "kat": [kat],
        "yapi_turu": [yapi_turu],
        "zemin_sinifi": [zemin_sinifi],
        "bina_yasi": [bina_yasi],
        "deprem_bolgesi": [deprem_bolgesi]
    })

    if st.button("Analizi Başlat"):
        prediction = model.predict(input_data)[0]
        risk_label = "⚠️ Yüksek Risk" if prediction == 1 else "✅ Güvenli"

        st.subheader("📊 Risk Sonucu:")
        st.success(f"Tahmin: {risk_label}")

        with st.spinner("🧠 GPT-4o açıklaması hazırlanıyor..."):
            explanation = llm.generate_explanation(input_data, risk_label)
            st.subheader("🧠 GPT-4o Teknik Değerlendirme:")
            st.write(explanation)

            # Opsiyonel: Sensör verisi
            if st.checkbox("📈 Sentetik Sensör Verisini Göster"):
                stream = SyntheticSensorStream()
                df_sensor = stream.generate()
                st.line_chart(df_sensor.set_index("timestamp"))


if __name__ == "__main__":
    main()
