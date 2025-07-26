# ==============================================================================
# [문제 6.3.2] Pandas 그룹 기반 변환 (Day 6 학습 내용)
# ==============================================================================

# --- [최초 나의 코딩] ---
import pandas as pd
data = {'Department': ['HR', 'IT', 'HR', 'IT', 'Marketing', 'HR', 'IT'],
        'Position': ['Manager', 'Developer', 'Staff', 'Developer', 'Manager', 'Staff', 'Manager'],
        'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
        'Salary': [90000, 75000, 62000, 80000, 100000, 65000, 95000]}
employees_df_v2 = pd.DataFrame(data)

employees_df_v2["Salary_Deviation"] = employees_df_v2.groupby("Department")["Salary"].transform(lambda x : x - x.mean().round(2))

print("\n--- 'Salary_Deviation' 컬럼이 추가된 employees_df_v2 DataFrame ---")
print(employees_df_v2)

# filter와 transform 둘 다 lambda를 쓰니까, 해당 부분에 대한 추가 학습을 하자

# --- [코드 실행 결과] ---
"""
--- 'Salary_Deviation' 컬럼이 추가된 employees_df_v2 DataFrame ---
  Department   Position Employee  Salary  Salary_Deviation
0         HR    Manager    Alice   90000          27500.00
1         IT  Developer      Bob   75000          -5833.33
2         HR      Staff  Charlie   62000          -3750.00
3         IT  Developer    David   80000          -833.33
4  Marketing    Manager      Eve  100000             0.00
5         HR      Staff    Frank   65000           -500.00
6         IT    Manager    Grace   95000          14166.67
"""

# --- [피드백] ---
"""
문제 6.3.2를 **완벽하게 해결**하셨습니다! `groupby()`와 `transform()` 메서드를 사용하여 각 부서별 평균에 대한 개인 급여 편차를 정확하게 계산하고 새로운 컬럼으로 추가했습니다.

1.  **정확한 그룹화**: `employees_df_v2.groupby("Department")`를 통해 부서별로 데이터를 올바르게 그룹화했습니다.
2.  **`transform()`을 사용한 그룹별 값 변환**: `transform(lambda x : x - x.mean().round(2))` 구문은 `transform()` 메서드의 핵심 기능을 잘 활용했습니다.
    * `transform()`은 각 그룹(`x`)에 대해 연산을 수행하고, 그 결과를 **원본 DataFrame의 인덱스(크기)에 맞춰** 반환하여 새로운 컬럼으로 추가할 수 있도록 합니다. 이는 각 개별 레코드에 그룹 기반의 계산 결과를 적용할 때 매우 유용합니다.
    * `lambda x : x - x.mean().round(2)`는 각 부서 그룹(`x`) 내에서 해당 직원의 급여에서 부서 평균 급여를 뺀 값을 계산합니다. `.round(2)`를 사용하여 평균값을 먼저 반올림한 후 편차를 계산한 점은 결과의 깔끔함을 유지하는 좋은 방법입니다.
3.  **새로운 컬럼 추가**: 계산된 `Salary_Deviation` 값을 기존 DataFrame에 새로운 컬럼으로 성공적으로 추가했습니다.

이 풀이는 Pandas `groupby()`와 `transform()`을 이용한 그룹 기반의 파생 변수 생성의 모범적인 예시이며, 데이터 분석에서 개별 레코드에 그룹 특성을 반영할 때 매우 유용하게 쓰입니다.
"""

# --- [모범 답안] ---
# 이미 '최초 나의 코딩'에서 모범적으로 해결되었으므로, 추가적인 모범 답안은 생략합니다.
# 코드의 가독성을 위해 평균 계산을 별도 변수로 빼거나 할 수도 있으나, 현재 코드도 매우 명확합니다.
# avg_salary_by_department = employees_df_v2.groupby("Department")["Salary"].transform('mean').round(2)
# employees_df_v2["Salary_Deviation_v2"] = employees_df_v2["Salary"] - avg_salary_by_department
# print("\n--- 'Salary_Deviation' 컬럼이 추가된 employees_df_v2 DataFrame (모범 답안 예시) ---")
# print(employees_df_v2)


# --- [학습 기록] ---
"""
**학습 질문**: 각 직원의 급여가 해당 부서의 평균 급여로부터 얼마나 차이가 나는지(편차)를 새로운 컬럼으로 추가하려면 어떻게 해야 할까? `groupby()`와 `transform()`의 역할은 무엇이며, `filter()`와는 어떻게 다른가?

**문제 해결**:
1.  **데이터프레임 준비**: 문제에서 주어진 직원 데이터를 포함하는 `employees_df_v2`를 생성했습니다.
2.  **`groupby()`로 그룹화**: `employees_df_v2.groupby("Department")`를 사용하여 데이터를 `'Department'` 컬럼을 기준으로 그룹화했습니다.
3.  **`transform()`을 이용한 그룹별 변환**: 그룹화된 객체에 `.transform()` 메서드를 적용하여 각 직원의 급여 편차를 계산했습니다.
    * `transform()`은 인자로 함수(여기서는 `lambda` 함수)를 받으며, 이 함수는 각 그룹(`x`로 표현)에 대해 연산을 수행합니다. 가장 중요한 특징은 반환되는 결과의 크기가 **원본 DataFrame과 동일**하다는 점입니다. 이를 통해 계산된 값을 새로운 컬럼으로 쉽게 추가할 수 있습니다.
    * `lambda x : x - x.mean().round(2)`는 각 그룹 `x` 내에서 각 직원의 급여(`x`)에서 해당 그룹의 평균 급여(`x.mean().round(2)`)를 뺀 값을 계산합니다. 이 연산은 각 그룹의 모든 행에 대해 적용되어, 원본 DataFrame의 'Salary' 컬럼과 동일한 순서와 길이를 가진 Series를 반환합니다.
4.  **새로운 컬럼 추가**: `employees_df_v2["Salary_Deviation"] = ...` 구문을 통해 계산된 편차 값을 `employees_df_v2` DataFrame에 `Salary_Deviation`이라는 새로운 컬럼으로 추가했습니다.

**추가 학습 (lambda 함수와 `filter()` vs `transform()` 공통점 및 차이점)**:

**공통점 (lambda 함수 활용):**
* `filter()`와 `transform()` 모두 `groupby()`와 함께 사용될 때 `lambda` 함수(또는 일반 함수)를 인자로 받아 각 그룹에 대해 사용자 정의 연산을 수행할 수 있습니다.
* `lambda x: ...`에서 `x`는 각 그룹에 해당하는 DataFrame 또는 Series를 나타냅니다. 이 `x`를 통해 그룹 내의 데이터에 접근하고 연산을 수행할 수 있습니다.

**차이점:**

1.  **`filter()`**:
    * **목적**: 그룹 **자체**를 필터링하여 특정 조건을 만족하는 **그룹의 모든 원본 행**을 반환합니다.
    * **반환 형태**: 원래 DataFrame의 구조와 동일한 형태의 DataFrame을 반환합니다. 그룹 단위로 `True`/`False`를 반환해야 하며, `True`인 그룹의 모든 행이 포함됩니다.
    * **예시**: `df.groupby('A').filter(lambda x: x['B'].sum() > 100)` -> 'B' 컬럼의 합계가 100을 초과하는 'A' 그룹의 모든 행을 반환. (그룹 전체가 필터링됨)

2.  **`transform()`**:
    * **목적**: 그룹별 연산을 수행한 결과를 **원본 DataFrame의 각 행에 매핑**하여 새로운 컬럼을 생성하거나 기존 컬럼을 변환합니다.
    * **반환 형태**: **원본 DataFrame의 길이와 동일한 Series**를 반환합니다. 이 Series를 새로운 컬럼으로 추가하거나 기존 컬럼을 덮어쓸 수 있습니다.
    * **예시**: `df.groupby('A')['B'].transform('mean')` -> 각 'A' 그룹 내 'B'의 평균을 계산하여, 원본 'B' 컬럼의 각 행에 해당 그룹의 평균값을 매핑하여 반환. (개별 값 변환)

**공인회계사 업무와의 관련성**:

* **`transform()`의 활용**:
    * **성과 평가 및 이상치 탐지**: 각 부서/지점/직원별 성과(예: 급여, 매출액)가 전체 평균 또는 해당 그룹 평균 대비 어느 정도의 편차를 보이는지 파악하는 데 유용합니다. 이를 통해 **성과가 저조하거나 (음의 편차), 지나치게 높아서 (양의 편차) 추가 조사가 필요한 개별 항목을 식별**할 수 있습니다.
        * 예시: `매출액_편차 = df.groupby('영업사원')['매출액'].transform(lambda x: x - x.mean())`
    * **그룹 내 상대적 위치 파악**: 특정 항목이 속한 그룹 내에서 상대적으로 어느 위치에 있는지 표준화된 지표를 만들 때 활용됩니다. (예: Z-score 계산)
    * **재무 비율 분석**: 특정 계정의 비율이 업계 평균 또는 해당 산업군 평균 대비 어떤지 파악하여 재무 상태를 평가할 때 활용될 수 있습니다. (예: `재고회전율_산업평균_대비 = df.groupby('산업')['재고회전율'].transform(lambda x: x / x.mean())`)

`transform()`은 그룹의 특성을 개별 레코드에 '주입'하여, **개별 데이터 포인트가 속한 그룹의 맥락에서 어떤 의미를 가지는지 분석**하는 데 매우 강력한 도구입니다. 이는 감사 절차에서 특정 거래의 비정상성 여부를 판단하거나, 내부 통제 강화를 위한 분석에 큰 도움이 됩니다.
"""
