"""
Analyze Dataset B (2022-2025)
"""

from services.data_service import load_analytics_dataset

df = load_analytics_dataset()

print("=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

print("\nFirst Five Rows")
print(df.head())

print("\nDescriptive Statistics")
print(df.describe(include="all"))