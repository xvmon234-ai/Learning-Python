# --- [최초 나의 코딩] ---
import pandas as pd
import numpy as np

data = {'A': [1, 2, np.nan, 4, 5],
        'B': [np.nan, 6, 7, np.nan, 9],
        'C': ['apple', 'banana', 'cherry', 'date', np.nan],
        'D': [10, 20, 30, 40, 50]}

sample_data = pd.DataFrame(data)
sample_data_copied = sample_data.copy()

null_deleted = sample_data_copied.dropna(subset = ["A", "C"], how="any", axis=0)

print("\n --- A, C Null Deleted --- ")
print(null_deleted)


# --- [코드 실행 결과] ---
"""
 --- A, C Null Deleted ---
     A    B       C   D
0  1.0  NaN   apple  10
1  2.0  6.0  banana  20
3  4.0  NaN    date  40
"""

# --- [피드백] ---
"""
정말 완벽하게 문제를 해결하셨습니다! `df.dropna()` 메서드의 `subset`과 `how` 매개변수를 정확히 이해하고 적용하셨어요.

1.  **DataFrame 복사**: `sample_data.copy()`를 사용해 원본 데이터를 보호하고 작업용 복사본을 만든 것은 매우 좋은 습관입니다. 실제 데이터 분석에서 원본 데이터의 불변성을 유지하는 것은 중요합니다.
2.  **특정 컬럼 기준 결측치 제거**: `sample_data_copied.dropna(subset=["A", "C"], how="any", axis=0)` 구문은 'A' 컬럼 또는 'C' 컬럼 중 **하나라도** 결측치(NaN)가 있는 행을 정확히 식별하여 제거했습니다.
    * `subset=["A", "C"]`: 결측치를 확인할 컬럼을 명확히 지정했습니다.
    * `how="any"`: `subset`으로 지정된 컬럼들 중 하나라도 NaN이 있다면 해당 행을 삭제하라는 의미입니다. 문제의 요구사항과 정확히 일치합니다.
    * `axis=0`: 기본값이기도 하지만, 명시적으로 행(row)을 삭제하겠다고 지정한 점도 좋습니다.

이 풀이는 `dropna()`의 `subset` 기능을 활용하는 모범적인 예시입니다. 특정 조건에 따라 데이터를 정제할 때 매우 유용하게 쓰일 수 있습니다.
"""

# --- [모범 답안] ---
import pandas as pd
import numpy as np

data = {'A': [1, 2, np.nan, 4, 5],
        'B': [np.nan, 6, 7, np.nan, 9],
        'C': ['apple', 'banana', 'cherry', 'date', np.nan],
        'D': [10, 20, 30, 40, 50]}

sample_data = pd.DataFrame(data)

# 원본 데이터 보호를 위해 복사본 생성
df_for_problem = sample_data.copy()

# 'A' 또는 'C' 컬럼 중 하나라도 결측치가 있는 행 제거
# subset에 ['A', 'C'] 지정, how='any' (기본값이므로 생략 가능)
cleaned_df = df_for_problem.dropna(subset=['A', 'C'], how='any', axis=0)

print("\n--- 'A' 또는 'C' 컬럼에 결측치가 있는 행 제거 후 ---")
print(cleaned_df)


# --- [학습 기록] ---
"""
**학습 질문**: 특정 컬럼들만을 기준으로 삼아 결측치가 포함된 행을 삭제하려면 어떻게 해야 할까? `dropna()` 메서드의 `subset` 매개변수는 언제 사용해야 할까?

**문제 해결**:
1.  **데이터프레임 복사**: 원본 `sample_data`의 무결성을 유지하기 위해 `copy()` 메서드를 사용해 새 DataFrame `sample_data_copied`를 생성했습니다.
2.  **`dropna()`와 `subset` 활용**: `sample_data_copied.dropna(subset=["A", "C"], how="any", axis=0)` 구문을 사용하여 문제를 해결했습니다.
    * `subset=["A", "C"]`: `dropna()`가 'A'와 'C' 컬럼에 대해서만 결측치를 검사하도록 지시했습니다. 이 매개변수 덕분에 'B' 컬럼에 `NaN`이 있어도 'A'나 'C'에 `NaN`이 없으면 해당 행이 삭제되지 않았습니다.
    * `how="any"`: `subset`으로 지정된 컬럼들 중 **단 하나라도** `NaN`이 존재하면 해당 행을 삭제하도록 설정했습니다. 이는 문제의 "하나라도"라는 조건에 부합했습니다.
    * `axis=0`: 행을 삭제하는 기본 동작을 명시적으로 지정했습니다.
3.  **결과 확인**: 출력된 DataFrame에서 행 인덱스 2번 (A가 NaN)과 4번 (C가 NaN)이 성공적으로 제거되었음을 확인했습니다. 이는 `subset` 매개변수가 특정 컬럼에 초점을 맞춰 결측치를 처리하는 데 매우 효과적임을 보여줍니다.

**추가 학습**:
* **`dropna()`의 `subset` 매개변수**: 이 매개변수는 특정 컬럼(들)에만 집중하여 결측치를 처리할 때 매우 강력합니다. 예를 들어, `Age`와 `Income` 컬럼에 결측치가 있을 때만 해당 고객 데이터를 삭제하고 싶을 때 유용합니다. 모든 컬럼을 대상으로 삭제하는 것보다 데이터 손실을 최소화하면서 필요한 정제를 수행할 수 있습니다.
* **`how='any'` vs `how='all'` with `subset`**:
    * `subset=['col1', 'col2'], how='any'`: `col1` 또는 `col2` 중 하나라도 `NaN`이면 삭제.
    * `subset=['col1', 'col2'], how='all'`: `col1`과 `col2` **모두** `NaN`일 때만 삭제.
    이 두 가지 조합은 데이터 정제 전략에 따라 다르게 적용될 수 있음을 이해하는 것이 중요합니다.
"""
