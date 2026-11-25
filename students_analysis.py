import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "Marks": [85, 92, 76, 88]
}

df = pd.DataFrame(data)

print(df)

print("Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

import matplotlib.pyplot as plt

plt.bar(df["Name"], df["Marks"])

plt.title("Student Marks Analysis")
plt.xlabel("Student Name")
plt.ylabel("Marks")

plt.show()

total = df["Marks"].sum()
print("Total Marks:", total)
topper = df.loc[df["Marks"].idxmax()]

print("Highest Scorer:", topper["Name"])
print("Marks:", topper["Marks"])
lowest = df.loc[df["Marks"].idxmin()]

print("Lowest Scorer:", lowest["Name"])
print("Marks:", lowest["Marks"])

df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)
print(df)
import matplotlib.pyplot as plt

plt.bar(df["Name"], df["Marks"])

plt.title("Student Performance Analysis")
plt.xlabel("Student Name")
plt.ylabel("Marks")

plt.axhline(y=40, linestyle="--", label="Pass Mark")
plt.legend()

plt.show()
# Find Topper
topper = df.loc[df["Marks"].idxmax()]
print("Topper:", topper["Name"])

# Find Lowest Scorer
lowest = df.loc[df["Marks"].idxmin()]
print("Lowest Scorer:", lowest["Name"])

# Pass or Fail
df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

print("\nFinal Student Result:")
print(df)
import matplotlib.pyplot as plt

# Create Bar Chart
plt.figure(figsize=(8, 5))

plt.bar(df["Name"], df["Marks"])

plt.title("Student Performance Analysis")
plt.xlabel("Student Name")
plt.ylabel("Marks")

plt.axhline(y=40, linestyle="--", label="Pass Marks")

plt.legend()
plt.grid(axis="y")
plt.show()