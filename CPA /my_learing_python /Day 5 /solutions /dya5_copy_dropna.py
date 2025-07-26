# --- [최초 나의 코딩] ---
import pandas as pd
import numpy as np

data = {'A': [1, 2, np.nan, 4, 5],
        'B': [np.nan, 6, 7, np.nan, 9],
        'C': ['apple', 'banana', 'cherry', 'date', np.nan],
        'D': [10, 20, 30, 40, 50]}

sample_data = pd.DataFrame(data)
sample_data_copied = sample_data.copy()

row_deleted = sample_data_copied.dropna(how='all', axis=0) #axis = 0(row), 1(column)

print("\n --- Row Deleted --- ")
print(row_deleted)

col_deleted = row_deleted.dropna(how="all", axis=1)

print("\n --- Column Deleted --- ")
print(col_deleted)


# --- [코드 실행 결과] ---
"""
 --- Row Deleted ---
     A    B       C   D
0  1.0  NaN   apple  10
1  2.0  6.0  banana  20
2  NaN  7.0  cherry  30
3  4.0  NaN    date  40
4  5.0  9.0     NaN  50

 --- Column Deleted ---
     A    B       C   D
0  1.0  NaN   apple  10
1  2.0  6.0  banana  20
2  NaN  7.0  cherry  30
3  4.0  NaN    date  40
4  5.0  9.0     NaN  50
"""

# --- [피드백] ---
"""
코드 정말 잘 작성하셨습니다! 모든 요구사항을 정확하게 반영했고, `dropna()` 메서드의 `how='all'`과 `axis` 매개변수 사용법을 완벽하게 이해하고 적용했습니다.

1.  **DataFrame 복사**: `sample_data.copy()`를 사용하여 원본 데이터를 안전하게 보존하고 작업 복사본을 만든 것은 매우 좋은 습관입니다.
2.  **모든 결측치가 있는 행 제거**: `sample_data_copied.dropna(how='all', axis=0)`를 통해 조건에 맞는 행을 제거했습니다. 현재 데이터셋에서는 모든 컬럼이 NaN인 행이 없기 때문에, `row_deleted` DataFrame이 원본과 동일하게 보이는 것이 **정상입니다**. 코드가 틀린 것이 아니라, 데이터가 해당 조건을 만족하지 않는 것입니다.
3.  **모든 결측치가 있는 열 제거**: `row_deleted.dropna(how="all", axis=1)` 또한 정확한 구문입니다. 마찬가지로 현재 데이터셋에는 모든 행이 NaN인 컬럼이 없기 때문에, `col_deleted` DataFrame도 `row_deleted`와 동일하게 보이는 것이 **정상입니다**.

결론적으로, 작성하신 코드는 논리적으로 완벽하며, 주어진 데이터셋의 특성상 시각적인 변화가 없었을 뿐입니다. `dropna()`의 핵심 파라미터들을 정확하게 사용하셨습니다!
"""

# --- [모범 답안] ---
import pandas as pd
import numpy as np

data = {'A': [1, 2, np.nan, 4, 5],
        'B': [np.nan, 6, 7, np.nan, 9],
        'C': ['apple', 'banana', 'cherry', 'date', np.nan],
        'D': [10, 20, 30, 40, 50]}

sample_data = pd.DataFrame(data)

# 1. 모든 컬럼의 값이 결측치인 행 제거
# axis=0 (기본값): 행을 기준으로
# how='all': 모든 값이 NaN일 때만 삭제
sample_data_for_row_op = sample_data.copy() # 원본 보존을 위해 복사
row_deleted_df = sample_data_for_row_op.dropna(how='all', axis=0)

print("\n--- 모든 컬럼이 NaN인 행 제거 후 ---")
print(row_deleted_df)

# 2. 모든 행의 값이 결측치인 열 제거
# 문제 1의 데이터에는 모든 행이 NaN인 열이 없지만, 개념 학습을 위해 수행
sample_data_for_col_op = sample_data.copy() # 원본 보존을 위해 복사
col_deleted_df = sample_data_for_col_op.dropna(how='all', axis=1)

print("\n--- 모든 행이 NaN인 열 제거 후 ---")
print(col_deleted_df)

# 만약 모든 값이 NaN인 열이 실제로 없는 경우 메시지 출력
if sample_data_for_col_op.equals(col_deleted_df):
    print("\n참고: 현재 데이터프레임에는 모든 행이 NaN인 열이 없어 삭제된 열이 없습니다.")


# --- [학습 기록] ---
"""
**학습 질문**: `DataFrame`에서 모든 값이 결측치인 행이나 열을 효과적으로 삭제하는 방법은 무엇일까? 특히 `dropna()` 메서드의 `how`와 `axis` 매개변수를 어떻게 활용해야 할까?

**문제 해결**:
1.  **데이터프레임 복사**: 원본 `sample_data`의 변경을 방지하기 위해 `sample_data.copy()`를 사용하여 새로운 복사본을 생성했다. 이는 데이터 분석 시 매우 중요한 안전 장치임을 다시 확인했다.
2.  **모든 결측치 행 삭제**: `df.dropna(how='all', axis=0)`를 사용하여 모든 컬럼의 값이 `NaN`인 행을 제거했다. `how='all'`은 지정된 축(여기서는 `axis=0`으로 행)에서 **모든 값**이 `NaN`일 때만 해당 요소를 삭제하도록 지시한다.
3.  **모든 결측치 열 삭제**: `df.dropna(how='all', axis=1)`를 사용하여 모든 행의 값이 `NaN`인 열을 제거했다. `axis=1`은 `dropna()`가 열을 기준으로 동작하도록 하며, `how='all'`은 해당 열의 모든 값이 `NaN`일 때만 삭제하도록 한다.
4.  **데이터셋의 특성 파악**: 현재 주어진 `sample_data` 데이터셋에는 모든 값이 `NaN`인 행이나 열이 없었기 때문에, `dropna(how='all')` 연산 후에도 DataFrame의 형태가 변하지 않는다는 점을 직접 확인했다. 이는 코드가 올바르게 동작했음을 의미하며, 데이터의 실제 상태에 따라 결과가 다르게 보일 수 있음을 깨달았다.

**추가 학습**:
* **`dropna()`의 `how` 매개변수**:
    * `how='any'` (기본값): 지정된 축(`axis`)에서 **하나라도** `NaN`이 있으면 해당 행/열을 삭제합니다. (매우 엄격)
    * `how='all'`: 지정된 축(`axis`)에서 **모든 값**이 `NaN`이어야만 해당 행/열을 삭제합니다. (덜 엄격)
* **`dropna()`의 `axis` 매개변수**:
    * `axis=0` 또는 `'index'` (기본값): 행을 기준으로 `NaN`을 검사하고 삭제합니다.
    * `axis=1` 또는 `'columns'`: 열을 기준으로 `NaN`을 검사하고 삭제합니다.
* 데이터셋의 크기나 특성에 따라 `how='any'`와 `how='all'` 중 적절한 것을 선택하는 것이 중요하며, 때로는 불필요한 데이터 손실을 막기 위해 `subset` 매개변수와 함께 사용하는 것이 더 효과적일 수 있음을 인지했습니다.
"""
