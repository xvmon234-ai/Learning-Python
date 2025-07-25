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

df_filtered = df_employees[(df_employees["Department"] == "IT") & \
                           (df_employees["Salary"] >= 70000)] # 가독성을 위해 줄 바꿈(\) 사용

print("\n --- Employees in IT with High Salary --- ")
print(df_filtered)

# 새로운 컬럼 'Bonus' 추가
df_employees["Bonus"] = df_employees["Salary"] * 0.1

print("\n --- DataFrame with Bonus --- ")
print(df_employees)

# 'Bonus' 컬럼 삭제
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

**추가 학습**:
Pandas에서 `drop()` 메서드는 행(기본값) 또는 열을 삭제할 때 사용된다.
* **`axis`**: 축을 지정하는 파라미터. `axis=0` 또는 `axis='index'`는 행을 의미하고, `axis=1` 또는 `axis='columns'`는 열(컬럼)을 의미한다. 컬럼 삭제 시에는 반드시 `axis=1`을 지정해야 한다.
* **`inplace`**: 연산 결과를 원본 DataFrame에 바로 적용할지 여부를 결정하는 불리언 파라미터.
    * `inplace=True`: 원본 DataFrame을 직접 변경하고 `None`을 반환한다. (재할당 불필요)
    * `inplace=False` (기본값): 원본 DataFrame은 그대로 두고, 변경된 내용이 반영된 **새로운 DataFrame을 반환**한다. (재할당 필요)
`inplace=True` 사용 시에는 원본 데이터가 변경되므로 주의 깊게 사용해야 한다. 보통은 `inplace=False`를 유지하고 새로운 변수에 할당하거나, `df = df.drop(...)` 형태로 재할당하는 것이 권장된다.
"""

# --- [further_study.py 링크 (선택 사항)] ---
# # 예시: [Further Study: Understanding axis and inplace in Pandas](further_study.py)
# # 추가 학습이 필요한 경우, 별도의 further_study.py 파일을 생성하고 여기에 링크를 남겨두세요.
