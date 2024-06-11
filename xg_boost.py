from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Assuming X and y are already defined and preprocessed

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model_xgb = XGBRegressor(objective ='reg:squarederror', seed=42)
model_xgb.fit(X_train, y_train)

# Evaluate the model
predictions = model_xgb.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)
def predict_grade0(essay):
    essay_vector = vectorizer.transform([essay])
    grade = model.predict(essay_vector)[0]
    print("Predicted Grade:", grade)
