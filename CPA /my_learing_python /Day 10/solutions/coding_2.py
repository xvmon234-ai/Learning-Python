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
# 문제 2: map()과 replace() 활용
# --------------------------------------------------------------------------------

# [내가 최초 제공한 코딩]
df['customer_num_id'] = df['customer_id'].factorize()[0] + 1
print("\ncustomer_num_id 열이 추가된 DataFrame:")
print(df)

status_mapping = {
    'Pending': '처리 중',
    'Completed': '완료',
    'Cancelled': '취소'
}
df['status'] = df['status'].replace(status_mapping)
print("\nstatus 열의 값이 변환된 DataFrame:")
print(df)


# [피드백 및 모범 답안]
# - 문제의 요구사항을 완벽하게 충족하는 훌륭한 코드입니다.
# - 'customer_id'를 고유한 숫자 ID로 변환하기 위해 'map' 대신 'factorize'를 사용한 점이 매우 좋습니다. 'factorize'는 범주형 데이터를 숫자형으로 인코딩하는 데 매우 효율적인 방법입니다.
# - 'status' 열의 값을 'replace'와 딕셔너리를 사용해 변환한 방식은 Pandas의 표준적인 방법입니다. 가독성이 높아 추천되는 방법입니다.

# [추가 학습]
# - 'map' 함수는 딕셔너리에 정의되지 않은 값이 있으면 'NaN'으로 변환되므로, 모든 값을 매핑할 필요가 있을 때 유용합니다.
# - 'replace'는 여러 값들을 한 번에 바꾸거나, 정규 표현식 기반으로 값을 교체할 때도 유용합니다.
