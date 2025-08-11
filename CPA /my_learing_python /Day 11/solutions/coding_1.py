import pandas as pd
import numpy as np
import io
import matplotlib.pyplot as plt
import seaborn as sns

# --- 데이터 준비 ---
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

cust_csv = cust_df.to_csv(index=False)
cust_io = io.StringIO(cust_csv)

prod_data = {
    'product_id': range(1001, 1016),
    'product_name': [f'Product_{i}' for i in range(1, 16)],
    'category': ['Electronics', 'Apparel', 'Food', 'Electronics', 'Apparel', 'Food', 'Electronics', 'Apparel', 'Food', 'Electronics', 'Apparel', 'Food', 'Electronics', 'Apparel', 'Food'],
    'price': np.random.randint(10000, 50001, 15)
}
prod_df = pd.DataFrame(prod_data)
prod_excel_io = io.BytesIO()
prod_df.to_excel(prod_excel_io, index=False)
prod_excel_io.seek(0)

df_purchases = pd.read_csv(cust_io)
df_products = pd.read_excel(prod_excel_io)


# --------------------------------------------------------------------------------
# 문제 1: 데이터 병합 및 전처리
# --------------------------------------------------------------------------------

# 내가 최초 제출한 코딩
df_merged = pd.merge(df_purchases, df_products, on='product_id', how='left')
df_merged['customer_id'] = df_merged['customer_id'].fillna('Unknown')
df_merged.loc[df_merged['quantity'] < 1, 'quantity'] = 1
df_merged['purchase_date'] = pd.to_datetime(df_merged['purchase_date'])

print("--- Preprocessed Merged Data Head ---")
print(df_merged.head())


# --------------------------------------------------------------------------------
# 피드백 및 모범 답안
# --------------------------------------------------------------------------------

# - 데이터 병합: 문제의 요구사항에 맞게 'product_id'를 기준으로 두 파일을 정확하게 병합했습니다. 'how='left''를 사용하여 모든 구매 데이터를 유지하고 상품 정보를 추가한 방식이 올바릅니다.
# - 결측치 및 이상치 처리: 'fillna()'와 '.loc'을 사용해 결측치와 이상치를 효과적으로 처리했습니다. 특히 조건 기반으로 값을 바꾸는 '.loc'은 실전에서 매우 유용합니다.
# - 날짜 타입 변환: 'pd.to_datetime()'으로 'purchase_date' 열을 정확히 변환하여 이후 시계열 분석을 위한 준비를 마쳤습니다.

# [추가 학습: join 방식의 이해]
# Pandas의 'merge' 함수는 SQL의 JOIN과 유사하며, 'how' 인자를 통해 네 가지 주요 병합 방식을 지정할 수 있습니다.
# 1. 'left': 왼쪽 데이터프레임(df_purchases)의 모든 행을 기준으로 병합. 오른쪽 데이터프레임에 매칭되는 값이 없으면 NaN으로 채워짐. (현재 문제에 사용된 방식)
#    - 예시: 모든 구매 기록을 남기고, 해당 상품 정보가 없을 경우 NaN으로 표시하고 싶을 때 사용.
# 2. 'right': 오른쪽 데이터프레임(df_products)의 모든 행을 기준으로 병합.
#    - 예시: 모든 상품 정보를 남기고, 해당 상품에 대한 구매 기록이 없을 경우 NaN으로 표시하고 싶을 때 사용.
# 3. 'inner': 양쪽 데이터프레임에 공통으로 존재하는 행만 병합.
#    - 예시: 구매 기록과 상품 정보가 모두 있는 데이터만 보고 싶을 때 사용.
# 4. 'outer': 양쪽 데이터프레임의 모든 행을 병합. 매칭되지 않는 값은 NaN으로 채워짐.
#    - 예시: 모든 구매 기록과 모든 상품 정보를 한 테이블에서 보고 싶을 때 사용.
