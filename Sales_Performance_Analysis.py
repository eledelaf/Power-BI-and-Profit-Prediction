from Data_cleaning import clean_data
import pandas as pd

# 2. Core Sales Performance Analysis

df = clean_data(pd.read_excel("Sample_data.xlsx"))

# ['Segment', 'Country', 'Product', 'Discount Band', 'Units Sold', 'Manufacturing Price', 'Sale Price', 'Gross Sales', 'Discounts', ' Sales', 'COGS', 'Profit', 'Date']
def kpi_summary(df):
    sales = df['Sales'].sum()
    units_sold = df['Units Sold'].sum()
    profit = df['Profit'].sum()

    return {
        "Total Sales": float(sales),
        "Total Units Sold": float(units_sold),
        "Total Profit": float(profit), 
        "Gross Profit": float(sales - profit),
        "Average Profit per Unit": float(profit / units_sold) if units_sold else 0,
        "Profit Margin": float(profit / sales * 100) if sales else 0

    }

print(kpi_summary(df))
