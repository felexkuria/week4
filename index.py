import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("orders_export-1746132369388.csv",parse_dates=["Updated At"])
# dataPd= pd.DataFrame(data)
# print(data)
# print(data.columns)
# print(data['Name'])
# plt.plot(data['Paid Price'])
# plt.xlabel('Seller Sku')
# plt.ylabel('Paid Price')
# plt.show()
# Calculate total revenue and best selling product
total_revenue = data['Paid Price'].sum().round(2)
best_selling_product = data.groupby('Item Name').size().idxmax()
best_selling_units = data.groupby('Item Name').size().max()

# Step 4: Day with Highest Sales (based on Revenue) 
day_highest_sales = data.groupby('Updated At')['Paid Price'].sum().idxmax()
highest_sales_day = day_highest_sales.strftime('%Y-%m-%d')
# Step 5: Save Summary
summary = {
    'Total Revenue': total_revenue,
    'Day with Highest Sales': highest_sales_day,
    'Best Selling Product': f"{best_selling_product} ({best_selling_units} units sold)",
}
with open("sales_summary.txt", "w") as file:
    file.write(str(summary))

# Step 6: Print Insights
print(summary)
# 🎯 Bonus: Visualize Sales Trends
daily_revenue = data.groupby('Updated At')['Paid Price'].sum()

plt.figure(figsize=(10, 6))
plt.plot(daily_revenue.index, daily_revenue.values, marker="o", linestyle="-", color="blue")
plt.title("Daily Revenue Trend")
plt.xlabel("Date")
plt.ylabel("Revenue (Kes)")
plt.grid(True)
plt.tight_layout()
plt.savefig("sales_trend.png")
plt.show()

print("Total Revenue: Kes ", total_revenue)
print(int(data['Shipping Fee'].sum().round(2)))
