# ==============================================================================
# [문제 6.3.1] Pandas 그룹 필터링 (Day 6 학습 내용)
# ==============================================================================

# --- [최초 나의 코딩] ---
import pandas as pd
data = {'Department': ['HR', 'IT', 'HR', 'IT', 'Marketing', 'HR', 'IT'],
        'Position': ['Manager', 'Developer', 'Staff', 'Developer', 'Manager', 'Staff', 'Manager'],
        'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
        'Salary': [90000, 75000, 62000, 80000, 100000, 65000, 95000]}
employees_df_v2 = pd.DataFrame(data)

group_data = employees_df_v2.groupby("Department").filter(lambda x : x["Salary"].mean() >= 70000)
# lambda를 lamda로 적어서 오류

print("\n--- Departments with Avg Salary >= 70000 ---")
print(group_data)

# --- [코드 실행 결과] ---
"""
--- Departments with Avg Salary >= 70000 ---
  Department   Position Employee  Salary
1         IT  Developer      Bob   75000
3         IT  Developer    David   80000
4  Marketing    Manager      Eve  100000
6         IT    Manager    Grace   95000
"""

# --- [피드백] ---
"""
문제 6.3.1을 **완벽하게 해결**하셨습니다! `groupby()`와 `filter()` 메서드를 사용하여 특정 조건에 맞는 그룹만을 정확히 추출했습니다.

1.  **정확한 그룹화**: `employees_df_v2.groupby("Department")`를 통해 부서별로 데이터를 올바르게 그룹화했습니다.
2.  **`filter()`를 사용한 조건부 그룹 선택**: `filter(lambda x : x["Salary"].mean() >= 70000)` 구문은 `filter()` 메서드의 강력한 활용법을 보여줍니다.
    * `filter()`는 각 그룹(`x`)에 대해 조건을 평가하여, 조건이 True인 그룹의 모든 원본 행을 반환합니다.
    * `lambda x : x["Salary"].mean() >= 70000`는 각 부서 그룹(`x`)의 'Salary' 평균이 70000 이상인지 확인하는 조건입니다. 이 조건에 맞는 'IT'와 'Marketing' 부서의 모든 행이 반환됩니다.
3.  **오류 수정**: `lambda`를 `lamda`로 오타를 내셨던 부분을 정확히 수정하여 문제를 해결하신 점은 매우 좋습니다. 이는 프로그래밍 시 발생할 수 있는 흔한 오타에 대한 디버깅 능력을 보여줍니다.

이 풀이는 Pandas `groupby()`와 `filter()`를 이용한 조건부 그룹 선택의 모범적인 예시이며, 특정 기준에 따라 데이터를 선별하는 데 매우 유용합니다.
"""

# --- [모범 답안] ---
# 이미 '최초 나의 코딩'에서 모범적으로 해결되었으므로, 추가적인 모범 답안은 생략합니다.
# 다만, 결과를 변수에 할당하는 것은 좋은 습관입니다.
# filtered_departments = employees_df_v2.groupby("Department").filter(lambda x: x["Salary"].mean() >= 70000)
# print("\n--- Departments with Avg Salary >= 70000 (모범 답안 예시) ---")
# print(filtered_departments)

# --- [학습 기록] ---
"""
**학습 질문**: 특정 컬럼(예: 'Department')을 기준으로 그룹화한 후, 그룹 자체의 특정 통계량(예: 평균 급여)이 특정 조건을 만족하는 그룹의 모든 원본 행을 추출하려면 어떻게 해야 할까?

**문제 해결**:
1.  **데이터프레임 준비**: 문제에서 주어진 직원 데이터를 포함하는 `employees_df_v2`를 생성했습니다.
2.  **`groupby()`로 그룹화**: `employees_df_v2.groupby("Department")`를 사용하여 데이터를 `'Department'` 컬럼을 기준으로 그룹화했습니다.
3.  **`filter()` 메서드를 이용한 조건부 필터링**: 그룹화된 객체에 `.filter()` 메서드를 적용하여 특정 조건을 만족하는 그룹만 남겼습니다.
    * `filter()`는 인자로 함수(여기서는 `lambda` 함수)를 받으며, 이 함수는 각 그룹(`x`로 표현)에 대해 `True` 또는 `False`를 반환해야 합니다. `True`를 반환하는 그룹의 모든 원본 행이 최종 결과에 포함됩니다.
    * `lambda x : x["Salary"].mean() >= 70000`는 각 그룹 `x` 내에서 'Salary' 컬럼의 평균을 계산하고, 이 평균이 70000 이상인지 여부를 확인하는 조건입니다. 'IT' 부서와 'Marketing' 부서는 이 조건을 만족하므로 해당 부서의 모든 직원이 결과에 포함됩니다.
4.  **오타 수정**: `lambda` 키워드를 `lamda`로 잘못 입력하여 발생했던 `SyntaxError`를 `lambda`로 올바르게 수정하여 문제를 해결했습니다. 키워드 오타는 흔한 실수이므로 주의해야 합니다.

**추가 학습 (공인회계사 업무와의 관련성)**:
* **이상치/특정 조건 만족 그룹 식별**: 공인회계사는 데이터의 이상 징후나 특정 기준을 만족하는 거래/계정 그룹을 식별하는 데 `filter()`를 유용하게 활용할 수 있습니다.
    * **예시 1: 특정 지점의 비정상적인 매출 변동**: `groupby('지점')['매출액'].filter(lambda x: x.std() / x.mean() > 0.5)` 와 같이 사용하여, 매출 변동성이 평균의 50%를 초과하는 비정상적인 지점을 찾아낼 수 있습니다. 이는 **이상치 탐지** 및 **내부 통제 점검**에 도움이 됩니다.
    * **예시 2: 특정 기준을 초과하는 비용 계정**: `groupby('비용계정')['금액'].filter(lambda x: x.sum() > 1000000)` 처럼 사용하여, 총 비용이 특정 금액을 초과하는 계정만 선별하여 추가적인 감사 절차를 수행할 대상을 선정할 수 있습니다. 이는 **중요성 평가** 및 **감사 계획 수립**에 기여합니다.
* **데이터의 부분 집합 분석**: 감사 범위나 특정 보고서 작성을 위해 전체 데이터 중 특정 기준을 충족하는 부분 집합만 추출해야 할 때 `filter()`는 매우 효과적입니다. 예를 들어, 특정 평균 수익률을 넘는 투자 포트폴리오만 분석하거나, 특정 부채 비율을 초과하는 고객 그룹을 식별하는 데 사용될 수 있습니다.

`filter()`는 `groupby()` 이후 원본 DataFrame의 구조를 유지한 채 조건에 맞는 그룹 전체를 반환한다는 점에서 `agg()`나 `transform()`과는 다른 강력한 유용성을 가집니다. 회계 및 감사 업무에서 **특정 조건을 만족하는 개별 거래나 계정을 상세히 검토할 필요가 있을 때** 특히 유용하게 사용될 수 있습니다.
"""
