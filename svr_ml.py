from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MaxAbsScaler
from sklearn.pipeline import make_pipeline

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model using a pipeline that scales data appropriately for sparse matrices
model_svr = SVR(C=1.0, epsilon=0.1, kernel='rbf')
model_svr.fit(X_train, y_train)

# Evaluate the model
predictions = model_svr.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)
def predict_grade2(essay):
    essay_vector = vectorizer.transform([essay])
    grade = model.predict(essay_vector)[0]
    print("Predicted Grade:", grade)
