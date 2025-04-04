import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    df = pd.read_csv("sales_data.csv")  # Random dataset name
    print("First 5 rows of the dataset:")
    print(df.head())
    print("\nDataset Info:")
    print(df.info())
    
    # Check for missing values
    print("\nMissing values:")
    print(df.isnull().sum())
    
    # Fill missing values (modify as needed)
    df.fillna(method='ffill', inplace=True)
except FileNotFoundError:
    print("Error: The file was not found.")
    exit()

# Task 2: Basic Data Analysis
print("\nBasic Statistics:")
print(df.describe())

# Grouping and aggregating data
print("\nAverage Sales per Region:")
print(df.groupby("Region")["Sales"].mean())

# Task 3: Data Visualization
sns.set_style("darkgrid")

# Line Chart - Sales Over Time
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Sales'], marker='o', linestyle='-', color='b')
plt.xlabel("Date")
plt.ylabel("Sales")
plt.title("Sales Trend Over Time")
plt.xticks(rotation=45)
plt.show()

# Bar Chart - Average Sales per Region
plt.figure(figsize=(8, 5))
sns.barplot(x=df["Region"], y=df["Sales"], estimator=sum, palette="coolwarm")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.title("Total Sales by Region")
plt.show()

# Histogram - Distribution of Sales
plt.figure(figsize=(8, 5))
sns.histplot(df["Sales"], bins=20, kde=True, color='g')
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.title("Sales Distribution")
plt.show()

# Scatter Plot - Sales vs. Profit
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["Sales"], y=df["Profit"], color='r')
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.title("Sales vs Profit")
plt.show()

print("\nAnalysis complete! 🎉")