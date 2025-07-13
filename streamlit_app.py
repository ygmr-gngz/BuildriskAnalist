import openai
import os
from dotenv import load_dotenv
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import streamlit as st
import pandas as pd
from dotenv import load_dotenv

load_dotenv()  
from models.xgboost_model import XGBRiskModel
from LLM.llm_report import GPTExplainer  
from core.ISensorStream import SyntheticSensorStream




# Model ve LLM yükle
model = XGBRiskModel("model/xgb_model.pkl")
model.load_model()
llm = GPTExplainer(api_key=os.getenv("OPENAI_API_KEY"))

# Streamlit Başlık
st.title("🏗️ buildRiskLLM: Deprem Sonrası Yapı Risk Analizi")
st.markdown("Yapı bilgilerini girin, sistem size risk skorunu ve GPT-4o ile detaylı analizini versin.")

# Form verileri
with st.form("risk_form"):
    kat = st.slider("Kat Sayısı", 1, 20, 5)
    bina_yasi = st.slider("Bina Yaşı", 1, 100, 30)
    yapi_turu = st.selectbox("Yapı Türü", ["betonarme", "çelik", "yığma", "ahşap"])
    zemin_sinifi = st.selectbox("Zemin Sınıfı", ["Z1", "Z2", "Z3", "Z4"])
    deprem_bolgesi = st.selectbox("Deprem Bölgesi", [1, 2, 3, 4, 5])
    submit = st.form_submit_button("Analizi Başlat")

# Tahmin işlemi
if submit:
    input_data = {
        "kat": kat,
        "bina_yasi": bina_yasi,
        "yapi_turu": yapi_turu,
        "zemin_sinifi": zemin_sinifi,
        "deprem_bolgesi": deprem_bolgesi
    }

    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    risk_label = "⚠️ Yüksek Risk" if prediction == 1 else "✅ Güvenli"

    st.subheader("📊 Risk Sonucu:")
    st.success(f"Tahmin: {risk_label}")

    with st.spinner("GPT-4o açıklaması hazırlanıyor..."):
        explanation = llm.generate_explanation(input_data, risk_label)
        st.subheader("🧠 GPT-4o Teknik Değerlendirme:")
        st.write(explanation)

    # Opsiyonel: Sensör verisini göster
    if st.checkbox("📈 Sentetik Sensör Verisini Göster"):
        stream = SyntheticSensorStream()
        df_sensor = stream.generate()
        st.line_chart(df_sensor.set_index("timestamp"))