# Import libraries
import numpy as np
import pandas as pd
import matplotlib
import seaborn as sns

# Load data
data = "Sample_data.xlsx"    
df = pd.read_excel(data)

def clean_data(df, verbose = False):
    if verbose:
        print(df.head())
        print(df.columns)

    df = df.rename(columns={" Sales": "Sales"})

    # 1. Data Cleaning
    # This is just an example of data cleaning, this data set is supposed to be already clean. 
    # Getting the info about the DF
    if verbose:
        print(df.describe())
        print(df.info()) 

    # There are missing values in Discount Band, since this columns depends of others we are going to try to learn the value.
    # We are going to see in the values of Discount Band how were they created.
    df["discount_pct"] = df["Discounts"] / df["Gross Sales"]
    if verbose:
        print(df[["Gross Sales", "Discounts", "discount_pct"]].describe())
        print(df.groupby("Discount Band")["discount_pct"].describe())

    # We are going to look into the Discount Band = NaN 
    if verbose: 
        print(df[df["Discount Band"].isna()][["Gross Sales", "Discounts", "discount_pct"]].head())

    # Lets create a function that gives a value to Discount Band 
    def assign_disc_band(value):
        if value == 0:
            return 'None'
        elif value <= 0.04:
            return 'Low'
        elif value <= 0.09:
            return 'Medium'
        else:
            return 'High'
        
    # We overwrite the column applying the funciton to the discount percentage    
    df["Discount Band"] = df["Discount Band"].fillna(df["discount_pct"].apply(assign_disc_band))

    # We can see that the problem was that in the Excel the value None was transalted into NaN
    if verbose:
        print(df.groupby("Discount Band")["discount_pct"].describe())

    # Now we eliminate "discount_pct"
    df = df.drop("discount_pct", axis=1)


    # Since we have the column Date, in order to save some space we can eliminate the columns: 'Month Number', 'Month Name' and 'Year'
    df = df.drop(['Month Number', 'Month Name', 'Year'], axis=1)

    # Lets check for data consistency 
    # Sales consistency, should be Gross Sales - Discounts = Net Sales
    if verbose:
        print("Sales consistency check:")
        print((df["Sales"] - (df["Gross Sales"] - df["Discounts"])).abs().describe())
        # We can see that most of the values are 0, which means that the data is consistent. They are not exactly 0 due to rounding errors.

    # Lets check for Profit consistency, should be Profit = Sales - COGS (Cost of Goods Sold)
    if verbose:
        print("Profit consistency check:")
        print((df["Profit"] - (df["Sales"] - df["COGS"])).abs().describe())
        # We can see that most of the values are 0, which means that the data is consistent. They are not exactly 0 due to rounding errors.

    # Check for impossible values, like negative sales or profit
    if verbose:
        print("Negative Sales check:")
        print((df[["Units Sold", "Gross Sales", "Sales", "COGS"]] < 0).sum())
    # Text Consistency
    # Removing leading and trailing whitespace
    df["Country"] = df["Country"].str.strip()
    df["Segment"] = df["Segment"].str.strip()
    df["Product"] = df["Product"].str.strip()
    df["Discount Band"] = df["Discount Band"].str.strip()

    if verbose:
        print(df["Product"].value_counts().head())
        print(df["Product"].nunique())
        print(df["Country"].value_counts().head())
        print(df["Country"].nunique())

    # Redundant columns check 
    # Ive already eliminated the redundant columns: 'Month Number', 'Month Name', and 'Year'

    # Check for duplicates rows
    if verbose:
        print("Number of duplicate rows:")
        print(df.duplicated().sum())

    # Lets check for candinality
    if verbose:
        print("Cardinality of each column:")
        print(df.nunique().sort_values(ascending=False))
    # The nunique() method returns the number of unique values for each column
    return df

if __name__ == "__main__":
    df = clean_data(df, True)