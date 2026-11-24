# Data Cleaning and Exploratory Data Analysis using Pandas
from io import StringIO

import pandas as pd

data = {
    "Name": ["Anitha", "Bala", "Chitra", "Dinesh", "Ezhil", "Fathima"],
    "Department": ["CSE", "CSE", "ECE", "CSE", "ECE", "CSE"],
    "Attendance": [92, 85, None, 88, 95, 90],
    "Mark": [86, 91, 78, None, 95, 82],
}
df = pd.DataFrame(data)

print("--- Original Dataset ---")
print(df)
print("\nMissing Values:")
print(df.isnull().sum())

df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["Mark"] = df["Mark"].fillna(df["Mark"].mean())
df = df.drop_duplicates()

print("\n--- Cleaned Dataset ---")
print(df)
print("\n--- Descriptive Statistics ---")
print(df.describe())
print("\n--- Department-wise Average Marks ---")
print(df.groupby("Department")["Mark"].mean().round(2))
print("\n--- EDA Summary ---")
print("Highest Mark :", df["Mark"].max())
print("Lowest Mark :", df["Mark"].min())
print("Average Mark :", round(df["Mark"].mean(), 2))
print("Average Attendance :", round(df["Attendance"].mean(), 2))

csv_data = """Name,Department,Attendance,Mark
Asha,CSE,90,88
Bala,CSE,80,76
Charan,ECE,,92
Divya,ECE,95,
Eshan,CSE,85,84
"""
csv_df = pd.read_csv(StringIO(csv_data))
print("\n--- Original CSV Dataset ---")
print(csv_df)
print("\nMissing Values:")
print(csv_df.isnull().sum())

csv_df["Attendance"] = csv_df["Attendance"].fillna(
    csv_df["Attendance"].mean()
)
csv_df["Mark"] = csv_df["Mark"].fillna(csv_df["Mark"].mean())
csv_df = csv_df.drop_duplicates()

print("\n--- Cleaned CSV Dataset ---")
print(csv_df)
print("\n--- Descriptive Statistics ---")
print(csv_df.describe())
print("\n--- Department-wise Average Marks ---")
print(csv_df.groupby("Department")["Mark"].mean().round(2))
print("\n--- CSV EDA Summary ---")
print("Highest Mark :", csv_df["Mark"].max())
print("Lowest Mark :", csv_df["Mark"].min())
print("Average Mark :", round(csv_df["Mark"].mean(), 2))
print("Average Attendance :", round(csv_df["Attendance"].mean(), 2))
