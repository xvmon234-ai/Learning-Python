# further_study.py

import pandas as pd
import numpy as np

# ==============================================================================
# [FURTHER STUDY] Pandas 메서드 체이닝 (Method Chaining)
# ==============================================================================

# --- [학습 목표] ---
"""
Pandas에서 **메서드 체이닝(Method Chaining)**의 개념을 이해하고,
이를 활용하여 코드를 더 간결하고 가독성 있게 작성하는 방법을 학습합니다.
특히, 데이터를 단계적으로 처리할 때 중간 변수 없이 연산을 연결하는 이점을 파악합니다.
"""

# --- [이론 설명] ---
"""
메서드 체이닝은 Pandas DataFrame 또는 Series 객체가 메서드를 호출한 후,
그 결과가 다시 DataFrame 또는 Series 객체를 반환할 때,
이 반환된 객체에 곧바로 다음 메서드를 호출하는 코딩 스타일을 말합니다.

이는 마치 "물 흐르듯이" 데이터를 처리하는 과정처럼 보이며,
각 연산의 결과가 다음 연산의 입력으로 바로 연결됩니다.

**주요 이점:**
1.  **코드 간결성**: 여러 줄에 걸쳐 작성될 코드를 한 줄 또는 적은 줄로 줄일 수 있습니다.
2.  **가독성**: 데이터 처리의 논리적인 흐름을 위에서 아래로(또는 왼쪽에서 오른쪽으로) 한눈에 파악하기 쉽습니다.
3.  **중간 변수 불필요**: 임시 데이터를 저장할 중간 변수를 생성할 필요가 없어 메모리 사용 효율을 높이고 코드 노이즈를 줄입니다.
"""

# --- [예시 데이터프레임] ---
data = {'Category': ['Electronics', 'Clothes', 'Electronics', 'Books', 'Clothes', 'Books', 'Electronics'],
        'Product': ['TV', 'Shirt', 'Laptop', 'Novel', 'Pants', 'Magazine', 'Monitor'],
        'Quantity': [10, 25, 5, 15, 30, 20, 8],
        'Price': [500, 30, 1200, 20, 40, 15, 350],
        'Salesperson': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie', 'Alice']}
sales_df = pd.DataFrame(data)

print("--- 원본 sales_df ---")
print(sales_df)

# --- [체이닝 적용 전 (단계별 코드)] ---
print("\n--- 체이닝 적용 전: 단계별 코드 ---")

# 1. 'Category'별로 그룹화
grouped_by_category = sales_df.groupby('Category')

# 2. 'Quantity'의 합계 계산
sum_quantity = grouped_by_category['Quantity'].sum()

# 3. 결과를 DataFrame으로 변환
final_result_df = sum_quantity.reset_index()

print(final_result_df)

# --- [체이닝 적용 후 (간결한 코드)] ---
print("\n--- 체이닝 적용 후: 간결한 코드 ---")

chained_result_df = sales_df.groupby('Category')['Quantity'].sum().reset_index()

print(chained_result_df)


# --- [다른 체이닝 예시: 여러 연산 연결] ---
print("\n--- 다른 체이닝 예시: 필터링 + 그룹화 + 집계 + 정렬 ---")

# 목표: 판매 수량이 10개 이상인 제품만 필터링하고, 카테고리별 총 판매액(Quantity * Price)을 계산 후,
# 총 판매액이 높은 순서대로 정렬하여 상위 2개 카테고리만 출력하기

complex_chained_result = (
    sales_df[sales_df['Quantity'] >= 10] # 1. 조건에 맞는 행 필터링
    .assign(Total_Sales = lambda x: x['Quantity'] * x['Price']) # 2. 새로운 컬럼 생성
    .groupby('Category') # 3. 'Category'별로 그룹화
    .agg(Sum_Total_Sales = ('Total_Sales', 'sum')) # 4. 총 판매액 합계 집계
    .sort_values(by='Sum_Total_Sales', ascending=False) # 5. 총 판매액 기준으로 내림차순 정렬
    .head(2) # 6. 상위 2개 카테고리 선택
    .reset_index() # 7. 인덱스 리셋하여 DataFrame 형태로
)

print(complex_chained_result)

# --- [학습 요약] ---
"""
**체이닝을 사용할 때의 고려사항:**
* **가독성 유지**: 체이닝이 너무 길어지면 오히려 가독성을 해칠 수 있습니다. 적절한 줄 바꿈(`()`)을 사용하여 코드를 구조화하는 것이 중요합니다.
* **중간 결과 확인**: 디버깅 시 각 단계의 중간 결과를 확인하기 어려울 수 있습니다. 필요하다면 중간 변수에 할당하여 디버깅하는 것도 좋은 방법입니다.
* **성능**: 대부분의 경우 체이닝이 성능상 큰 이점을 주지는 않지만, 코드를 더 깔끔하게 만들어줍니다. 일부 복잡한 연산에서는 미묘한 성능 차이가 있을 수 있으나, 가독성 향상이 주된 목적입니다.

메서드 체이닝은 Pandas를 효율적으로 사용하는 데 필수적인 기술이며, 데이터를 가공하고 분석하는 과정을 명확하고 간결하게 표현하는 데 큰 도움이 됩니다.
"""
