# ==============================================================================
# [문제 2. 결측치가 모두 포함된 행/열 제거]
# ==============================================================================

# 관련 주제: 5.2 / 결측치(Missing Values) 처리: 삭제
# 요구사항:
# 다음 `sample_data` 데이터프레임을 생성하세요.
# import pandas as pd
# import numpy as np
# data = {'A': [1, 2, np.nan, 4, 5],
#         'B': [np.nan, 6, 7, np.nan, 9],
#         'C': ['apple', 'banana', 'cherry', 'date', np.nan],
#         'D': [10, 20, 30, 40, 50]}
# sample_data = pd.DataFrame(data)
# 이 데이터프레임에서 다음 작업을 수행하고 각각의 결과를 출력하세요:
# 1. 모든 컬럼의 값이 결측치(NaN)인 행을 제거하고 결과를 출력하세요.
# 2. 모든 행의 값이 결측치(NaN)인 열을 제거하고 결과를 출력하세요.
# 학습 목표: `df.dropna()` 메서드를 사용하여 DataFrame에서 결측치를 포함하는 행 또는 열을 제거하는 방법을 학습합니다. 특히 `how='all'` 매개변수와 `axis` 매개변수의 활용법을 이해합니다.
# 가이드:
# - `df.dropna()`를 사용하세요.
# - `axis` 매개변수는 행(0) 또는 열(1)을 지정합니다.
# - `how='all'`은 해당 축의 모든 값이 NaN일 때만 제거합니다.
# - 각 작업 단계마다 원본 `sample_data`를 **재생성**하거나 `df.copy()`를 사용하여 이전 작업이 다음 작업에 영향을 주지 않도록 하세요.

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
     A    B        C   D
0  1.0  NaN    apple  10
1  2.0  6.0   banana  20
2  NaN  7.0   cherry  30
3  4.0  NaN     date  40
4  5.0  9.0      NaN  50

 --- Column Deleted ---
     A    B        C   D
0  1.0  NaN    apple  10
1  2.0  6.0   banana  20
2  NaN  7.0   cherry  30
3  4.0  NaN     date  40
4  5.0  9.0      NaN  50
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

print("--- 원본 sample_data ---")
print(sample_data)
print(f"\n원본 sample_data의 결측치 개수:\n{sample_data.isnull().sum()}")


# 1. 모든 컬럼의 값이 결측치인 행 제거
# axis=0 (기본값): 행을 기준으로 검사
# how='all': 해당 행의 모든 값이 NaN일 때만 삭제
sample_data_for_row_op = sample_data.copy() # 원본 보존을 위해 복사
row_deleted_df = sample_data_for_row_op.dropna(how='all', axis=0)

print("\n--- 1. 모든 컬럼이 NaN인 행 제거 후 ---")
print(row_deleted_df)
# 데이터셋 특성상 변화가 없으므로 메시지 추가
if sample_data.equals(row_deleted_df):
    print("\n(참고: 현재 데이터프레임에는 모든 컬럼이 NaN인 행이 없어 삭제된 행이 없습니다.)")


# 2. 모든 행의 값이 결측치인 열 제거
# axis=1: 열을 기준으로 검사
# how='all': 해당 열의 모든 값이 NaN일 때만 삭제
sample_data_for_col_op = sample_data.copy() # 원본 보존을 위해 복사
col_deleted_df = sample_data_for_col_op.dropna(how='all', axis=1)

print("\n--- 2. 모든 행이 NaN인 열 제거 후 ---")
print(col_deleted_df)
# 데이터셋 특성상 변화가 없으므로 메시지 추가
if sample_data.equals(col_deleted_df):
    print("\n(참고: 현재 데이터프레임에는 모든 행이 NaN인 열이 없어 삭제된 열이 없습니다.)")

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
* **[공인회계사 업무 관련 추가 학습]**:
    `dropna()` 메서드를 이용한 결측치 제거는 공인회계사(CPA)가 재무 및 회계 데이터를 다룰 때 **데이터의 신뢰성과 분석의 정확성을 확보하는 데 필수적인 전처리 단계**입니다.

    * **데이터 완전성 및 유효성 검증**:
        * **예시**: 회계 시스템에서 추출된 데이터 중 **특정 거래의 핵심 정보(예: 거래 금액, 계정 코드)가 모두 누락된 행**이 있을 수 있습니다. 이러한 행은 분석에 아무런 가치를 제공하지 못하며 오히려 왜곡을 유발할 수 있습니다. `dropna(how='all', axis=0)`를 사용하여 이러한 **의미 없는 완전 결측 행**을 제거하여 데이터셋을 정화합니다.
        * **활용**: CPA는 감사 과정에서 원장 데이터, 전표 데이터, 또는 재고 실사 데이터 등에서 **의미 없는 빈 레코드를 제거**하여 유효한 데이터만을 기반으로 분석을 수행하고, 보고서의 신뢰성을 높일 수 있습니다.

    * **불필요한 컬럼 제거**:
        * **예시**: 특정 회계 데이터베이스에서 추출 시 **모든 레코드에서 값이 없는(즉, 완전히 비어있는) 보조 컬럼**이 생성될 수 있습니다. 이러한 컬럼은 데이터 분석에 불필요하며, 데이터프레임의 크기를 늘려 메모리 효율성을 떨어뜨립니다. `dropna(how='all', axis=1)`를 사용하여 이러한 **완전 결측 컬럼**을 식별하고 제거합니다.
        * **활용**: CPA는 대용량 데이터를 다룰 때 불필요한 컬럼을 제거하여 **데이터 처리 속도를 향상**시키고, 핵심 정보에 집중하여 분석 효율성을 높일 수 있습니다. 이는 특히 빅데이터 환경에서의 재무 분석에서 중요합니다.

    * **데이터 정제 및 준비**:
        * `dropna()`를 활용한 결측치 제거는 데이터 정제 과정의 중요한 부분입니다. CPA는 재무 모델링, 재무 예측, 또는 다양한 감사 분석(예: 비율 분석, 추세 분석)을 수행하기 전에 **결측치 없는 깨끗한 데이터셋을 준비**해야 합니다.
        * 모든 값이 NaN인 행이나 열을 제거함으로써, 향후 분석 시 `NaN` 값으로 인한 계산 오류나 분석 결과의 왜곡을 방지하고, 데이터의 **품질을 보장**할 수 있습니다.

    결론적으로, `dropna(how='all')`은 CPA가 **의미 없는 완전 결측 데이터를 효율적으로 식별하고 제거하여, 재무 데이터의 완전성을 높이고, 분석의 정확성 및 효율성을 극대화하는 데 필수적인 기능**이라고 할 수 있습니다.
"""
