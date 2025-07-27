# ==============================================================================
# [추가 학습: Pandas의 중복값 처리 (duplicated()와 drop_duplicates() 심화)]
# ==============================================================================

# **개요**:
# 데이터 분석에서 중복값은 데이터의 신뢰성을 떨어뜨리고 분석 결과에 왜곡을 초래할 수 있으므로, 적절하게 식별하고 처리하는 것이 매우 중요합니다. Pandas는 `duplicated()`와 `drop_duplicates()` 메서드를 통해 중복값을 효과적으로 관리할 수 있는 강력한 기능을 제공합니다. 이 두 메서드는 특히 `keep`과 `subset` 매개변수를 통해 다양한 시나리오에 대응할 수 있습니다.

# **1. `df.duplicated()`: 중복 여부 확인**

# * **기능**: DataFrame 또는 Series의 각 행/값(value)이 이전에 나타났는지 여부를 불리언(True/False) Series로 반환합니다.
# * **주요 매개변수**:
#     * `subset`: 중복을 검사할 **컬럼(들)을 지정**합니다. 기본값은 `None`으로, 이 경우 모든 컬럼을 기준으로 중복을 확인합니다. 리스트 형태로 여러 컬럼 이름을 전달할 수 있습니다 (`subset=['col1', 'col2']`). 지정된 모든 컬럼의 값이 동일할 때 중복으로 간주합니다.
#     * `keep`: 어떤 중복을 `True`로 표시할지 결정합니다.
#         * `'first'` (기본값): **첫 번째로 등장하는 값은 고유한 것으로 간주하고**, 이후에 등장하는 모든 중복값에 대해 `True`를 반환합니다. 가장 일반적인 시나리오입니다.
#         * `'last'`: **마지막으로 등장하는 값은 고유한 것으로 간주하고**, 그 이전에 등장하는 모든 중복값에 대해 `True`를 반환합니다.
#         * `False`: **모든 중복되는 값(첫 등장하는 값 포함)에 대해 `True`를 반환**합니다. 이는 중복된 모든 인스턴스를 찾고 싶을 때 유용합니다.

# **2. `df.drop_duplicates()`: 중복값 제거**

# * **기능**: DataFrame 또는 Series에서 중복되는 행/값을 제거한 새로운 DataFrame/Series를 반환합니다. 원본 데이터를 변경하지 않습니다 (기본 `inplace=False`).
# * **주요 매개변수**:
#     * `subset`: `duplicated()`와 동일하게 중복을 검사할 **컬럼(들)을 지정**합니다.
#     * `keep`: 중복되는 값들 중에서 어떤 것을 **유지할지** 결정합니다.
#         * `'first'` (기본값): 중복되는 값들 중 **첫 번째로 등장하는 값을 유지**하고 나머지를 제거합니다.
#         * `'last'`: 중복되는 값들 중 **마지막으로 등장하는 값을 유지**하고 나머지를 제거합니다.
#         * `False`: 중복되는 값들을 **모두 제거**하여, 해당 값의 모든 인스턴스가 삭제됩니다. (즉, 중복되지 않는 유일한 값만 남습니다.)
#     * `inplace`: `True`로 설정하면 원본 DataFrame을 직접 수정하고 `None`을 반환합니다. 기본값은 `False`입니다. (주의해서 사용해야 합니다!)

# **중복값 처리 시 고려사항**:

# * **중복의 정의**: '중복'이란 무엇인가를 명확히 정의해야 합니다. 모든 컬럼이 일치해야 중복인가요? 아니면 특정 ID 컬럼만 일치하면 중복으로 볼 것인가요? `subset` 매개변수가 이 정의를 내려줍니다.
# * **어떤 중복을 유지할 것인가?**: 중복이 발견되었을 때, 어떤 중복을 '진짜' 데이터로 간주하고 유지할 것인지 (`first`, `last`) 또는 모두 삭제할 것인지 (`False`) 결정해야 합니다. 이는 데이터의 특성과 분석 목적에 따라 달라집니다. 예를 들어, 최신 정보가 중요한 경우 `keep='last'`를 사용할 수 있습니다.
# * **원본 데이터 보존**: `drop_duplicates()`는 기본적으로 원본을 변경하지 않는 새로운 DataFrame을 반환하므로 안전합니다. 만약 원본을 직접 변경해야 한다면 `inplace=True`를 사용하지만, 실수 방지를 위해 복사본(`df.copy()`)으로 작업하거나 재할당(`df = df.drop_duplicates(...)`)하는 것을 권장합니다.

# 중복값 처리는 데이터 전처리의 핵심 단계이며, 이 메서드들을 능숙하게 사용하는 것은 깨끗하고 신뢰할 수 있는 데이터를 확보하는 데 중요합니다.

# --- 실습 예시: duplicated()와 drop_duplicates() 심화 ---
import pandas as pd

# 예시 데이터 생성
data = {'ID': [1, 2, 1, 3, 2, 4],
        'Value': ['A', 'B', 'A', 'C', 'X', 'D'], # ID는 중복되지만 Value는 다를 수 있음
        'Timestamp': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-03', '2023-01-02', '2023-01-04']}
df_dup_study = pd.DataFrame(data)

print("--- 원본 DataFrame ---")
print(df_dup_study)

# 1. 전체 행 기준 중복 확인
# (1, 'A', '2023-01-01')이 0번과 2번에 중복.
# (2, 'B', '2023-01-02')가 1번과 (2, 'X', '2023-01-02')는 다름.
# (2, 'B', '2023-01-02')가 1번에 있고, 4번은 (2, 'X', '2023-01-02')이므로 전체 중복 아님.

print("\n--- df.duplicated(keep='first') (기본값) ---")
# 첫 번째 등장하는 중복은 False, 이후 중복만 True
# Index 0: False (첫 등장)
# Index 1: False (첫 등장)
# Index 2: True (Index 0과 중복)
# Index 3: False (첫 등장)
# Index 4: False (Index 1과 ID만 같고 Value, Timestamp가 다름)
# Index 5: False (첫 등장)
print(df_dup_study.duplicated(keep='first')) # [False, False, True, False, False, False]

print("\n--- df.duplicated(keep='last') ---")
# 마지막 등장하는 중복은 False, 이전 중복만 True
# Index 0: True (Index 2가 마지막 중복)
# Index 1: False
# Index 2: False (마지막 중복)
# Index 3: False
# Index 4: False
# Index 5: False
print(df_dup_study.duplicated(keep='last')) # [True, False, False, False, False, False]

print("\n--- df.duplicated(keep=False) (모든 중복 인스턴스 True) ---")
# Index 0: True
# Index 1: False
# Index 2: True
# Index 3: False
# Index 4: False
# Index 5: False
print(df_dup_study.duplicated(keep=False)) # [True, False, True, False, False, False]


# 2. 'ID' 컬럼 기준 중복 확인 (subset 활용)
print("\n--- df.duplicated(subset='ID', keep='first') ---")
# ID가 1인 경우 (0, 2), ID가 2인 경우 (1, 4)
# Index 0: False
# Index 1: False
# Index 2: True (ID 1 중복)
# Index 3: False
# Index 4: True (ID 2 중복)
# Index 5: False
print(df_dup_study.duplicated(subset='ID', keep='first')) # [False, False, True, False, True, False]

print("\n--- df.drop_duplicates(subset='ID', keep='first') ---")
# ID가 중복될 경우 첫 번째 등장하는 행 유지
print(df_dup_study.drop_duplicates(subset='ID', keep='first'))


print("\n--- df.drop_duplicates(subset='ID', keep='last') ---")
# ID가 중복될 경우 마지막 등장하는 행 유지
print(df_dup_study.drop_duplicates(subset='ID', keep='last'))


print("\n--- df.drop_duplicates(subset='ID', keep=False) ---")
# ID가 중복되는 모든 행 제거 (ID 1과 2를 가진 행은 모두 사라짐)
print(df_dup_study.drop_duplicates(subset='ID', keep=False))
