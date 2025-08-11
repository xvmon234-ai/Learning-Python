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
df_merged['customer_id'] = df_merged['customer_id'].fillna('Unknown')
df_merged['quantity'] = df_merged['quantity'].apply(lambda x: 1 if x < 1 else x)
df_merged['purchase_date'] = pd.to_datetime(df_merged['purchase_date'])
df_merged['sales_amount'] = df_merged['quantity'] * df_merged['price']


# --------------------------------------------------------------------------------
# 문제 3: 데이터 저장
# --------------------------------------------------------------------------------

# 내가 최초 제출한 코딩
def categorize_age(customer_id):
    if customer_id == 'Unknown':
        return 'Unknown'
    
    id_num = int(customer_id)
    if 1 <= id_num <= 5:
        return 'Teens'
    elif 6 <= id_num <= 10:
        return '20s'
    elif 11 <= id_num <= 15:
        return '30s'
    elif 16 <= id_num <= 20:
        return '40s'
    else:
        return 'Unknown'

df_merged['age_group'] = df_merged['customer_id'].astype(str).apply(categorize_age)
customer_age_summary = df_merged.groupby('age_group')['sales_amount'].mean().reset_index()
customer_age_summary.rename(columns={'sales_amount': 'average_purchase_amount'}, inplace=True)
customer_age_summary.to_csv('customer_age_summary.csv', index=False)

print("\n--- Saved 'customer_age_summary.csv' with the following data ---")
print(customer_age_summary)


# --------------------------------------------------------------------------------
# 피드백 및 모범 답안
# --------------------------------------------------------------------------------

# - 고객 연령대 그룹화: 'customer_id'를 문자열로 변환한 후, 'apply'를 사용해 조건에 따라 연령대를 그룹화하는 방식이 논리적입니다.
# - 'ValueError' 해결: 'customer_id'가 'Unknown'일 때를 먼저 처리하여 에러를 방지한 로직이 아주 훌륭합니다.
# - 결과 저장: 'groupby'를 통해 평균을 계산하고 'to_csv()'로 파일을 저장하는 과정이 정확합니다.

# [추가 학습]
# - 'pd.cut' 함수를 사용하면 연속적인 값을 범주로 나누는 작업을 더 간결하고 효율적으로 수행할 수 있습니다. 특히 연령대나 소득 구간처럼 특정 범위로 데이터를 나눌 때 유용합니다.
#   - 예: 'bins = [0, 5, 10, 15, 20, np.inf]', 'labels = ['Teens', '20s', '30s', '40s', 'Unknown']'
#   - df_merged['age_group'] = pd.cut(df_merged['customer_id'], bins=bins, labels=labels, right=False)
