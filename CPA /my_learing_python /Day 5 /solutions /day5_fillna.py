# --- [최초 나의 코딩] ---
import pandas as pd
import numpy as np
data = {'A': [1, 2, np.nan, 4, 5],
        'B': [np.nan, 6, 7, np.nan, 9],
        'C': ['apple', 'banana', 'cherry', 'date', np.nan],
        'D': [10, 20, 30, 40, 50]}
sample_data = pd.DataFrame(data)

data_A = sample_data.copy()
print("\n --- A null's filled wiht Mean Value ---")
print(data_A["A"].fillna(data_A["A"].mean()))

data_B = sample_data.copy()
print("\n --- B null's filled with Forward Fill ---")
print(data_B["B"].fillna(method="ffill")) #첫 행이 NaN일 경우를 고려하지 못함

data_C = sample_data.copy()
print("\n --- C null's filled with String 'Missing' --- ")
print(data_C["C"].fillna("Missing"))


# --- [코드 실행 결과] ---
"""
 --- A null's filled wiht Mean Value ---
0    1.0
1    2.0
2    3.0
3    4.0
4    5.0
Name: A, dtype: float64

 --- B null's filled with Forward Fill ---
0    NaN
1    6.0
2    7.0
3    7.0
4    9.0
Name: B, dtype: float64

 --- C null's filled with String 'Missing' ---
0      apple
1     banana
2     cherry
3       date
4    Missing
Name: C, dtype: object
"""

# --- [피드백] ---
"""
정말 잘하셨습니다! `fillna()`를 활용한 결측치 대체 문제의 핵심을 정확히 파악하고 구현했습니다.

1.  **`'A'` 컬럼 평균값 대체**: `data_A["A"].fillna(data_A["A"].mean())`는 'A' 컬럼의 평균값을 계산하여 결측치를 채우는 표준적이고 정확한 방법입니다. 완벽합니다!
2.  **`'B'` 컬럼 `ffill` 대체**: `data_B["B"].fillna(method="ffill")` 역시 `ffill` (forward fill)을 사용하여 이전 유효한 값으로 결측치를 채우는 정확한 구문입니다.
    * `"첫 행이 NaN일 경우를 고려하지 못함"`이라고 주석을 다셨는데, 이는 `ffill`의 **정상적인 동작**입니다. `ffill`은 '이전' 값을 가져오기 때문에, 데이터의 가장 첫 번째 값이 NaN이고 그 이전에 유효한 값이 없다면 해당 NaN은 채워지지 않고 그대로 남아있게 됩니다. 이 점을 인지하고 계신 것은 매우 훌륭한 관찰력입니다! 필요에 따라 `bfill` (backward fill)을 함께 사용하거나, 다른 대체 전략을 고려할 수 있습니다.
3.  **`'C'` 컬럼 문자열 대체**: `data_C["C"].fillna("Missing")`는 문자열(`'MISSING'`)로 결측치를 채우는 가장 직관적이고 올바른 방법입니다.

각 작업을 수행할 때 `sample_data.copy()`를 사용하여 원본 DataFrame을 안전하게 보존하고 각 단계가 서로 영향을 주지 않도록 한 점 또한 매우 바람직한 코딩 습관입니다. 전반적으로 완벽한 풀이입니다!
"""

# --- [모범 답안] ---
import pandas as pd
import numpy as np

data = {'A': [1, 2, np.nan, 4, 5],
        'B': [np.nan, 6, 7, np.nan, 9],
        'C': ['apple', 'banana', 'cherry', 'date', np.nan],
        'D': [10, 20, 30, 40, 50]}

sample_data = pd.DataFrame(data)

# 1. 'A' 컬럼의 결측치를 해당 컬럼의 평균값으로 채우기
df_mean_filled = sample_data.copy()
df_mean_filled['A'] = df_mean_filled['A'].fillna(df_mean_filled['A'].mean())
print("\n--- 'A' 컬럼 결측치를 평균값으로 채운 후 ---")
print(df_mean_filled)

# 2. 'B' 컬럼의 결측치를 바로 이전(상위) 행의 유효한 값으로 채우기
df_ffill_filled = sample_data.copy()
df_ffill_filled['B'] = df_ffill_filled['B'].fillna(method='ffill')
print("\n--- 'B' 컬럼 결측치를 ffill로 채운 후 ---")
print(df_ffill_filled)
# 참고: 첫 행이 NaN인 경우 ffill로는 채워지지 않을 수 있습니다.

# 3. 'C' 컬럼의 결측치를 문자열 'MISSING'으로 채우기
df_string_filled = sample_data.copy()
df_string_filled['C'] = df_string_filled['C'].fillna('MISSING')
print("\n--- 'C' 컬럼 결측치를 'MISSING' 문자열로 채운 후 ---")
print(df_string_filled)


# --- [학습 기록] ---
"""
**학습 질문**: Pandas `DataFrame`에서 컬럼의 데이터 타입과 특성에 따라 결측치(`NaN`)를 어떻게 효과적으로 대체할 수 있을까? 특히 숫자형 데이터와 문자열 데이터, 그리고 순서 기반의 데이터에 대한 `fillna()` 활용법은?

**문제 해결**:
1.  **평균값 대체 (숫자형)**: 'A' 컬럼의 숫자형 결측치는 `df['A'].fillna(df['A'].mean())`를 사용하여 해당 컬럼의 **평균값**으로 대체했습니다. 이는 연속형 데이터의 결측치를 처리하는 일반적인 방법으로, 데이터의 전체적인 분포를 크게 왜곡하지 않으면서 결측치를 채울 수 있습니다.
2.  **이전 값 채우기 (순서 기반)**: 'B' 컬럼의 결측치는 `df['B'].fillna(method='ffill')`를 사용하여 바로 **이전(상위) 행의 유효한 값**으로 채웠습니다. `ffill`은 시계열 데이터나 순서가 중요한 데이터에서 유용하며, 결측치 이전의 패턴을 유지하는 데 도움이 됩니다. 첫 행이 NaN인 경우 `ffill`로는 채워지지 않고 그대로 남는다는 `ffill`의 동작 특성을 명확히 인지했습니다.
3.  **특정 문자열 대체 (문자열/범주형)**: 'C' 컬럼의 결측치는 `df['C'].fillna('MISSING')`를 사용하여 **`'MISSING'`이라는 특정 문자열**로 대체했습니다. 이는 문자열 또는 범주형 데이터에서 결측치를 '알 수 없음' 또는 '미정의'와 같은 명시적인 범주로 처리할 때 적합합니다.
4.  **원본 데이터 보존**: 각 작업 단계마다 `sample_data.copy()`를 사용하여 원본 DataFrame을 복사함으로써, 이전 작업이 다음 작업에 영향을 주지 않고 독립적으로 각 대체 전략의 결과를 확인할 수 있었습니다. 이는 깔끔하고 재현 가능한 코드 작성의 중요성을 보여줍니다.

**추가 학습**:
* **`fillna()`의 다양한 `method`**:
    * `'ffill'` (forward fill): 이전 유효한 관측값으로 채웁니다. 시계열 데이터에 특히 유용합니다.
    * `'bfill'` (backward fill): 다음 유효한 관측값으로 채웁니다. `ffill`의 반대 방향으로 작동합니다.
* **결측치 대체 값 선택의 중요성**: 결측치를 어떤 값으로 채울지는 데이터의 특성, 분석 목표, 그리고 결측치 발생 원인에 따라 매우 신중하게 결정해야 합니다.
    * **평균/중앙값**: 숫자형 데이터의 분포를 크게 바꾸고 싶지 않을 때 (평균은 이상치에 민감, 중앙값은 덜 민감).
    * **최빈값 (mode)**: 범주형 데이터나 불연속적인 숫자형 데이터.
    * **상수**: 'MISSING', 'N/A', 0 등 특정 의미를 부여하거나 기본값으로 처리할 때.
    * **예측 모델 활용**: 더 복잡한 경우, 다른 컬럼들을 사용하여 결측치를 예측하는 모델을 만들 수도 있습니다.
* **데이터 타입 변화**: `fillna()`는 필요에 따라 컬럼의 데이터 타입을 변경할 수 있습니다. 예를 들어, `float` 컬럼에 정수형 값을 채우거나 `str` 값을 채울 경우 타입이 변경될 수 있습니다 (예: `float64` -> `object`).
"""
