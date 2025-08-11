import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt
import seaborn as sns

# --- 데이터 준비 (문제 1의 최종 df_merged를 가정) ---
cust_data = {
    'order_id': range(101, 201),
    'customer_id': np.random.choice(range(1, 21), 100),
    'product_id': np.random.choice(range(1001, 1016), 100),
    'purchase_date': pd.to_datetime(pd.date_range(start='2024-01-01', periods=100, freq='D')),
    'quantity': np.random.randint(1, 10, 100),
}
cust_df = pd.DataFrame(cust_data)
cust_df.loc[[10, 20], 'customer_id'] = np.nan
cust_df.loc[[30, 40], 'quantity'] = -1
prod_data = {
    'product_id': range(1001, 1016),
    'product_name': [f'Product_{i}' for i in range(1, 16)],
    'category': ['Electronics', 'Apparel', 'Food', 'Electronics', 'Apparel', 'Food', 'Electronics', 'Apparel', 'Food', 'Electronics', 'Apparel', 'Food', 'Electronics', 'Apparel', 'Food'],
    'price': np.random.randint(10000, 50001, 15)
}
prod_df = pd.DataFrame(prod_data)
df_merged = pd.merge(cust_df, prod_df, on='product_id', how='left')
df_merged['quantity'] = df_merged['quantity'].apply(lambda x: 1 if x < 1 else x)
df_merged['purchase_date'] = pd.to_datetime(df_merged['purchase_date'])


# --------------------------------------------------------------------------------
# 문제 2: 분석 및 시각화
# --------------------------------------------------------------------------------

# 내가 최초 제출한 코딩
top5_categories = df_merged.groupby('category')['quantity'].sum().nlargest(5)
plt.figure(figsize=(10, 6))
sns.barplot(x=top5_categories.index, y=top5_categories.values, palette='viridis')
plt.title('Top 5 Best-Selling Product Categories')
plt.xlabel('Product Category')
plt.ylabel('Total Quantity Sold')
plt.show()

df_merged['sales_amount'] = df_merged['quantity'] * df_merged['price']
df_merged['purchase_month'] = df_merged['purchase_date'].dt.to_period('M')
monthly_sales = df_merged.groupby('purchase_month')['sales_amount'].sum()
plt.figure(figsize=(12, 7))
monthly_sales.plot(kind='line', marker='o', color='royalblue')
plt.title('Monthly Total Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales Amount')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()


# --------------------------------------------------------------------------------
# 피드백 및 모범 답안
# --------------------------------------------------------------------------------

# - Top 5 카테고리 분석: 'groupby', 'sum', 'nlargest(5)'를 사용하여 가장 많이 팔린 카테고리를 효율적으로 찾았습니다. 이는 여러 메서드를 체인으로 연결하는 Pandas의 강력한 기능을 잘 활용한 예시입니다.
# - 월별 매출 추이 분석: 'dt.to_period('M')'을 사용해 날짜를 월 단위로 그룹화한 점이 매우 좋습니다. 시계열 데이터 분석 시 날짜를 문자열로 변환하는 것보다 훨씬 간결하고 정확한 방법입니다.
# - 시각화: Matplotlib와 Seaborn을 목적에 맞게(`barplot`과 `lineplot`) 사용하고, 제목, 레이블, 그리드 등을 추가하여 차트의 가독성을 높였습니다.

# [추가 학습]
# - 시각화에서 'df.groupby(...).plot()'을 사용하면 코드를 더 간결하게 만들 수 있습니다.
# - 'sns.lineplot'의 'x'와 'y' 인자에 직접 열 이름을 전달하는 방식도 좋습니다.
