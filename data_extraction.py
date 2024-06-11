import pandas as pd
# Load the dataset
data = pd.read_csv('essay.csv')
from sklearn.feature_extraction.text import CountVectorizer

# Tokenization
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['essay'])

# Target labels
y = data['grade']
!pip install xgboost
