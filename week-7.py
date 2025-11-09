import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create the dataset (C++ has missing value NaN)
data = {
    "Programming Language": ["Java", "Python", "PHP", "JavaScript", "C#", "C++"],
    "Popularity": [22.2, 17.6, 8.8, 8.0, 7.7, np.nan]
}

# Create DataFrame
df = pd.DataFrame(data)

# a. Pandas: Find missing data and output in Boolean
print("Missing Data in Popularity Column:")
print(df["Popularity"].isnull())

# b. NumPy: Add missing value 6.7 for C++ and update JavaScript to 8.3
df.loc[df["Programming Language"] == "C++", "Popularity"] = 6.7
df.loc[df["Programming Language"] == "JavaScript", "Popularity"] = 8.3

print("\nUpdated DataFrame:")
print(df)

# c. Matplotlib: Display bar chart
plt.figure(figsize=(8, 5))
plt.bar(df["Programming Language"], df["Popularity"], color="skyblue", edgecolor="black")
plt.title("Programming Language Popularity")
plt.xlabel("Programming Languages")
plt.ylabel("Popularity (%)")
plt.show()
