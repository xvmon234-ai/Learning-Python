# solution.py

import pandas as pd
from io import StringIO

# --- [문제 4.5 데이터 재사용 (초기 상태)] ---
employees_data = """EmployeeID,Name,Department,Salary
E001,John,HR,60000
E002,Jane,IT,75000
E003,Mike,IT,65000
E004,Sarah,HR,80000
E005,David,IT,90000
"""

# DataFrame 생성 (Bonus 컬럼 추가는 문제의 지시에 따라 필터링 전에 먼저 수행)
df_employees = pd.read_csv(StringIO(employees_data))
df_employees["Bonus"] = df_employees["Salary"] * 0.1 # 문제 지시에 따라 Bonus 컬럼 추가

# --- [문제 4.6] ---
# 문제 제시: 위 4.5 문제에서 생성한 DataFrame(단, 'Bonus' 컬럼은 삭제되지 않은 초기 상태로)을 사용하여 다음을 수행하세요.
# 1. 'Name' 컬럼에서 이름에 'a' 또는 'A'가 포함된 직원들만 str.contains()를 사용하여 필터링하여 출력해보세요.
# 2. 'Department'가 'HR' 또는 'Finance'인 직원들만 isin() 메서드를 사용하여 필터링하여 출력해보세요.
#
# 목표: str.contains()를 사용한 문자열 포함 필터링과 isin()을 사용한 목록 포함 필터링을 연습합니다.
# 가이드:
# 1. str.contains() 메서드에 case=False 옵션을 사용하여 대소문자를 무시하도록 설정하세요.
# 2. isin() 메서드에 부서 이름 리스트를 전달하여 필터링하세요.

# --- [최초 나의 코딩] ---
# 1. 'Name' 컬럼에서 'a' 또는 'A'가 포함된 직원 필터링 (str.contains() 활용)
# 이 부분은 불리언 Series를 생성하는 것이므로, 필터링을 위해서는 DataFrame에 적용해야 합니다.
# df_name_filtered = df_employees["Name"].str.contains("a", case=False) #False가 대소문자 무시인지, 아닌지 헷갈렸음
# print("\n --- Name Filtered (Boolean Series) --- ")
# print(df_name_filtered)

# 2. 'Department'가 'HR' 또는 'Finance'인 직원 필터링 (isin() 활용)
# df_dept_filtered = df_employees[df_employees["Department"].isin("HR", "Finance")] #TypeError 발생, 이유를 모르겠음
# print("\n --- Department Filtered --- ")
# print(df_dept_filtered)

# ---- 올바른 필터링 적용 (문제의 목표에 맞춰 최종 DataFrame을 출력하도록 수정) ----
# 1. 'Name' 컬럼에서 'a' 또는 'A'가 포함된 직원 필터링 (str.contains() 활용)
filtered_by_name = df_employees[df_employees["Name"].str.contains("a", case=False)]
print("\n--- 이름에 'a' 또는 'A'가 포함된 직원 ---")
print(filtered_by_name)

# 2. 'Department'가 'HR' 또는 'Finance'인 직원 필터링 (isin() 활용)
# isin() 메서드는 인자로 단일 리스트를 받습니다.
filtered_by_dept = df_employees[df_employees["Department"].isin(["HR", "Finance"])]
print("\n--- 'HR' 또는 'Finance' 부서 직원 ---")
print(filtered_by_dept)


# --- [코드 실행 결과] ---
"""
--- 이름에 'a' 또는 'A'가 포함된 직원 ---
  EmployeeID   Name Department  Salary   Bonus
1       E002   Jane         IT   75000  7500.0
3       E004  Sarah         HR   80000  8000.0
4       E005  David         IT   90000  9000.0

--- 'HR' 또는 'Finance' 부서 직원 ---
  EmployeeID  Name Department  Salary   Bonus
0       E001  John         HR   60000  6000.0
3       E004  Sarah         HR   80000  8000.0
"""

# --- [피드백] ---
"""
코드 거의 완벽하게 작성하셨습니다! 두 가지 중요한 학습 포인트를 잘 포착하셨네요.

1.  **DataFrame 생성 및 'Bonus' 컬럼 추가**:
    데이터프레임을 정확하게 생성하고, 문제 지시에 따라 'Bonus' 컬럼을 추가하는 초기 설정을 잘 해주셨습니다.

2.  **`str.contains()` 활용 (거의 완벽!)**:
    `df_employees["Name"].str.contains("a", case=False)`를 사용하여 이름에 'a' 또는 'A'가 포함된 직원을 찾기 위한 불리언 Series를 정확하게 생성했습니다. `case=False`가 대소문자 무시라는 것을 제대로 파악하고 사용했습니다.
    **한 가지 아쉬운 점**: 이 불리언 Series를 바로 출력하는 대신, 이 Series를 **원본 DataFrame의 인덱싱에 적용**하여 실제로 필터링된 DataFrame(`df_employees[...]`)을 출력하는 것이 문제의 목표와 더욱 부합합니다. 이 점을 모범 답안에 반영했습니다.

3.  **`isin()` 활용 (정확한 오류 파악!)**:
    `df_employees["Department"].isin("HR", "Finance")`에서 `TypeError`가 발생한 것은 매우 좋은 발견이자 학습 포인트입니다!
    * **오류 원인**: `isin()` 메서드는 인자로 **단일 리스트(또는 Series, set 등)**를 받아서, 해당 리스트 안에 요소가 포함되어 있는지 여부를 확인합니다. 즉, `'HR'`과 `'Finance'`를 각각 별개의 인자로 전달하는 것이 아니라, `['HR', 'Finance']`와 같이 **하나의 리스트로 묶어 전달**해야 합니다.
    * **해결책**: `df_employees["Department"].isin(["HR", "Finance"])` 와 같이 수정하면 됩니다. 이 오류를 통해 메서드의 인자 타입에 대한 이해를 높일 수 있습니다.

**종합**:
`str.contains()`와 `isin()` 두 메서드의 기본적인 사용법은 정확히 알고 계시며, 특히 `isin()`에서 발생한 `TypeError`의 원인을 스스로 파악하려 한 점은 매우 뛰어난 학습 능력입니다. 약간의 수정으로 완벽한 해결이 가능합니다. 정말 잘하셨습니다!
"""

# --- [모범 답안] ---
"""
import pandas as pd
from io import StringIO

employees_data = """EmployeeID,Name,Department,Salary
E001,John,HR,60000
E002,Jane,IT,75000
E003,Mike,IT,65000
E004,Sarah,HR,80000
E005,David,IT,90000
"""

df_employees = pd.read_csv(StringIO(employees_data))
df_employees["Bonus"] = df_employees["Salary"] * 0.1 # 문제 지시에 따라 Bonus 컬럼 추가

# 1. 'Name' 컬럼에서 이름에 'a' 또는 'A'가 포함된 직원 필터링 (str.contains() 활용)
# case=False: 대소문자를 무시하고 검색
# str.contains() 결과로 반환되는 불리언 Series를 DataFrame에 직접 적용하여 필터링합니다.
filtered_by_name = df_employees[df_employees["Name"].str.contains("a", case=False)]
print("--- 이름에 'a' 또는 'A'가 포함된 직원 ---")
print(filtered_by_name)

# 2. 'Department'가 'HR' 또는 'Finance'인 직원 필터링 (isin() 활용)
# isin() 메서드에는 확인하고자 하는 값들을 반드시 '리스트' 형태로 전달해야 합니다.
filtered_by_dept = df_employees[df_employees["Department"].isin(["HR", "Finance"])]
print("\n--- 'HR' 또는 'Finance' 부서 직원 ---")
print(filtered_by_dept)
"""

# --- [학습 기록] ---
"""
**학습 질문**: 문자열 컬럼에서 특정 문자열 포함 여부를 필터링하는 `str.contains()`와, 여러 값 중 하나에 속하는지 필터링하는 `isin()` 메서드를 어떻게 정확히 사용할까? 특히 `case` 파라미터와 `isin()`의 인자 전달 방식은?

**문제 해결**:
1.  **`str.contains()` 활용**: 'Name' 컬럼에서 이름에 'a' 또는 'A'가 포함된 직원을 찾기 위해 `df_employees["Name"].str.contains("a", case=False)`를 사용했다. `case=False`는 대소문자를 무시하고 검색하도록 설정하는 파라미터임을 확인했다. 초기에는 이 결과로 나온 불리언 Series를 그대로 출력했으나, 문제의 목표인 '필터링된 DataFrame'을 얻기 위해서는 이 불리언 Series를 원본 DataFrame에 `df_employees[...]` 형태로 적용해야 한다는 점을 수정하며 학습했다.
2.  **`isin()` 활용 및 `TypeError` 해결**: 'Department' 컬럼 값이 'HR' 또는 'Finance'인 직원을 찾기 위해 `isin()` 메서드를 사용했으나, `df_employees["Department"].isin("HR", "Finance")`와 같이 여러 인자를 직접 전달하여 `TypeError`가 발생했다. 이 오류를 통해 `isin()` 메서드가 인자로 **단일 리스트(`[]`)**를 받는다는 것을 명확히 이해하게 되었다. `df_employees["Department"].isin(["HR", "Finance"])`와 같이 리스트로 묶어 전달하니 올바르게 필터링되었다.

**추가 학습**:
* **`str.contains()`**: 문자열 Series에 적용되는 메서드로, 정규 표현식도 지원한다. `case` 외에도 `na` (결측값 처리 방법) 등 다양한 파라미터가 있다. 문자열 데이터에 대한 조건부 필터링에 매우 강력하게 사용된다.
* **`isin()`**: Series 내의 각 요소가 주어진 '목록'에 포함되는지 여부를 불리언 Series로 반환하는 메서드이다. `isin()`에 전달되는 목록은 파이썬의 `list`, `set`, `Series` 등 순회 가능한(iterable) 객체여야 한다. `isin()`은 SQL의 `IN` 절과 유사한 기능을 수행한다고 생각할 수 있다.
* **불리언 Series의 활용**: `str.contains()`나 `isin()`의 결과로 생성된 불리언 Series는 그 자체로는 True/False 값들의 집합이지만, 이 Series를 DataFrame의 `[]` 안에 넣으면 `True`에 해당하는 행들만 선택하여 새로운 DataFrame을 반환하는 핵심적인 필터링 메커니즘으로 작동한다. 이는 Pandas 필터링의 기본 중의 기본이므로 확실히 이해해야 한다.
"""

# --- [further_study.py 링크 (선택 사항)] ---
# # 예시: [Further Study: Advanced String Operations with Pandas](further_study.py)
# # 추가 학습이 필요한 경우, 별도의 further_study.py 파일을 생성하고 여기에 링크를 남겨두세요.
