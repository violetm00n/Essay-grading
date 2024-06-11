from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Text vectorization with TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['essay'])
y = data['grade']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest model
model_rf = RandomForestRegressor(random_state=42)
model_rf.fit(X_train, y_train)

# Evaluate the model
predictions = model_rf.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)
def predict_grade1(essay):
    essay_vector = vectorizer.transform([essay])
    grade = model.predict(essay_vector)[0]
    print("Predicted Grade:", grade)
