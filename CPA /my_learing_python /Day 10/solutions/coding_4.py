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
# 문제 4: 날짜/시간 데이터 처리
# --------------------------------------------------------------------------------

# [내가 최초 제공한 코딩]
df['order_date'] = pd.to_datetime(df['order_date'])
print("datetime 타입으로 변환된 order_date 열:")
print(df['order_date'].head())

df['order_month'] = df['order_date'].dt.month
df['day_of_week'] = df['order_date'].dt.day_name()
print("\n날짜/시간 기반으로 추가된 열:")
print(df[['order_date', 'order_month', 'day_of_week']].head())

average_quantity_by_day = df.groupby('day_of_week')['quantity'].mean().reset_index()
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
average_quantity_by_day['day_of_week'] = pd.Categorical(average_quantity_by_day['day_of_week'], categories=days_order, ordered=True)
average_quantity_by_day = average_quantity_by_day.sort_values('day_of_week')

print("\n요일별 평균 주문 수량:")
print(average_quantity_by_day)


# [피드백 및 모범 답안]
# - 문제의 요구사항을 완벽하게 충족하는 훌륭한 코드입니다.
# - 'pd.to_datetime'으로 날짜/시간 타입을 변환하고, '.dt' 접근자를 사용해 월, 요일 등을 추출한 방식은 Pandas 날짜 처리의 정석입니다.
# - 'groupby'를 통해 요일별 평균을 계산하고, 'pd.Categorical'과 'sort_values'를 사용하여 요일 순서를 올바르게 정렬한 점은 매우 뛰어납니다. 이는 데이터 분석 결과의 가독성을 높이는 고급 기법입니다.

# [추가 학습]
# - 'pd.to_datetime'은 'format' 인자를 사용하여 다양한 형식의 날짜 문자열도 변환할 수 있습니다.
# - 'dt' 접근자를 사용하면 'dt.year', 'dt.quarter', 'dt.isoweekday()' 등 더 다양한 날짜/시간 정보를 추출할 수 있습니다.
# - 'resample' 함수를 사용하면 일별 데이터를 주 단위, 월 단위 등으로 집계하는 작업을 더 편리하게 수행할 수 있습니다.
