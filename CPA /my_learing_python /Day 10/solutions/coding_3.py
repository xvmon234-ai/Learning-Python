import pandas as pd
import numpy as np

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
# 문제 3: 범주형 데이터 처리
# --------------------------------------------------------------------------------

# [내가 최초 제공한 코딩]
df.info(memory_usage='deep')
for col in ['product_id', 'customer_id', 'status']:
    df[col] = df[col].astype('category')
print("\n변환 후 DataFrame 정보:")
df.info(memory_usage='deep')


# [피드백 및 모범 답안]
# - 문제의 요구사항을 정확히 이해하고 'astype('category')'를 올바르게 적용했습니다.
# - 'df.info(memory_usage='deep')'를 사용하여 변환 전후의 메모리 사용량을 실제로 비교해본 점이 매우 좋습니다. 범주형 데이터 변환의 효과를 시각적으로 확인하는 좋은 방법입니다.
# - for 반복문을 사용하여 여러 열을 한 번에 처리한 코드도 효율적입니다.

# [추가 학습]
# - 범주형 데이터는 'cat.codes'를 통해 내부적으로 인코딩된 숫자 값을 확인할 수 있습니다.
# - 범주형 데이터는 문자열 데이터에 비해 메모리 효율이 좋고, 일부 연산에서 성능 이점을 가질 수 있습니다.
