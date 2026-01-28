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
# Getting the info about the DF
print(df.describe())
print(df.info()) 

# There are missing values in Discount Band, since this columns depends of others we are going to try to learn the value.
# We are going to see in the values of Discount Band how were they created.
df["discount_pct"] = df["Discounts"] / df["Gross Sales"]



