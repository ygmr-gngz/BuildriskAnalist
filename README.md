# BuildRiskLLM

**AI-Powered Post-Earthquake Structural Risk Assessment with Stellar Blockchain Integration**

> Developed for the **HackStellar Hackathon** — Open Innovation Track

---

## Overview

BuildRiskLLM is an end-to-end intelligent system for assessing the structural safety of buildings following seismic events. It combines machine learning-based risk prediction, large language model (LLM) analysis, synthetic sensor data simulation, and immutable on-chain record-keeping via the Stellar Testnet — creating a transparent, auditable, and intelligent pipeline for disaster response and structural safety verification.

---

## Key Features

### 1. ML-Based Structural Risk Prediction

A trained **XGBoost** classifier evaluates building safety using the following input parameters:

| Parameter | Description |
|---|---|
| Number of floors | Vertical structural load factor |
| Building type | Construction material and design class |
| Soil class | Ground response category |
| Building age | Construction era and code compliance |
| Seismic zone | Regional hazard level |

**Output:**
- Binary classification: `Safe` or `High Risk`
- Numerical risk score: `0 – 100`

---

### 2. LLM-Powered Architectural Analysis (GPT-4o)

For every prediction, the system generates a technical engineering-level report covering:

- Identified structural weaknesses
- Site and soil response characteristics
- Probable failure modes and deformation patterns
- Safety recommendations and intervention priorities

---

### 3. Synthetic Sensor Data Stream

Simulated time-series sensor data is generated and visualized in real time, including:

- Acceleration measurements
- Stress and strain readings
- Structural oscillation patterns

This enables realistic testing and demonstration without requiring physical IoT infrastructure.

---

### 4. Stellar Testnet Integration (Blockchain Auditability)

Risk assessment results are committed to the **Stellar Testnet** with a single click, providing an immutable, tamper-resistant public record.

**On-chain data stored:**

```
Memo:        projectId:riskScore
ManageData:  "risk-{projectId}" → riskScore
```

**Returns:**
- Transaction hash
- Direct link to Stellar Expert Explorer for independent verification

This mechanism ensures **auditability**, **immutability**, and **transparency** — critical properties for insurance verification, government compliance, and disaster response coordination.

---

## Technology Stack

| Layer | Technologies |
|---|---|
| Frontend / UI | Streamlit |
| Machine Learning | XGBoost, Scikit-Learn, Pandas |
| LLM Analysis | GPT-4o via OpenAI API |
| Blockchain | Stellar Testnet, Stellar Python SDK |
| Configuration | Python 3.10+, python-dotenv |

---

## Project Structure

```
BuildRiskAnalist/
│
├── streamlit_app.py          # Main application — UI, ML inference, LLM, Stellar
├── model/
│   └── xgb_model.pkl         # Trained XGBoost model
├── LLM/
│   └── llm_report.py         # GPT-4o wrapper for structured report generation
├── core/
│   └── sensor_generator.py   # Synthetic sensor data generation
├── src/blockchain/
│   ├── stellar_client.py     # Stellar network connection handler
│   └── risk_writer.py        # Writes risk scores to Stellar Testnet
├── requirements.txt
└── .env.example
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ygmr-gngz/BuildRiskAnalist.git
cd BuildRiskAnalist
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows (Git Bash)
source venv/Scripts/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
STELLAR_SECRET_KEY=your_stellar_secret_key
```

> Fund your Stellar Testnet account before running:
> [Stellar Laboratory — Account Creator (Testnet)](https://laboratory.stellar.org/#account-creator?network=testnet)

### 5. Run the Application

```bash
streamlit run streamlit_app.py
```

---

## On-Chain Verification

After generating a risk prediction, click **"Save risk result to Stellar Testnet"**.

The application will return:

- A **transaction hash** confirming the write operation
- A **Stellar Expert Explorer link** for independent, public verification

```
https://stellar.expert/explorer/testnet/tx/<your_tx_hash>
```

Any party — insurers, engineers, municipal authorities — can verify the record without relying on the application itself.

---

## Hackathon Evaluation Criteria

| Criterion | How BuildRiskLLM Addresses It |
|---|---|
| **Originality** | Novel combination of XGBoost, GPT-4o analysis, synthetic sensors, and Stellar blockchain for a real-world safety use case |
| **Deployment** | Fully operational Stellar Testnet integration with live transaction output |
| **Scope** | Implements Memo + ManageData operations using the Stellar SDK within a clean, modular architecture |
| **Technical Quality** | Well-organized codebase, separation of concerns, documented modules, stable MVP |
| **User Experience** | Intuitive Streamlit UI, real-time charts, one-click blockchain commit |
| **Readiness** | End-to-end functional pipeline; extensible to physical sensor inputs |
| **Impact Potential** | Applicable to disaster response, post-earthquake building inspection, insurance verification, and regulatory compliance |

---

## Potential Impact

BuildRiskLLM addresses a critical gap in disaster response infrastructure: the need for fast, transparent, and verifiable structural safety assessments at scale. By anchoring AI predictions to an immutable blockchain record, the system enables:

- **Emergency responders** to prioritize evacuation and inspection resources
- **Insurance companies** to access tamper-proof risk data
- **Municipal governments** to maintain auditable building safety registries
- **Engineers** to receive structured AI-assisted analysis for rapid field decisions

---

## License

This project is released under the [MIT License](LICENSE).

---

*BuildRiskLLM — Where artificial intelligence meets structural integrity, secured by blockchain.*

