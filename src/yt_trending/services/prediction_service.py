import joblib
from pathlib import Path

MODEL_DIR = Path("models")

_loaded_models = {}

FEATURE_ORDER = [
    "likes",
    "comment_count",
    "category_id",
    "comments_disabled",
    "ratings_disabled",
]

def load_model(region: str):
    if region in _loaded_models:
        return _loaded_models[region]

    model_path = MODEL_DIR / f"trending_model_{region}.joblib"

    if not model_path.exists():
        raise RuntimeError(f"Model not found for region: {region}")

    model = joblib.load(model_path)
    _loaded_models[region] = model
    return model


def predict_popularity(
    region: str,
    likes: int,
    comments: int,
    category_id: int,
    comments_disabled: bool,
    ratings_disabled: bool,
) -> float:
    model = load_model(region)

    features = [[
        likes,
        comments,
        category_id,
        int(comments_disabled),
        int(ratings_disabled),
    ]]

    prob = model.predict_proba(features)[0][1]
    return round(float(prob), 4)


def get_feature_importance(region: str):
    model = load_model(region)

    importances = model.feature_importances_

    return dict(zip(FEATURE_ORDER, importances.round(4)))
