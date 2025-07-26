import pandas as pd
import numpy as np

# --- 1. 데이터프레임 생성 및 초기 상태 확인 ---
data = {'Region': ['East', 'West', 'East', 'West', 'East', 'East'],
        'Product': ['A', 'B', 'A', 'C', 'B', 'A'],
        'Sales': [100, 150, np.nan, 200, 120, np.nan]}
sales_data = pd.DataFrame(data)

print("--- 원본 sales_data ---")
print(sales_data)
print("\n--- Sales 컬럼의 결측치 위치 (True = NaN) ---")
print(sales_data['Sales'].isnull())
print("-" * 50)

# --- 2. groupby() 메서드 이해하기 ---
# groupby()는 특정 컬럼(들)의 고유한 값을 기준으로 데이터프레임을 여러 개의 '그룹'으로 분할하는 메서드입니다.
# 직접적으로 데이터를 변경하지는 않고, 그룹별 연산을 위한 '그룹 객체'를 반환합니다.

print("--- 'Region' 컬럼으로 그룹화된 객체 (직접 출력하면 정보성 메시지가 나옴) ---")
print(sales_data.groupby('Region'))
print("-" * 50)

# 그룹별 통계량 계산 예시: 각 Region의 평균 Sales
# 'East' 그룹과 'West' 그룹의 Sales 평균이 각각 계산됩니다.
region_avg_sales = sales_data.groupby('Region')['Sales'].mean()
print("--- 'Region'별 Sales 평균 ---")
print(region_avg_sales)
print("-" * 50)

# --- 3. transform() 메서드 이해하기 ---
# transform()은 groupby()와 함께 사용될 때 강력한 기능을 발휘합니다.
# 1. 그룹별로 어떤 연산(예: mean, sum, custom function)을 수행합니다.
# 2. 그 연산의 결과를 '원본 DataFrame의 인덱스(크기)'에 맞춰서 확장하여 반환합니다.
#    이것이 핵심입니다. 단순히 그룹별 하나의 값을 반환하는 것이 아니라,
#    원본 데이터의 각 행이 속한 그룹의 연산 결과를 해당 행의 위치에 맞게 채워줍니다.
#    따라서 fillna()와 같이 원본 데이터의 형태를 유지하면서 값을 채울 때 매우 유용합니다.

# 예시: 각 Sales 값 옆에 해당 Region의 평균 Sales 값을 추가하고 싶을 때
# 이 결과를 보면 각 'Sales' 값이 어떤 'Region'에 속해있는지에 따라 그 Region의 평균이 매칭됩니다.
sales_mean_transformed = sales_data.groupby('Region')['Sales'].transform('mean')
print("--- transform()을 통해 확장된 Region별 Sales 평균 ---")
print(sales_mean_transformed)
print("-" * 50)

# --- 4. fillna()와 transform()의 조합을 통한 조건부 결측치 대체 ---
# 이제 'Sales' 컬럼의 결측치(NaN)를 해당 그룹의 평균으로 채우는 방법을 조합해봅니다.
# 1. sales_data.groupby('Region')['Sales']: 'Region'별로 'Sales' 컬럼을 그룹화합니다.
# 2. .transform(lambda x: x.fillna(x.mean())):
#    - transform() 내부의 `lambda x`에서 `x`는 각 그룹의 'Sales' Series를 의미합니다.
#    - `x.mean()`: 해당 그룹의 'Sales' 평균을 계산합니다.
#    - `x.fillna(x.mean())`: 해당 그룹 내에서 `x` (현재 그룹의 Sales Series)의 결측치를
#      바로 위에서 계산한 `x.mean()` 값으로 채웁니다.
#    - transform()은 이 결과를 원본 sales_data['Sales']와 동일한 형태로 반환합니다.
# 3. sales_data['Sales'] = ... : 최종적으로 이 결과를 원본 DataFrame의 'Sales' 컬럼에 재할당하여
#    결측치가 채워진 새로운 'Sales' 컬럼으로 업데이트합니다.

print("--- 결측치 대체 전 sales_data ---")
print(sales_data)

# 실제 결측치 대체 수행
sales_data['Sales'] = sales_data.groupby('Region')['Sales'].transform(lambda x: x.fillna(x.mean()))

print("\n--- 결측치가 대체된 sales_data ---")
print(sales_data)
print("\n--- 대체 후 Sales 컬럼의 결측치 확인 ---")
print(sales_data['Sales'].isnull()) # 모든 False가 출력되어야 함 (결측치 없음)
print("-" * 50)

# --- 5. apply() 메서드와 lambda 함수 이해하기 ---

## 5.1. apply() 메서드
# apply()는 Series 또는 DataFrame의 각 요소(혹은 행/열)에 함수를 적용할 때 사용됩니다.
# groupby()와 함께 사용될 때는 각 그룹에 함수를 적용합니다.
# apply()는 transform()보다 더 유연하지만, 결과 형태가 다양할 수 있습니다.
# transform()은 항상 원본과 같은 크기의 Series/DataFrame을 반환하는 반면,
# apply()는 그룹별로 하나의 스칼라 값, Series, 또는 DataFrame을 반환할 수 있습니다.

print("--- apply() 메서드 예시 ---")

# Series에 apply 적용 (각 값에 10 더하기)
s = pd.Series([1, 2, 3])
s_plus_10 = s.apply(lambda x: x + 10)
print("Series에 apply 적용 (각 값에 10 더하기):")
print(s_plus_10)
print("-" * 30)

# DataFrame의 특정 컬럼에 apply 적용 (각 Sales 값의 10% 계산)
sales_percentage = sales_data['Sales'].apply(lambda x: x * 0.10)
print("Sales 컬럼에 apply 적용 (각 값의 10% 계산):")
print(sales_percentage)
print("-" * 30)

# groupby()와 apply() 조합 예시: 각 Region의 Sales 합계 구하기
# 이 경우 transform('sum')과 결과는 같지만, apply는 더 복잡한 로직을 넣을 수 있습니다.
region_sum_sales_apply = sales_data.groupby('Region')['Sales'].apply(sum)
print("groupby()와 apply() 조합 (Region별 Sales 합계):")
print(region_sum_sales_apply)
print("-" * 30)

# apply()를 이용한 결측치 대체 (transform과 유사한 결과)
# 이 방법도 가능하지만, transform이 이 특정 케이스(그룹별로 채우고 원본 크기 유지)에는 더 효율적입니다.
sales_data_apply_filled = sales_data.copy() # 원본 데이터 복사
sales_data_apply_filled['Sales'] = sales_data_apply_filled.groupby('Region')['Sales'].apply(lambda x: x.fillna(x.mean()))
print("apply()를 이용한 결측치 대체 (결과는 transform과 유사):")
print(sales_data_apply_filled)
print("-" * 50)


## 5.2. lambda 함수
# lambda 함수는 작은 익명(이름이 없는) 함수를 만들 때 사용됩니다.
# 주로 `apply()`, `transform()`, `sort_values()` 등의 메서드 내에서
# 간단한 일회성 연산을 정의할 때 유용하게 쓰입니다.

# 문법: lambda arguments: expression

print("--- lambda 함수 예시 ---")

# 일반 함수 정의
def add_five(x):
    return x + 5

# lambda 함수로 동일한 기능 구현
add_five_lambda = lambda x: x + 5

print(f"일반 함수 (add_five(10)): {add_five(10)}")
print(f"lambda 함수 (add_five_lambda(10)): {add_five_lambda(10)}")
print("-" * 30)

# DataFrame 컬럼에 lambda 적용 예시
# 'Sales' 컬럼의 모든 값에 50을 더한 새로운 Series 생성
sales_plus_50 = sales_data['Sales'].apply(lambda x: x + 50)
print("Sales 컬럼에 lambda 적용 (각 값에 50 더하기):")
print(sales_plus_50)
print("-" * 50)

# --- 결론 ---
# - `groupby()`: 데이터를 그룹으로 나눕니다.
# - `transform()`: 그룹별 연산 결과를 원본 DataFrame의 형태에 맞춰 반환할 때 유용합니다. 특히 결측치 채우기처럼 원래 컬럼의 크기를 유지해야 할 때 강력합니다.
# - `apply()`: 그룹별로 더 복잡하거나 다양한 형태의 결과를 반환할 수 있는 유연한 함수 적용 메서드입니다.
# - `lambda`: 코드의 가독성을 높이고 간단한 함수를 즉석에서 정의할 때 사용하는 익명 함수입니다.

# 이 개념들을 잘 익혀두시면 Pandas를 이용한 데이터 전처리 및 분석에 큰 도움이 될 것입니다.
