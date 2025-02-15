# import pickle
# model = pickle.load(open('model.pkl', 'rb'))
# print(model.feature_names_in_)  # This will show what features the model was trained with

import pandas as pd

# Load dataset
df = pd.read_csv("heart.csv")

# Drop target column
features = df.drop(columns=["target"]).columns

# Print feature names
print("Feature Names Used for Training:", list(features))
