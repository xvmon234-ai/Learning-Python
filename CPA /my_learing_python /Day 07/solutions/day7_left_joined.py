# ==============================================================================
# [문제 1-2] 직원 정보와 부서 정보 `left` 조인 (누락 데이터 처리) (Day 7 학습 내용)
# ==============================================================================

# --- [최초 나의 코딩] ---
import pandas as pd

data_employees = {'EmployeeID': [101, 102, 103, 104, 105],
                  'Name': ['John', 'Jane', 'Mike', 'Sarah', 'Paul'],
                  'DepartmentID': [1, 2, 99, 1, 3]} # DepartmentID 99는 departments_df에 없음
employees_df = pd.DataFrame(data_employees)

data_departments = {'DeptID': [1, 2, 3],
                    'DepartmentName': ['HR', 'IT', 'Marketing'],
                    'Location': ['Seoul', 'Busan', 'Jeju']}
departments_df = pd.DataFrame(data_departments)

df_joined = pd.merge(employees_df, departments_df, left_on="DepartmentID", right_on="DeptID", how="left")

print("\n --- Left Joined Dataframe --- \n")
print(df_joined)

# --- [코드 실행 결과] ---
"""
 --- Left Joined Dataframe ---
   EmployeeID   Name  DepartmentID  DeptID DepartmentName Location
0         101   John             1     1.0           HR    Seoul
1         102   Jane             2     2.0           IT    Busan
2         103   Mike            99     NaN          NaN      NaN
3         104  Sarah             1     1.0           HR    Seoul
4         105   Paul             3     3.0    Marketing     Jeju
"""

# --- [피드백] ---
"""
문제 1-2를 **아주 정확하게 해결**하셨습니다! `pd.merge()` 함수와 `left` 조인 방식을 사용하여 직원 정보의 완전성을 유지하면서 부서 정보를 성공적으로 연결했습니다. 특히, 서로 다른 키(컬럼) 이름을 가진 DataFrame을 올바르게 조인하고, 조인 키가 일치하지 않는 경우 `NaN`이 발생하는 `left` 조인의 특성을 잘 이해하고 있음을 보여줍니다.

1.  **올바른 조인 방식 선택**: `how="left"`를 사용하여 `employees_df` (왼쪽 DataFrame)의 모든 레코드를 최종 결과에 포함시킨 것은 문제의 요구사항을 정확히 충족시킵니다.
2.  **상이한 키 이름 처리**: `left_on="DepartmentID"`와 `right_on="DeptID"`를 통해 양쪽 DataFrame의 조인 키 컬럼 이름이 다를 때도 문제없이 병합을 수행할 수 있음을 입증했습니다. 이는 실제 데이터에서 흔히 발생하는 시나리오에 대한 이해를 보여줍니다.
3.  **`NaN` 값의 의미 이해**: `DepartmentID`가 99인 'Mike' 직원의 경우, `departments_df`에 매칭되는 `DeptID`가 없으므로 해당 직원의 부서 관련 정보(`DeptID`, `DepartmentName`, `Location`)가 `NaN`으로 채워진 것을 확인할 수 있습니다. 이는 `left` 조인의 핵심적인 동작 특성이며, 데이터에 누락된 정보가 있음을 시각적으로 명확하게 보여줍니다.

이 풀이는 실제 비즈니스 데이터에서 기준 마스터 데이터를 기반으로 다른 데이터를 연결하고, 이 과정에서 발생할 수 있는 데이터 불일치나 누락을 식별하는 데 매우 유용한 접근 방식입니다. `left` 조인은 CPA가 데이터의 완전성 감사나 누락된 정보 식별 시 중요한 도구입니다.
"""

# --- [모범 답안] ---
# 이미 '최초 나의 코딩'에서 모범적으로 해결되었으므로, 추가적인 모범 답안은 생략합니다.
# 다만, 결과를 변수에 할당하고 출력 메시지를 명확히 하는 것이 좋은 습관입니다.

# combined_employee_info_df = pd.merge(employees_df, departments_df, left_on="DepartmentID", right_on="DeptID", how="left")
# print("\n--- 직원 및 부서 정보 통합 (Left Join) 결과 ---")
# print(combined_employee_info_df)


# --- [학습 기록] ---
"""
**학습 질문**: 모든 직원의 정보를 유지하면서, 각 직원의 부서 정보를 연결하고 싶을 때 어떤 조인 방식을 사용해야 할까? 그리고 조인 키가 서로 다를 때 어떻게 처리해야 할까?

**문제 해결**:
1.  **데이터프레임 준비**: 직원 정보 `employees_df`와 부서 정보 `departments_df`를 각각 생성했습니다. `employees_df`에는 'DepartmentID'가, `departments_df`에는 'DeptID'가 부서를 식별하는 키로 사용되었습니다.
2.  **`pd.merge()` 함수와 `left` 조인 사용**:
    * `pd.merge(employees_df, departments_df, ...)`: `employees_df`를 '왼쪽' DataFrame으로, `departments_df`를 '오른쪽' DataFrame으로 지정했습니다.
    * `left_on="DepartmentID", right_on="DeptID"`: 양쪽 DataFrame의 조인 키 컬럼 이름이 다르므로, `left_on`과 `right_on` 매개변수를 사용하여 각 DataFrame의 조인 기준이 되는 컬럼을 명확히 지정했습니다.
    * `how="left"`: `left` 조인 방식을 명시했습니다. 이는 왼쪽 DataFrame(`employees_df`)에 있는 모든 레코드를 결과에 포함하고, 오른쪽 DataFrame(`departments_df`)에서 일치하는 `DeptID`가 없을 경우 해당 열들을 `NaN` (결측치)으로 채우도록 지시합니다.
3.  **결과 확인**: 병합된 `df_joined` DataFrame을 출력한 결과, `EmployeeID` 103번 'Mike'의 `DepartmentID` 99는 `departments_df`에 존재하지 않으므로, 'DeptID', 'DepartmentName', 'Location' 컬럼에 `NaN`이 채워진 것을 확인했습니다. 다른 직원들은 부서 정보가 정상적으로 연결되었습니다.

**추가 학습 (공인회계사 업무와의 관련성 및 `left` 조인의 활용)**:

`left` 조인은 공인회계사 업무에서 **특정 기준 데이터 집합의 완전성을 보장하면서 추가적인 속성이나 상태 정보를 연결**할 때 매우 유용합니다. 이는 **누락되거나 불일치하는 데이터를 식별**하고, **분석의 기준점을 명확히 설정**하는 데 핵심적인 역할을 합니다.

* **기준 대상의 완전성 유지 및 속성 확장**:
    * **예시**: 회계감사 시, 기업이 제시한 **'모든 유형자산 목록'(`asset_register_df`)**을 기준으로, 각 자산에 대한 **'물리적 실사 결과'(`physical_count_df`)**를 `left` 조인합니다.
        * `left` 조인을 사용하면 `asset_register_df`의 모든 자산이 결과에 포함되며, 실사에서 확인되지 않은 자산은 `physical_count_df`의 정보가 `NaN`으로 표시됩니다.
        * CPA는 `NaN`이 있는 자산들을 대상으로 추가 조사(예: 실물 자산 존재 여부 재확인, 폐기/매각 기록 확인 등)를 수행하여 자산의 완전성과 존재성을 검증합니다.

* **미회수 채권 및 미지급 부채 식별**:
    * **예시**: **'모든 매출채권 내역'(`ar_ledger_df`)**을 기준으로 **'실제 수금 내역'(`cash_receipts_df`)**을 `left` 조인합니다.
        * 결과 DataFrame에서 수금 내역이 `NaN`으로 나타나는 매출채권은 아직 회수되지 않은 채권으로 분류됩니다.
        * CPA는 이를 통해 **매출채권의 회수 가능성을 평가**하고, 장기 미수금에 대한 충당금 설정의 적정성을 검토합니다.
    * **예시**: **'모든 매입 채무 내역'(`ap_ledger_df`)**을 기준으로 **'실제 지급 내역'(`cash_payments_df`)**을 `left` 조인하여, 아직 지급되지 않은 매입 채무를 식별하고 부채의 완전성을 검증합니다.

* **인사 데이터 관리 및 이상 감지**:
    * **예시**: **'모든 재직 직원 목록'(`employee_master_df`)**을 기준으로 **'월별 급여 지급 기록'(`payroll_records_df`)**을 `left` 조인합니다.
        * 급여 지급 기록이 `NaN`으로 나타나는 직원은 급여가 누락되었거나, 휴직 등으로 지급 대상이 아닌 경우일 수 있습니다.
        * 감사인은 이를 통해 **급여 지급의 정확성과 완전성**을 확인하고, 퇴사한 직원에게 급여가 계속 지급되는 '유령 직원'과 같은 이상 징후를 탐지하는 데 활용할 수 있습니다.

`left` 조인은 CPA가 **특정 데이터 집합(예: 모든 자산, 모든 거래, 모든 직원)을 '중심'에 두고 관련 정보들을 연결하여 전체적인 맥락을 파악하고, 이 과정에서 발생할 수 있는 누락, 불일치, 또는 예외 사항을 식별**하는 데 필수적인 도구입니다. 이는 감사 절차의 효율성을 높이고, 재무 정보의 신뢰성을 확보하는 데 직접적으로 기여합니다.
"""
