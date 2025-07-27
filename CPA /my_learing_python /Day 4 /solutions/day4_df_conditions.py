# --- [문제 4.5] ---
# 문제 제시:
# 다음 데이터를 사용하여 DataFrame을 생성하세요.
# EmployeeID,Name,Department,Salary
# E001,John,HR,60000
# E002,Jane,IT,75000
# E003,Mike,IT,65000
# E004,Sarah,HR,80000
# E005,David,IT,90000
#
# 1. 'Department'가 'IT'이면서 'Salary'가 70000 이상인 직원들만 필터링하여 출력하세요.
# 2. 새로운 컬럼 'Bonus'를 추가하세요. 보너스는 'Salary'의 10%라고 가정합니다.
# 3. 추가한 'Bonus' 컬럼을 삭제한 후 DataFrame을 출력하세요.
#
# 목표: &를 사용한 다중 조건 필터링, 새로운 컬럼 추가, 그리고 컬럼 삭제 방법을 종합적으로 연습합니다.
# 가이드:
# 1. 각 조건을 소괄호로 묶고 & 연산자로 연결하여 필터링하세요.
# 2. 새로운 컬럼은 df['새컬럼명'] = ... 형태로 할당하세요.
# 3. drop() 메서드를 사용하여 컬럼을 삭제하되, axis와 inplace 파라미터를 올바르게 설정하세요.

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

df_employees = pd.read_csv(StringIO(employees_data))

# 1. 다중 조건 필터링
df_filtered = df_employees[(df_employees["Department"] == "IT") & \
                           (df_employees["Salary"] >= 70000)] # 가독성을 위해 줄 바꿈(\) 사용

print("\n --- Employees in IT with High Salary --- ")
print(df_filtered)

# 2. 새로운 컬럼 'Bonus' 추가
df_employees["Bonus"] = df_employees["Salary"] * 0.1

print("\n --- DataFrame with Bonus --- ")
print(df_employees)

# 3. 'Bonus' 컬럼 삭제
df_employees.drop("Bonus", axis=1, inplace=True) #inplace랑 axis 헷갈림, 추가로 정리할 필요

print("\n --- DataFrame without Bonus --- ")
print(df_employees)


# --- [코드 실행 결과] ---
"""
 --- Employees in IT with High Salary ---
   EmployeeID  Name Department  Salary
1        E002  Jane         IT   75000
4        E005  David         IT   90000

 --- DataFrame with Bonus ---
  EmployeeID   Name Department  Salary   Bonus
0       E001   John         HR   60000  6000.0
1       E002   Jane         IT   75000  7500.0
2       E003   Mike         IT   65000  6500.0
3       E004  Sarah         HR   80000  8000.0
4       E005  David         IT   90000  9000.0

 --- DataFrame without Bonus ---
  EmployeeID   Name Department  Salary
0       E001   John         HR   60000
1       E002   Jane         IT   75000
2       E003   Mike         IT   65000
3       E004  Sarah         HR   80000
4       E005  David         IT   90000
"""

# --- [피드백] ---
"""
코드 아주 훌륭하게 작성하셨습니다! 모든 요구사항을 정확하고 효율적으로 해결하셨네요.

1.  **DataFrame 생성**: 주어진 직원 데이터를 사용하여 DataFrame을 성공적으로 생성했습니다.
2.  **다중 조건 필터링**:
    `df_employees[(df_employees["Department"] == "IT") & (df_employees["Salary"] >= 70000)]` 구문을 사용하여 'Department'가 'IT'이고 'Salary'가 70000 이상인 직원들만 정확히 필터링했습니다. 각 조건을 소괄호로 묶고 '&' 연산자를 사용한 것이 올바른 다중 조건 필터링 방식입니다.
3.  **컬럼 추가**:
    `df_employees["Bonus"] = df_employees["Salary"] * 0.1`를 통해 'Salary'의 10%에 해당하는 'Bonus' 컬럼을 완벽하게 추가했습니다. 새로운 컬럼을 추가하는 표준 방식을 정확히 적용하셨습니다.
4.  **컬럼 삭제**:
    `df_employees.drop("Bonus", axis=1, inplace=True)`를 사용하여 'Bonus' 컬럼을 성공적으로 삭제했습니다. `axis=1`은 '열(컬럼)'을 기준으로 삭제함을 의미하고, `inplace=True`는 원본 DataFrame을 직접 수정함을 의미합니다. 이 두 파라미터의 사용법을 정확히 이해하고 적용하셨습니다. `inplace`와 `axis`에 대한 혼란이 있었다고 하셨는데, 정확하게 사용하셨으니 이미 잘 이해하고 계시다고 볼 수 있습니다!

모든 작업을 완벽하게 수행했습니다. 정말 잘하셨습니다!
"""

# --- [모범 답안] ---
"""
# 아래 코드는 최초 나의 코딩과 동일합니다.
# 이미 완벽하게 문제를 해결하셨기 때문에 별도의 수정이 필요 없습니다.

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

# 1. 'Department'가 'IT'이면서 'Salary'가 70000 이상인 직원 필터링
df_filtered_employees = df_employees[(df_employees["Department"] == "IT") & \
                                     (df_employees["Salary"] >= 70000)]
print("--- 'Department'가 'IT'이고 'Salary'가 70000 이상인 직원 ---")
print(df_filtered_employees)

# 2. 새로운 컬럼 'Bonus' 추가 (Salary의 10%)
df_employees["Bonus"] = df_employees["Salary"] * 0.1
print("\n--- 'Bonus' 컬럼이 추가된 DataFrame ---")
print(df_employees)

# 3. 'Bonus' 컬럼 삭제
# axis=1: 컬럼(열)을 기준으로 삭제
# inplace=True: 원본 DataFrame을 직접 수정 (False일 경우 수정된 새로운 DataFrame 반환)
df_employees.drop("Bonus", axis=1, inplace=True)
print("\n--- 'Bonus' 컬럼이 삭제된 DataFrame ---")
print(df_employees)
"""

# --- [학습 기록] ---
"""
**학습 질문**: 여러 조건을 동시에 적용하여 필터링하고, DataFrame에 새로운 컬럼을 추가 및 삭제하는 방법은 무엇일까? 특히 `drop()` 메서드의 `axis`와 `inplace` 파라미터는 어떻게 동작할까?

**문제 해결**:
1.  **다중 조건 필터링**: `&` 연산자를 사용하여 `'Department'`가 `'IT'`인 조건과 `'Salary'`가 70000 이상인 조건을 연결하여 필터링했다. 이때 각 개별 조건을 **소괄호 `()`로 감싸는 것**이 필수적이라는 점을 다시 한번 확인했다. `df[(조건1) & (조건2)]` 형태는 여러 조건을 조합하는 표준적인 방법이다.
2.  **컬럼 추가**: `df_employees["Bonus"] = df_employees["Salary"] * 0.1`와 같이 새로운 컬럼 이름에 값을 할당하는 방식으로 'Bonus' 컬럼을 성공적으로 추가했다. 이 방식은 기존 컬럼의 연산을 통해 새로운 컬럼을 생성할 때 매우 유용하다.
3.  **컬럼 삭제**: `df_employees.drop("Bonus", axis=1, inplace=True)`를 사용하여 'Bonus' 컬럼을 삭제했다. 이 과정에서 `axis=1`은 '컬럼(열)' 방향으로 작업하라는 의미이며, `inplace=True`는 해당 연산을 수행한 결과가 **원본 DataFrame에 즉시 반영**되도록 하는 파라미터임을 명확히 이해했다. (만약 `inplace=False`였다면, `df_employees.drop("Bonus", axis=1)`는 'Bonus' 컬럼이 삭제된 새로운 DataFrame을 반환하므로, 이를 `df_employees = df_employees.drop("Bonus", axis=1)`와 같이 재할당해야 한다.) `inplace`와 `axis`의 정확한 의미를 파악하는 것이 Pandas 데이터 조작의 핵심임을 재확인했다.

**추가 학습 (공인회계사 업무와의 관련성)**:

Pandas의 **다중 조건 필터링**, **컬럼 추가**, **컬럼 삭제** 기능은 공인회계사(CPA)가 **복잡한 재무 데이터를 정교하게 분석하고, 필요한 정보를 가공하여 보고서를 작성하는 데 필수적인 고급 데이터 조작 능력**입니다.

* **다중 조건 필터링**:
    * **예시**: 특정 회계연도에 발생한 거래 중, **매출액이 특정 금액을 초과하고(`Amount > X`), 특정 유형의 고객(`CustomerType == 'B2B'`)과의 거래이면서(`&`), 아직 미수 상태(`Status == 'Outstanding'`)인 거래**만을 필터링하여 분석합니다.
    * CPA는 이를 통해 내부 통제 시스템의 허점, 잠재적 부실 채권, 또는 고위험 매출 거래 등을 식별하여 감사 절차의 초점을 맞출 수 있습니다. 이는 감사 샘플링이나 특정 리스크 평가 시 매우 유용합니다.

* **새로운 컬럼 추가**:
    * **예시**: 직원 급여 데이터에 **각 직원의 '세후 급여'(`Net_Salary`) 컬럼**을 추가하거나, 매출 데이터에 **'매출 총이익률'(`Gross_Margin_Rate`) 컬럼**을 추가하여 재무 분석의 깊이를 더합니다. `df_employees['Net_Salary'] = df_employees['Salary'] * (1 - Tax_Rate)`와 같이 사용할 수 있습니다.
    * CPA는 이를 통해 원본 데이터에 없는 새로운 재무 지표를 생성하여 재무 성과를 다각도로 평가하고, 경영진에게 보다 유의미한 정보를 제공할 수 있습니다. 이는 재무 모델링 및 성과 분석 보고서 작성의 핵심 단계입니다.

* **컬럼 삭제**:
    * **예시**: 재무 분석에 불필요하거나 **민감한 개인 정보(예: '주민등록번호', '개인 연락처') 컬럼**을 삭제하여 데이터 보안을 강화하거나, 불필요한 데이터를 제거하여 분석 효율성을 높입니다.
    * CPA는 감사 과정에서 수집된 방대한 데이터 중 **내부 감사 보고서나 외부 공시 목적에 맞지 않는 불필요하거나 민감한 정보를 제거**하여 정보 보안 규정을 준수하고, 보고서의 간결성을 유지합니다. 예를 들어, `df_audit_data.drop(['Personal_ID', 'Phone_Number'], axis=1, inplace=True)`와 같이 사용할 수 있습니다.

결론적으로, 다중 조건 필터링, 컬럼 추가 및 삭제는 CPA가 **복잡한 비즈니스 규칙을 데이터에 적용하여 필요한 정보를 정교하게 추출하고, 분석에 필요한 새로운 지표를 생성하며, 보안 및 보고 목적에 맞게 데이터를 정리하는 데 필수적인 실무 능력**입니다.
"""
