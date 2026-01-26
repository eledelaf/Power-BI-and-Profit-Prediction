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

# Key questions to answer
# Total revenue (revenue = units sold x Price per unit)
df['Revenue'] = df['Units Sold'] * df['Sale Price']
total_revenue = df['Revenue'].sum()
print("The total revenue is :", total_revenue)

# Total Units Sold
print("The total units sold are:", int(df['Units Sold'].sum()))

# Average Order Value
