import pandas as pd
import numpy as np
import xgboost as xgb
import joblib
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import os

def create_synthetic_training_data():
    n = 200
    df = pd.DataFrame({
        "kat": np.random.randint(1, 20, size=n),
        "yapi_turu": np.random.choice(["betonarme", "çelik", "yığma", "ahşap"], size=n),
        "zemin_sinifi": np.random.choice(["Z1", "Z2", "Z3", "Z4"], size=n),
        "bina_yasi": np.random.randint(1, 80, size=n),
        "deprem_bolgesi": np.random.randint(1, 6, size=n),
    })
    df["risk"] = ((df["kat"] > 6) & (df["bina_yasi"] > 30)).astype(int)
    return df

def train_and_save_model():
    df = create_synthetic_training_data()
    X = df.drop("risk", axis=1)
    y = df["risk"]

    numeric_features = ["kat", "bina_yasi", "deprem_bolgesi"]
    categorical_features = ["yapi_turu", "zemin_sinifi"]

    numeric_transformer = Pipeline(steps=[
        ("scaler", StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", xgb.XGBClassifier(
            use_label_encoder=False,
            eval_metric="logloss",
            random_state=42
        ))
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    pipeline.fit(X_train, y_train)

    os.makedirs("model", exist_ok=True)
    joblib.dump(pipeline, "model/xgb_model.pkl")
    print("✅ Model başarıyla eğitildi ve 'model/xgb_model.pkl' olarak kaydedildi.")

if __name__ == "__main__":
    train_and_save_model()
