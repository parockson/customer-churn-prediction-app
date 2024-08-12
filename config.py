
import os

ONE_DAY_SEC = 24*60*60

ONE_WEEK_SEC = ONE_DAY_SEC*7

XGBClassifier_URL = "https://drive.google.com/file/d/1S7OOihqHqjYNsYvLPj1wQZgyxvkImPPL/view?usp=sharing"

RandomForest_URL = "https://drive.google.com/file/d/1H_r_xgKjr8ScRq1IsyoxLWPXtjBZeIK-/view?usp=sharing"

LGBM_URL = "https://drive.google.com/file/d/1kLkfXyUH9kGY8u4WkX2vMJny22zrKzME/view?usp=sharing"

ENCODER_URL = "https://github.com/MoIdris/Sepsis-Prediction-ML-API/blob/dev/dev/models/encoder.joblib"


BASE_DIR = './'  # Where Unicorn server runs from

ENV_PATH = os.path.join(BASE_DIR, '.src/api/.env')
