import pandas as pd
import json
import os

# Always get the folder where this script exists
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(BASE_DIR, "crop_recommendation.csv")


print("Looking for dataset at:", csv_path)

# Load dataset
df = pd.read_csv(csv_path)

# Columns used for ideal values
features = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

ideal_values = {}

# Calculate mean values per crop
for crop in df["label"].unique():
    crop_df = df[df["label"] == crop]
    ideal_values[crop] = {
        feature: round(crop_df[feature].mean(), 2)
        for feature in features
    }

# Save JSON
json_path = os.path.join(BASE_DIR, "crop_ideal_values.json")

with open(json_path, "w") as f:
    json.dump(ideal_values, f, indent=4)

print("✅ crop_ideal_values.json created successfully")
