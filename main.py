# Import libraries
import numpy as np
import pandas as pd
import matplotlib
import seaborn as sns

# Load data
data = "Sample_data.xlsx"
df = pd.read_excel(data)

print(df.head())
print(df.columns)

# 1. Data Cleaning
print(df.describe())
print(df.info()) # Only Null values are 53 discount Band
print(df[df["Discount Band"].isna()].head()) 
# 2. Core Sales Performance Analysis
# Total revenue (revenue = units sold x Price per unit)
df['Revenue'] = df['Units Sold'] * df['Sale Price']
total_revenue = df['Revenue'].sum()
print("The total revenue is :", total_revenue)

# Total Units Sold
print("The total units sold are:", int(df['Units Sold'].sum()))

# Average Order Value
