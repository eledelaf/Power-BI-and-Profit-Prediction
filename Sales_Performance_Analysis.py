from Data_cleaning import df

# 2. Core Sales Performance Analysis
# Total revenue (revenue = units sold x Price per unit)
df['Revenue'] = df['Units Sold'] * df['Sale Price']
total_revenue = df['Revenue'].sum()
print("The total revenue is :", total_revenue)

# Total Units Sold
print("The total units sold are:", int(df['Units Sold'].sum()))

# Average Order Value: dividing total revenue by the number of orders over a specific period 

