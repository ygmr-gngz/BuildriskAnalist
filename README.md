# 🏗️ BuildRiskLLM  
**AI-Powered Earthquake Structural Risk Assessment + Stellar Blockchain Integration**

BuildRiskLLM is an AI-driven system that evaluates the post-earthquake structural safety of buildings.  
It combines **machine learning**, **LLM-based explanations**, **synthetic sensor data**, and a **Stellar Testnet integration** that records risk results on-chain.

This project was developed for **HackStellar Hackathon** (Open Innovation Track).

---

## 🚀 Features

### 🔹 1. ML-Based Structural Risk Prediction
Uses an XGBoost model trained on structural parameters:
- Number of floors  
- Building type  
- Soil class  
- Building age  
- Seismic zone  

Output:
- Binary classification (Safe / High Risk)  
- Numerical risk score (0–100)

---

### 🔹 2. GPT-4o Architecture Analysis  
The system generates a **technical engineering-level explanation** using GPT-4o:
- Structural weaknesses  
- Ground response  
- Failure modes  
- Expected deformation  
- Safety recommendations  

---

### 🔹 3. Synthetic Sensor Stream  
A simulated sensor dataset visualized as a time series:
- Acceleration  
- Stress/strain  
- Structural oscillation patterns  

---

### 🔹 4. Stellar Testnet Integration (Blockchain)  
Risk scores can be **saved to Stellar Testnet** with a single button.

Stored on-chain:
- Memo: `projectId:riskScore`  
- ManageData: `"risk-projectId" = riskScore`

Returns:
- Transaction hash  
- Direct link to Stellar Expert Explorer  

This provides **auditability**, **immutability**, and **tamper-proof transparency**.

---

## 🛠️ Tech Stack

| Layer | Technologies |
|-------|--------------|
| **UI** | Streamlit |
| **AI/ML** | XGBoost, Pandas, Scikit-Learn |
| **LLM** | GPT-4o (OpenAI API) |
| **Blockchain** | Stellar Testnet, Stellar SDK |
| **DevOps** | Python 3.10+, dotenv |

---

## 📁 Project Structure

buildriskanalist/
│
├── streamlit_app.py # Main app (UI + ML + LLM + Stellar)
├── model/xgb_model.pkl # Trained ML model
├── LLM/llm_report.py # GPT model wrapper
├── core/ # Synthetic sensor generator
├── src/blockchain/
│ ├── stellar_client.py # Stellar connection test
│ └── risk_writer.py # Writes risk results to Stellar
└── requirements.txt


---

## ⚙️ Installation

```bash
git clone https://github.com/ygmr-gngz/BuildRiskAnalist.git
cd BuildRiskAnalist

python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)

pip install -r requirements.txt

🔐 Environment Variables

Create a .env file:

OPENAI_API_KEY=your_openai_key
STELLAR_SECRET_KEY=your_stellar_secret


Fund your Stellar Testnet account:
https://laboratory.stellar.org/#account-creator?network=testnet
▶️ Run the App
streamlit run streamlit_app.py

🌐 On-Chain Demo

After risk prediction, click:

💾 Save risk result to Stellar Testnet


The app provides:

Transaction hash

Explorer link

Verifiable on-chain record of the building’s risk score

Example:
https://stellar.expert/explorer/testnet/tx/
<your_tx_hash>

🧠 How This Meets Hackathon Criteria
✔️ Orijinallik

Combines ML, LLM explanation, synthetic sensors + Stellar blockchain auditability.

✔️ Deployment

Fully operational Stellar Testnet integration.

✔️ Kapsam

Uses Memo + ManageData operations, Stellar SDK, and clean modular structure.

✔️ Teknik Kalite

Well-organized architecture, documented Python code, stable MVP.

✔️ Kullanıcı Deneyimi

Clear UI, real-time charts, one-click blockchain save.

✔️ Hazır Olma Durumu

End-to-end working pipeline; extendable to real sensor inputs.

✔️ Potansiyel Etki

Useful for disaster response, building safety assessments, insurance verification.

🏁 Conclusion

BuildRiskLLM demonstrates how AI + Blockchain can support public safety after earthquakes.
It brings transparency, auditability, and intelligence to structural risk analysis.

✨ Thanks for reviewing our project!

