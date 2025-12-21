import pandas as pd
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

DATA_DIR = Path("data/raw")
MODEL_DIR = Path("models")

REGIONS = {
    "IN": "INvideos.csv",
    "US": "USvideos.csv",
}

FEATURES = [
    "likes",
    "comment_count",
    "category_id",
    "comments_disabled",
    "ratings_disabled",
]

def train_region(region: str, filename: str):
    print(f"\nTraining model for region: {region}")
    df = pd.read_csv(DATA_DIR / filename)

    df = df[["views"] + FEATURES].dropna()
    df["comments_disabled"] = df["comments_disabled"].astype(int)
    df["ratings_disabled"] = df["ratings_disabled"].astype(int)

    threshold = df["views"].quantile(0.75)
    df["popular"] = (df["views"] > threshold).astype(int)

    X = df[FEATURES]
    y = df["popular"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=12,
        random_state=42,
        n_jobs=-1,
    )

    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    print(classification_report(y_test, preds))

    MODEL_DIR.mkdir(exist_ok=True)
    joblib.dump(model, MODEL_DIR / f"trending_model_{region}.joblib")


def main():
    for region, file in REGIONS.items():
        if (DATA_DIR / file).exists():
            train_region(region, file)
        else:
            print(f"Skipping {region}, file not found")


if __name__ == "__main__":
    main()
