# ==============================================================================
# [추가 학습: Pandas groupby().transform()과 groupby().apply()의 비교]
# ==============================================================================

# **개요**:
# Pandas에서 `groupby()`는 데이터를 그룹별로 나누는 강력한 도구입니다. 이 그룹화된 데이터에 연산을 적용할 때 `transform()`과 `apply()`는 모두 유용하지만, 작동 방식과 반환하는 결과의 형태에 중요한 차이가 있습니다. 이 차이를 이해하는 것은 복잡한 그룹별 연산을 정확하게 수행하는 데 필수적입니다.

# **1. `groupby().transform()`**

# * **목적**: 그룹별 연산을 수행한 결과를 **원본 DataFrame 또는 Series의 인덱스와 동일한 형태로 반환**할 때 사용됩니다. 즉, 입력과 출력의 '모양(shape)'이 같습니다.
# * **작동 방식**:
#     * 각 그룹에 함수를 적용합니다.
#     * 함수의 결과는 각 그룹의 원래 크기로 '확장'되어 원본 DataFrame의 해당 위치에 다시 매핑됩니다.
#     * 주로 그룹별 통계량(평균, 중앙값 등)으로 결측치를 채우거나, 그룹별로 데이터를 정규화하는 등의 '변환' 작업에 사용됩니다.
# * **특징**:
#     * 반환되는 Series/DataFrame의 인덱스가 원본과 일치합니다.
#     * `transform`에 전달되는 함수는 각 그룹의 Series(`x`)를 입력받아 하나의 스칼라 값 또는 `x`와 동일한 크기의 Series를 반환해야 합니다.
# * **예시**: 그룹별 평균으로 결측치 채우기, 그룹별 스케일링.

# **2. `groupby().apply()`**

# * **목적**: 그룹별 연산을 수행한 후, 그 결과를 **더 유연한 형태**로 반환할 때 사용됩니다. `transform`보다 훨씬 광범위한 연산에 적용할 수 있습니다.
# * **작동 방식**:
#     * 각 그룹에 함수를 적용합니다.
#     * 함수의 결과는 각 그룹에 대해 개별적으로 수집되며, 이 수집된 결과들이 합쳐져 최종 DataFrame 또는 Series가 됩니다.
#     * 그룹별 필터링, 복잡한 사용자 정의 함수 적용, 여러 컬럼에 걸친 연산 등 다양한 시나리오에 사용됩니다.
# * **특징**:
#     * 반환되는 Series/DataFrame의 shape이 원본과 다를 수 있습니다 (요약 통계, 필터링된 부분집합 등).
#     * `apply`에 전달되는 함수는 각 그룹의 DataFrame 또는 Series(`x`)를 입력받아 스칼라, Series, 또는 DataFrame을 반환할 수 있습니다.
# * **예시**: 그룹별 상위 N개 행 추출, 그룹별 특정 조건 만족하는 행 필터링, 그룹별 복합 통계 계산.

# **주요 차이점 요약**:

# | 특징          | `transform()`                              | `apply()`                                   |
# | :------------ | :----------------------------------------- | :------------------------------------------ |
# | **반환 형태** | 원본 DataFrame/Series와 동일한 shape       | 유연한 형태 (스칼라, Series, DataFrame)     |
# | **목적** | 그룹별 '변환' (값 채우기, 정규화)          | 그룹별 '적용' (복잡한 연산, 요약, 필터링)   |
# | **속도** | 일반적으로 더 빠름 (최적화된 경우가 많음) | 더 유연하지만, 경우에 따라 느릴 수 있음     |

# **언제 무엇을 사용할까?**

# * **`transform()`**:
#     * 그룹별로 계산된 값을 원본 데이터의 해당 위치에 다시 매핑해야 할 때.
#     * 예: 그룹별 평균으로 NaN 채우기, 그룹 내 데이터 스케일링.
# * **`apply()`**:
#     * `transform`으로는 처리하기 어려운 복잡한 그룹별 연산이 필요할 때.
#     * 그룹별로 요약된 통계, 필터링된 부분집합, 또는 완전히 새로운 구조의 데이터를 반환해야 할 때.
#     * 예: 각 그룹에서 'Sales'가 가장 높은 상위 3개 행만 가져오기.

# **결론**: `transform()`은 그룹별 연산 결과를 원본 구조에 다시 맞춰야 할 때 매우 효율적이며, `apply()`는 훨씬 더 넓은 범위의 사용자 정의 그룹 연산에 유연하게 대응할 수 있습니다. 상황에 맞는 적절한 메서드를 선택하는 것이 중요합니다.

# --- 실습 예시: transform()과 apply() 비교 ---
import pandas as pd
import numpy as np

data = {'Category': ['A', 'A', 'B', 'B', 'A', 'B'],
        'Value': [10, 20, 30, np.nan, 15, 40],
        'Other': [1, 2, 3, 4, 5, 6]}
df = pd.DataFrame(data)

print("--- 원본 DataFrame ---")
print(df)

# 1. groupby().transform() 예시: 그룹별 평균으로 결측치 채우기
# 각 그룹의 평균이 계산된 후, 원본 'Value' 컬럼의 NaN 위치에 매핑됩니다.
df_transformed = df.copy()
df_transformed['Value_filled_transform'] = df_transformed.groupby('Category')['Value'].transform(lambda x: x.fillna(x.mean()))

print("\n--- transform()으로 'Value' 결측치 채운 후 ---")
print(df_transformed)
print(f"변환된 컬럼의 결측치 확인:\n{df_transformed['Value_filled_transform'].isnull().sum()}")


# 2. groupby().apply() 예시 1: 그룹별 평균 계산 (apply가 Series를 반환)
# 각 그룹의 평균이 요약된 형태로 반환됩니다. (transform과 유사한 요약 기능)
df_applied_mean = df.groupby('Category')['Value'].apply(lambda x: x.mean())

print("\n--- apply()로 그룹별 평균 계산 후 (요약) ---")
print(df_applied_mean)


# 3. groupby().apply() 예시 2: 그룹별 상위 2개 행 추출 (apply가 DataFrame을 반환)
# 각 그룹에 대해 복잡한 연산을 수행하고, 원본과 다른 형태의 DataFrame을 반환합니다.
def get_top_n(group_df, n=2):
    return group_df.nlargest(n, 'Value')

df_applied_top_n = df.groupby('Category').apply(get_top_n)

print("\n--- apply()로 그룹별 상위 2개 Value 행 추출 후 ---")
print(df_applied_top_n)
