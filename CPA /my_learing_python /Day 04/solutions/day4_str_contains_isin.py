# ==============================================================================
# [문제 4.6] str.contains() 및 isin() 활용 필터링 (Day 4 학습 내용)
# ==============================================================================

# 문제 제시: 위 4.5 문제에서 생성한 DataFrame(단, 'Bonus' 컬럼은 삭제되지 않은 초기 상태로)을 사용하여 다음을 수행하세요.
# 1. 'Name' 컬럼에서 이름에 'a' 또는 'A'가 포함된 직원들만 str.contains()를 사용하여 필터링하여 출력해보세요.
# 2. 'Department'가 'HR' 또는 'Finance'인 직원들만 isin() 메서드를 사용하여 필터링하여 출력해보세요.
#
# 목표: str.contains()를 사용한 문자열 포함 필터링과 isin()을 사용한 목록 포함 필터링을 연습합니다.
# 가이드:
# 1. str.contains() 메서드에 case=False 옵션을 사용하여 대소문자를 무시하도록 설정하세요.
# 2. isin() 메서드에 부서 이름 리스트를 전달하여 필터링하세요.

# --- [최초 나의 코딩] ---
import pandas as pd
from io import StringIO

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
    `df_employees["Name"].str.contains("a", case=False)`를 사용하여 이름에 'a' 또는 'A'가 포함된 직원을 찾기 위한 불리언 Series를 정확하게 생성했습니다. **`case=False`가 대소문자 무시**라는 것을 제대로 파악하고 사용했습니다.
    **한 가지 아쉬운 점**: 이 불리언 Series를 바로 출력하는 대신, 이 Series를 **원본 DataFrame의 인덱싱에 적용**하여 실제로 필터링된 DataFrame(`df_employees[...]`)을 출력하는 것이 문제의 목표와 더욱 부합합니다. 이 점을 모범 답안에 반영했습니다.

3.  **`isin()` 활용 (정확한 오류 파악!)**:
    `df_employees["Department"].isin("HR", "Finance")`에서 **`TypeError`가 발생한 것은 매우 좋은 발견이자 학습 포인트**입니다!
    * **오류 원인**: `isin()` 메서드는 인자로 **단일 리스트(또는 Series, set 등)를 받아서**, 해당 리스트 안에 요소가 포함되어 있는지 여부를 확인합니다. 즉, `'HR'`과 `'Finance'`를 각각 별개의 인자로 전달하는 것이 아니라, `['HR', 'Finance']`와 같이 **하나의 리스트로 묶어 전달**해야 합니다.
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
1.  **`str.contains()` 활용**: 'Name' 컬럼에서 이름에 'a' 또는 'A'가 포함된 직원을 찾기 위해 `df_employees["Name"].str.contains("a", case=False)`를 사용했습니다. `case=False`는 대소문자를 무시하고 검색하도록 설정하는 파라미터임을 확인했습니다. 초기에는 이 결과로 나온 불리언 Series를 그대로 출력했으나, 문제의 목표인 '필터링된 DataFrame'을 얻기 위해서는 이 불리언 Series를 원본 DataFrame에 `df_employees[...]` 형태로 적용해야 한다는 점을 수정하며 학습했습니다.
2.  **`isin()` 활용 및 `TypeError` 해결**: 'Department' 컬럼 값이 'HR' 또는 'Finance'인 직원을 찾기 위해 `isin()` 메서드를 사용했으나, `df_employees["Department"].isin("HR", "Finance")`와 같이 여러 인자를 직접 전달하여 `TypeError`가 발생했습니다. 이 오류를 통해 `isin()` 메서드가 인자로 **단일 리스트(`[]`)**를 받는다는 것을 명확히 이해하게 되었습니다. `df_employees["Department"].isin(["HR", "Finance"])`와 같이 리스트로 묶어 전달하니 올바르게 필터링되었습니다.

**추가 학습 (공인회계사 업무와의 관련성)**:

Pandas의 `str.contains()`를 사용한 **문자열 포함 필터링**과 `isin()`을 사용한 **목록 포함 필터링**은 공인회계사(CPA)가 **텍스트 기반의 데이터나 범주형 데이터에서 특정 패턴이나 그룹에 속하는 정보를 효율적으로 식별하고 추출**하는 데 매우 유용합니다.

* **`str.contains()` 활용**:
    * **예시**: **계정과목명, 거래처명, 제품명** 등 텍스트 기반의 데이터에서 **특정 키워드(예: '수수료', '보험', '지점', '수선')가 포함된 거래**를 필터링하여 검토합니다. `df_gl[df_gl['Account_Name'].str.contains('수수료', case=False)]`와 같이 사용하여 특정 비용의 상세 내역을 파악하거나, 관련 계정의 적정성을 검토할 수 있습니다.
    * CPA는 이를 통해 특정 유형의 거래를 식별하여 감사 범위를 좁히거나, 특정 비용의 발생 원인을 분석하는 데 활용합니다. 예를 들어, '광고선전비' 계정 내에서 '온라인' 또는 '디지털'이라는 키워드가 포함된 지출만 따로 분석하는 경우입니다.

* **`isin()` 활용**:
    * **예시**: **특정 부서(예: '영업부', '마케팅부'), 특정 프로젝트 코드(예: 'PJT_A', 'PJT_B'), 또는 특정 지역(예: '서울', '부산')**에 해당하는 데이터만 필터링하여 분석합니다. `df_expenses[df_expenses['Department'].isin(['영업부', '마케팅부'])]`와 같이 사용합니다.
    * CPA는 이를 통해 특정 조직 단위의 성과를 평가하거나, 특정 유형의 거래(예: 관계회사와의 거래)만을 추출하여 독립성 및 공정성 여부를 검토하는 등 **그룹 기반의 분석**을 수행할 수 있습니다. 이는 재무제표 주석 작성이나 특정 감사 절차 수행 시 매우 효율적인 방법입니다.

* **데이터 클리닝 및 유효성 검사**:
    * `str.contains()`를 사용하여 특정 컬럼에 **예상치 못한 문자열 패턴(예: 잘못된 형식의 코드, 특수 문자 포함)**이 있는지 확인하고, `isin()`을 사용하여 특정 컬럼의 값이 **정의된 유효한 목록(예: '승인', '거절', '보류'와 같은 상태값)** 내에 있는지 검증하여 데이터 품질을 향상시킵니다.

결론적으로, `str.contains()`와 `isin()`은 CPA가 **텍스트 및 범주형 데이터를 기반으로 복잡한 필터링을 수행하고, 특정 감사 목적에 맞는 정보를 효율적으로 추출하며, 데이터의 품질을 검증하는 데 필수적인 고급 데이터 조작 기술**입니다.
"""
