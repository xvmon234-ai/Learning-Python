import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#요구사항1. 데이터 불러오기 및 전처리
df_sales = pd.read_csv("monthly_sales_data.csv")
df_sales["Sale_Date"] = pd.to_datetime(df_sales["Sale_Date"], errors='coerce')
df_sales["Sale_Month"] = df_sales["Sale_Date"].dt.to_period("M")
df_sales["Total_Revenue"] = df_sales["Quantity_Sold"] * df_sales["Unit_Price"]

#요구사항2. 월별 총 매출액 추이 분석 및 시각화
monthly_revenue = df_sales.groupby("Sale_Month")["Total_Revenue"].sum().sort_index()
plt.figure(figsize=(10, 6))
plt.plot(monthly_revenue.index.astype(str), monthly_revenue.values, marker='o', linestyle='-', color='blue')

plt.title("Monthly Total Revenue Trend", fontsize=14)
plt.xlabel("Sales Month")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

#요구사항3. 제품 카테고리별 매출 기여도 분석 및 시각화
category_revenue = df_sales.groupby("Product_Category")["Total_Revenue"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 8))
plt.pie(category_revenue, labels=category_revenue.index, 
        autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)

plt.title("Sales Contribution by Product Category", fontsize=14)
plt.axis('equal')  
plt.tight_layout()
plt.show()

#요구사항4. 지역별 상위 3개 제품 카테고리 분석
grouped = df_sales.groupby(['Region', 'Product_Category'])['Total_Revenue'].sum().reset_index()
grouped_sorted = grouped.sort_values(['Region', 'Total_Revenue'], ascending=[True, False])
top3_per_region = grouped_sorted.groupby('Region').head(3)

print(top3_per_region)
