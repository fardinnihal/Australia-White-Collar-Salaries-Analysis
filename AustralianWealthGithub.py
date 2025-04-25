import pandas as pd
import numpy as np

# 1. Load Data
data = {
    "Job": ["Accountant", "Actuary", "Health Professional", "Acupuncturist", 
            "Civil Engineer", "Nurse", "Software Developer", "Teacher", 
            "Electrical Engineer", "Doctor", "Dentist", "Pilot", "Business Analyst"],
    "Min_Salary": [70, 125, 115, 123, 95, 75, 105, 85, 80, 150, 180, 105, 105],
    "Max_Salary": [90, 145, 130, 123, 115, 95, 125, 95, 120, 300, 200, 125, 160]
}

df = pd.DataFrame(data)
df["Avg_Salary"] = (df["Min_Salary"] + df["Max_Salary"]) / 2  # Average salary
df["Salary_Range"] = df["Max_Salary"] - df["Min_Salary"]       # Range (spread)

# 2. Basic Exploration
print("=== Top 3 Highest-Paying Jobs ===")
print(df.nlargest(3, "Avg_Salary")[["Job", "Avg_Salary"]])
print("\n=== Bottom 3 Lowest-Paying Jobs ===")
print(df.nsmallest(3, "Avg_Salary")[["Job", "Avg_Salary"]])

# 3. Salary Ranges
print("\n=== Jobs with Widest Salary Ranges ===")
print(df[["Job", "Salary_Range"]].sort_values("Salary_Range", ascending=False))

# 4. Statistical Summary
print("\n=== Statistical Summary ===")
print(df.describe())

# 5. Filtering: High-Paying Jobs (>120K)
print("\n=== High-Paying Jobs (Avg > $120K) ===")
print(df[df["Avg_Salary"] > 120][["Job", "Avg_Salary"]])

# 6. Compare Engineers
print("\n=== Engineers ===")
print(df[df["Job"].str.contains("Engineer")])

# 7. Advanced: Normalized Salaries (0-1 scale)
df["Normalized_Salary"] = (df["Avg_Salary"] - df["Avg_Salary"].min()) / (df["Avg_Salary"].max() - df["Avg_Salary"].min())
print("\n=== Normalized Salaries (0=Lowest, 1=Highest) ===")
print(df[["Job", "Normalized_Salary"]])

# 8. Percentile Rankings
df["Percentile"] = df["Avg_Salary"].rank(pct=True) * 100
print("\n=== Salary Percentiles ===")
print(df[["Job", "Percentile"]].sort_values("Percentile", ascending=False))
print("==Data analysis==")
print("\nDoctors earn the most and accountants earn the least.")
print("\nIn business analytics field, several factors like experience, location,education background play an important role.")
print("\nCivil Engineers earn slightly more than electrical engineers.")