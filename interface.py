import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split


with open("xgboost_model.pkl", "wb") as f:
    pickle.dump(model_xgb, f)


with open("random_forest_model.pkl", "wb") as f:
    pickle.dump(model_rf, f)


with open("svr_model.pkl", "wb") as f:
    pickle.dump(model_svr, f)

# Save the TF-IDF vectorizer
pickle.dump(vectorizer, open("vectorizer_filename.pkl", "wb"))

print("Models and vectorizer saved successfully.")
