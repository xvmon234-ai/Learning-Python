# ==============================================================================
# [추가 학습: fillna() 사용 시 데이터 타입(Dtype) 변경 고려사항]
# ==============================================================================

# **개요**:
# `fillna()` 메서드를 사용하여 결측치를 대체할 때, 때로는 컬럼의 데이터 타입(dtype)이 자동으로 변경될 수 있습니다.
# 이는 Pandas가 데이터의 일관성을 유지하고, 새로운 값이 기존 컬럼의 데이터 타입에 맞지 않을 경우
# 가장 적합하다고 판단되는 타입으로 변경하기 때문에 발생하는 현상입니다.
# 이러한 타입 변경은 예상치 못한 오류를 발생시키거나 데이터 분석에 영향을 줄 수 있으므로 이해하고 있어야 합니다.

# **데이터 타입 변경이 발생하는 일반적인 시나리오**:

# 1. **정수(int) 컬럼에 NaN(실수형)이 있는 경우**:
#    * Pandas에서 정수형 컬럼은 기본적으로 `NaN` 값을 표현할 수 없습니다. `NaN`은 부동 소수점(float) 타입으로 간주되기 때문입니다.
#    * 따라서 정수형 컬럼에 `NaN`이 포함되면 해당 컬럼은 자동으로 `float64` 타입으로 변환됩니다.
#    * 이 상태에서 `fillna(0)`와 같이 정수 값으로 채워도, 컬럼의 타입은 여전히 `float64`로 남아있을 수 있습니다 (예: `1.0`, `2.0`). 이는 Pandas가 컬럼 전체의 일관된 타입을 유지하려 하기 때문입니다.
#    * 만약 정수 타입으로 되돌리고 싶다면, `astype(int)` (단, NaN이 없어야 함) 또는 `astype('Int64')` (Pandas의 Nullable Integer 타입)를 명시적으로 사용해야 합니다.

# 2. **숫자형 컬럼에 문자열로 채우는 경우**:
#    * 숫자형 (`int`, `float`) 컬럼의 결측치를 `'Unknown'`, `'N/A'`와 같은 **문자열**로 채우면, 해당 컬럼의 데이터 타입은 숫자와 문자열을 모두 포함할 수 있는 가장 일반적인 타입인 `object` (파이썬 문자열이나 혼합 타입을 나타냄)로 변환됩니다.
#    * 이렇게 되면 해당 컬럼에 대해 더 이상 숫자형 연산(평균, 합계 등)을 직접 수행할 수 없게 됩니다.

# 3. **날짜/시간(datetime) 컬럼에 문자열/숫자로 채우는 경우**:
#    * `datetime64[ns]` 타입의 컬럼에 `NaT` (Not a Time) 대신 일반 문자열이나 숫자를 채우려 하면, `object` 타입으로 변환될 수 있습니다.

# **타입 변경을 고려해야 하는 이유**:

# * **연산 오류**: 숫자형 연산을 수행해야 하는데 `object` 타입으로 변경되어 오류가 발생하거나, 예상과 다른 결과가 나올 수 있습니다.
# * **메모리 사용**: `object` 타입은 일반적으로 숫자형 타입보다 더 많은 메모리를 사용합니다.
# * **일관성 유지**: 데이터 타입의 일관성이 깨지면 향후 데이터 처리 및 분석 과정에서 혼란을 야기할 수 있습니다.

# **해결 및 관리 방안**:

# * **`fillna()` 후 `astype()` 사용**: `fillna()`를 통해 값을 채운 후, 원하는 데이터 타입으로 명시적으로 변환합니다.
#     * 예: `df['col'] = df['col'].fillna(0).astype('Int64')` (Pandas Nullable Integer)
#     * 예: `df['col'] = df['col'].fillna(0).astype(int)` (NaN이 모두 채워진 경우)
# * **Pandas의 Nullable Dtypes 활용**: Pandas 1.0부터 도입된 새로운 정수형 (`Int64`, `Int32` 등)은 `NaN`을 저장할 수 있습니다. 이를 사용하면 `float`으로 자동 변환되는 것을 방지할 수 있습니다.
# * **결측치 처리 전략 재고**: 특정 컬럼의 데이터 타입이 중요한 경우, `fillna()` 대신 `dropna()`를 사용하거나, 해당 컬럼만 따로 처리하는 등의 전략을 고려할 수 있습니다.

# **결론**: `fillna()` 사용 시 단순히 값을 채우는 것을 넘어, 컬럼의 데이터 타입이 어떻게 변화할 수 있는지 예측하고, 필요하다면 `astype()`을 통해 명시적으로 타입을 관리하는 것이 견고한 데이터 전처리 과정의 중요한 부분입니다.

# --- 실습 예시: fillna()에 따른 데이터 타입 변화 ---
import pandas as pd
import numpy as np

# 1. 정수형 컬럼에 NaN이 있는 경우 (자동으로 float64로 변환)
print("\n--- 1. 정수형 컬럼 + NaN -> float64 변환 ---")
data1 = {'A': [1, 2, np.nan, 4]}
df1 = pd.DataFrame(data1)
print(f"원본 df1:\n{df1}")
print(f"원본 df1 dtypes:\n{df1.dtypes}")

# NaN을 0으로 채워도 여전히 float64
df1_filled = df1.fillna(0)
print(f"\nfillna(0) 후 df1_filled:\n{df1_filled}")
print(f"fillna(0) 후 df1_filled dtypes:\n{df1_filled.dtypes}")

# 정수형으로 다시 변환 (NaN이 없으므로 가능)
df1_filled_int = df1_filled.astype(int)
print(f"\nastype(int) 후 df1_filled_int:\n{df1_filled_int}")
print(f"astype(int) 후 df1_filled_int dtypes:\n{df1_filled_int.dtypes}")

# Nullable Integer 타입으로 변환 (NaN을 포함한 상태에서도 정수형 유지 가능)
df1_nullable_int = df1.astype('Int64') # 대문자 I
print(f"\nNullable Int64로 변환 후 df1_nullable_int:\n{df1_nullable_int}")
print(f"Nullable Int64로 변환 후 df1_nullable_int dtypes:\n{df1_nullable_int.dtypes}")
df1_nullable_int_filled = df1_nullable_int.fillna(0)
print(f"\nNullable Int64 상태에서 fillna(0) 후:\n{df1_nullable_int_filled}")
print(f"Nullable Int64 상태에서 fillna(0) 후 dtypes:\n{df1_nullable_int_filled.dtypes}") # .dtypes 추가

# 2. 숫자형 컬럼에 문자열로 채우는 경우
print("\n--- 2. 숫자형 컬럼에 문자열 채움 -> object 변환 ---")
data2 = {'B': [1.1, np.nan, 3.3]}
df2 = pd.DataFrame(data2)
print(f"원본 df2:\n{df2}")
print(f"원본 df2 dtypes:\n{df2.dtypes}")

df2_filled_str = df2.fillna('Unknown')
print(f"\nfillna('Unknown') 후 df2_filled_str:\n{df2_filled_str}")
print(f"fillna('Unknown') 후 df2_filled_str dtypes:\n{df2_filled_str.dtypes}")

# 3. 날짜/시간 컬럼에 문자열로 채우는 경우
print("\n--- 3. 날짜/시간 컬럼에 문자열 채움 -> object 변환 ---")
data3 = {'C': pd.to_datetime(['2023-01-01', np.nan, '2023-01-03'])}
df3 = pd.DataFrame(data3)
print(f"원본 df3:\n{df3}")
print(f"원본 df3 dtypes:\n{df3.dtypes}")

df3_filled_str = df3.fillna('Invalid Date')
print(f"\nfillna('Invalid Date') 후 df3_filled_str:\n{df3_filled_str}")
print(f"fillna('Invalid Date') 후 df3_filled_str dtypes:\n{df3_filled_str.dtypes}")
