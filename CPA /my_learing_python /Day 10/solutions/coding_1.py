import pandas as pd
import numpy as np

# --- 데이터 준비 ---
data = {
    'product_id': ['A101', 'B202', 'A101', 'C303', 'B202', 'A101', 'C303'],
    'order_date': ['2024-03-01', '2024-03-02', '2024-03-03', '2024-03-04', '2024-03-05', '2024-03-06', '2024-03-07'],
    'customer_id': ['cust1', 'cust2', 'cust1', 'cust3', 'cust2', 'cust1', 'cust3'],
    'quantity': [5, 10, 8, 12, 7, 3, 15],
    'price_per_item': [1000, 2000, 1000, 1500, 2000, 1000, 1500],
    'status': ['Pending', 'Completed', 'Completed', 'Cancelled', 'Completed', 'Pending', 'Completed']
}
df = pd.DataFrame(data)

# --------------------------------------------------------------------------------
# 문제 1: apply()와 lambda 함수 활용
# --------------------------------------------------------------------------------

# [내가 최초 제공한 코딩]
df['total_price'] = df['price_per_item'] * df['quantity']
df['price_level'] = df['total_price'].apply(lambda x: 'High' if x >= 10000 else ('Medium' if x >= 5000 else 'Low'))
print(df.head())


# [피드백 및 모범 답안]
# - 문제의 요구사항을 완벽하게 충족하는 훌륭한 코드입니다.
# - 'total_price'를 먼저 계산하고, 그 결과를 'apply'와 'lambda'를 사용해 'price_level'로 분류한 과정이 논리적이고 깔끔합니다.
# - 'apply'와 'lambda'를 사용한 3항 연산자로 복잡한 조건문을 한 줄로 간결하게 표현한 점이 특히 좋습니다.

# [추가 학습]
# - 'apply'와 'lambda' 대신 'pd.cut' 함수를 사용하면 연속적인 값을 범주로 나누는 작업을 더 효율적으로 수행할 수 있습니다.
#   - 예: 'bins = [0, 5000, 10000, np.inf]', 'labels = ['Low', 'Medium', 'High']', 'df['price_level'] = pd.cut(df['total_price'], bins=bins, labels=labels)'
