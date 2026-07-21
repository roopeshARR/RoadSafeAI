import pandas as pd

df = pd.read_csv("data/processed/combined_dataset.csv")

print("Unique Severity Values:\n")
print(df["severity"].unique())

print("\nValue Counts:\n")
print(df["severity"].value_counts(dropna=False))