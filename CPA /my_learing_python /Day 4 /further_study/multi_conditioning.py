# ==============================================================================
# [문제 4.5] 추가 학습: 다중 조건 및 컬럼 조작의 심화 이해와 CPA 활용
# ==============================================================================

# 데이터 준비 예시
# (이론 설명을 위한 데이터로, 문제 4.5의 데이터와 동일합니다.)
employees_data = """EmployeeID,Name,Department,Salary
E001,John,HR,60000
E002,Jane,IT,75000
E003,Mike,IT,65000
E004,Sarah,HR,80000
E005,David,IT,90000
"""
df_employees = pd.read_csv(StringIO(employees_data))

print("--- 예시 DataFrame (df_employees) ---")
print(df_employees)

# 핵심 이론 1: 다중 조건 필터링 (Multiple Condition Filtering)
"""
다중 조건 필터링은 여러 개의 조건을 동시에 만족하거나(AND), 여러 조건 중 하나라도 만족하는(OR) 데이터를 선택할 때 사용됩니다.

**주요 특징 및 사용법**:

1.  **논리 연산자**:
    * **AND (`&`)**: 모든 조건이 `True`일 때만 해당 행을 선택합니다. (예: `조건1 & 조건2`)
    * **OR (`|`)**: 하나 이상의 조건이 `True`일 때 해당 행을 선택합니다. (예: `조건1 | 조건2`)
    * **NOT (`~`)**: 조건의 결과를 반전시킵니다. (예: `~조건1`)

2.  **소괄호 사용**:
    * 각 개별 조건식은 반드시 소괄호 `()`로 묶어야 합니다. 이는 연산자 우선순위 때문에 중요합니다. Pandas의 비트wise 논리 연산자 `&`, `|`는 비교 연산자(`==`, `>=`, 등)보다 우선순위가 높기 때문에, 소괄호로 묶지 않으면 예상치 못한 오류가 발생할 수 있습니다.
    * 올바른 예: `df[(df['컬럼'] == 값) & (df['컬럼'] > 숫자)]`
    * 잘못된 예: `df[df['컬럼'] == 값 & df['컬럼'] > 숫자]` (이 경우 `값 & df['컬럼']`이 먼저 연산되어 오류 발생)

**왜 중요한가?**:
실제 비즈니스 데이터는 단일 조건으로만 필터링하기 어려운 경우가 많습니다. 다중 조건 필터링은 복잡한 비즈니스 규칙이나 감사 기준을 데이터에 적용하여 매우 정교하게 필요한 데이터를 추출할 수 있게 해줍니다.
"""

# 다중 조건 필터링 예시
# 'Department'가 'IT'이면서 'Salary'가 70000 이상인 직원
filtered_and = df_employees[(df_employees["Department"] == "IT") & \
                            (df_employees["Salary"] >= 70000)]
print("\n--- 'IT' 부서이면서 급여 7만 이상인 직원 (AND 조건) ---")
print(filtered_and)

# 'Department'가 'IT'이거나 'Salary'가 80000 이상인 직원 (OR 연산자 | 추가 학습)
filtered_or = df_employees[(df_employees["Department"] == "IT") | \
                           (df_employees["Salary"] >= 80000)]
print("\n--- 'IT' 부서이거나 급여 8만 이상인 직원 (OR 조건) ---")
print(filtered_or)


# 핵심 이론 2: 새로운 컬럼 추가 (Adding New Columns)
"""
DataFrame에 새로운 컬럼을 추가하는 것은 기존 데이터를 기반으로 새로운 정보를 파생시키거나, 분석에 필요한 추가 속성을 부여할 때 사용됩니다.

**주요 특징 및 사용법**:

1.  **단순 할당**:
    * `df['새_컬럼명'] = 값_또는_Series`
    * 가장 일반적인 방법으로, 단일 값, 리스트, NumPy 배열, 또는 기존 컬럼의 연산 결과 Series를 할당할 수 있습니다.
    * 예: `df['Bonus'] = df['Salary'] * 0.1`

2.  **조건부 할당 (`.apply()` 또는 `np.where()`)**:
    * 특정 조건에 따라 다른 값을 할당해야 할 때 사용합니다.
    * `df.apply(lambda row: ... , axis=1)`: 행(row) 단위로 복잡한 로직을 적용할 때 유용합니다. `axis=1`은 행 방향으로 함수를 적용하라는 의미입니다.
    * `np.where(조건, True일때_값, False일때_값)`: NumPy의 `where` 함수를 사용하여 조건부 할당을 효율적으로 수행할 수 있습니다.

**왜 중요한가?**:
새로운 컬럼 추가는 원본 데이터에 없는 중요한 비즈니스 지표(예: 이익률, 세후 금액, 성과 점수)를 생성하여 분석의 깊이를 더하고, 보고서의 내용을 풍부하게 만듭니다.
"""

# 새로운 컬럼 추가 예시
df_employees_copy_for_add = df_employees.copy() # 원본 손상 방지를 위해 복사
df_employees_copy_for_add["Bonus"] = df_employees_copy_for_add["Salary"] * 0.1
print("\n--- 'Bonus' 컬럼 추가 (Salary의 10%) ---")
print(df_employees_copy_for_add)

# 새로운 컬럼 추가 (조건에 따른 값 할당 - Performance_Bonus)
df_employees_copy_for_conditional_add = df_employees.copy()
df_employees_copy_for_conditional_add["Performance_Bonus"] = df_employees_copy_for_conditional_add.apply(
    lambda row: row['Salary'] * 0.15 if row['Salary'] >= 75000 else row['Salary'] * 0.05, axis=1
)
print("\n--- 'Performance_Bonus' 컬럼 추가 (조건부: 급여 7.5만 이상 15%, 미만 5%) ---")
print(df_employees_copy_for_conditional_add)


# 핵심 이론 3: 컬럼 삭제 (Deleting Columns)
"""
DataFrame에서 불필요한 컬럼을 삭제하는 것은 데이터의 크기를 줄이고, 분석 효율성을 높이며, 민감한 정보를 제거하여 데이터 보안을 강화할 때 사용됩니다.

**주요 특징 및 사용법**:

1.  **`df.drop()` 메서드**:
    * `df.drop(컬럼명_또는_리스트, axis=1, inplace=False)`
    * `컬럼명_또는_리스트`: 삭제할 컬럼의 이름(단일) 또는 이름들의 리스트(여러 개).
    * `axis=1`: 컬럼(열)을 삭제할 때는 반드시 `axis=1`로 지정해야 합니다. `axis=0`은 행을 삭제할 때 사용됩니다.
    * `inplace=True` / `inplace=False`:
        * `inplace=True`: 원본 DataFrame을 직접 수정하고, 메서드는 아무것도 반환하지 않습니다. (주의해서 사용해야 합니다.)
        * `inplace=False` (기본값): 원본 DataFrame은 그대로 두고, 컬럼이 삭제된 **새로운 DataFrame을 반환**합니다. 실무에서는 원본 데이터의 보존을 위해 이 방식을 선호하고, 반환된 DataFrame을 새로운 변수에 할당하거나 원본 변수에 재할당합니다.

**왜 중요한가?**:
데이터 클리닝, 메모리 최적화, 그리고 특정 분석 목적에 맞게 데이터셋을 간결하게 유지하는 데 필수적인 작업입니다. 특히 개인 식별 정보(PII)와 같은 민감한 데이터를 처리할 때 보안 목적으로 사용됩니다.
"""

# 컬럼 삭제 예시
df_employees_copy_for_drop = df_employees_copy_for_add.copy() # Bonus 컬럼이 있는 복사본 사용
print("\n--- 삭제 전 DataFrame (Bonus 컬럼 포함) ---")
print(df_employees_copy_for_drop)

# 'Bonus' 컬럼 삭제 (inplace=True 사용)
df_employees_copy_for_drop.drop("Bonus", axis=1, inplace=True)
print("\n--- 'Bonus' 컬럼 삭제 후 (inplace=True로 원본 직접 수정) ---")
print(df_employees_copy_for_drop)

# 'Performance_Bonus' 컬럼 삭제 (inplace=False 사용 예시)
# (이전 단계에서 추가된 Performance_Bonus 컬럼이 있는 df_employees_copy_for_conditional_add 사용)
df_after_drop_false = df_employees_copy_for_conditional_add.drop("Performance_Bonus", axis=1, inplace=False)
print("\n--- 'Performance_Bonus' 삭제 후 (inplace=False로 새로운 DataFrame 반환) ---")
print(df_after_drop_false)
print("\n--- 원본 (df_employees_copy_for_conditional_add)은 그대로 유지됨 ---")
print(df_employees_copy_for_conditional_add) # 원본이 그대로 유지됨을 확인


print("\n[공인회계사(CPA) 업무와의 관련성]:")
"""
Pandas의 **다중 조건 필터링**, **컬럼 추가**, **컬럼 삭제** 기능은 공인회계사(CPA)가
**복잡한 재무 데이터를 정교하게 분석하고, 필요한 정보를 가공하여 보고서를 작성하는 데 필수적인 고급 데이터 조작 능력**입니다.

* **다중 조건 필터링**:
    * **활용**: 특정 회계연도에 발생한 거래 중, **매출액이 특정 금액을 초과하고(`Amount > X`), 특정 유형의 고객(`CustomerType == 'B2B'`)과의 거래이면서(`&`), 아직 미수 상태(`Status == 'Outstanding'`)인 거래**만을 필터링하여 분석합니다.
    * **의미**: CPA는 이를 통해 내부 통제 시스템의 허점, 잠재적 부실 채권, 또는 고위험 매출 거래 등을 식별하여 감사 절차의 초점을 맞출 수 있습니다. 이는 감사 샘플링이나 특정 리스크 평가 시 매우 유용합니다.

* **새로운 컬럼 추가**:
    * **활용**: 직원 급여 데이터에 **각 직원의 '세후 급여'(`Net_Salary`) 컬럼**을 추가하거나, 매출 데이터에 **'매출 총이익률'(`Gross_Margin_Rate`) 컬럼**을 추가하여 재무 분석의 깊이를 더합니다. `df_employees['Net_Salary'] = df_employees['Salary'] * (1 - Tax_Rate)`와 같이 사용할 수 있습니다.
    * **의미**: CPA는 이를 통해 원본 데이터에 없는 새로운 재무 지표를 생성하여 재무 성과를 다각도로 평가하고, 경영진에게 보다 유의미한 정보를 제공할 수 있습니다. 이는 재무 모델링 및 성과 분석 보고서 작성의 핵심 단계입니다.

* **컬럼 삭제**:
    * **활용**: 재무 분석에 불필요하거나 **민감한 개인 정보(예: '주민등록번호', '개인 연락처') 컬럼**을 삭제하여 데이터 보안을 강화하거나, 불필요한 데이터를 제거하여 분석 효율성을 높입니다.
    * **의미**: CPA는 감사 과정에서 수집된 방대한 데이터 중 **내부 감사 보고서나 외부 공시 목적에 맞지 않는 불필요하거나 민감한 정보를 제거**하여 정보 보안 규정을 준수하고, 보고서의 간결성을 유지합니다. 예를 들어, `df_audit_data.drop(['Personal_ID', 'Phone_Number'], axis=1, inplace=True)`와 같이 사용할 수 있습니다.

결론적으로, 다중 조건 필터링, 컬럼 추가 및 삭제는 CPA가 **복잡한 비즈니스 규칙을 데이터에 적용하여 필요한 정보를 정교하게 추출하고, 분석에 필요한 새로운 지표를 생성하며, 보안 및 보고 목적에 맞게 데이터를 정리하는 데 필수적인 실무 능력**입니다.
"""
