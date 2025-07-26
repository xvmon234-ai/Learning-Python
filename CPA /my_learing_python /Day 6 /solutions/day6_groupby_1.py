# ==============================================================================
# [문제 6.1.1] Pandas 그룹화 및 집계 (Day 6 학습 내용)
# ==============================================================================

import pandas as pd
import numpy as np # numpy는 현재 문제에 직접 사용되지 않지만, Pandas와 함께 자주 사용되므로 포함할 수 있습니다.

# --- [문제 데이터프레임 정의] ---
employees_data = {'Department': ['HR', 'IT', 'HR', 'IT', 'Marketing', 'HR'],
                  'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
                  'Salary': [60000, 75000, 62000, 80000, 70000, 65000]}
employees_df = pd.DataFrame(employees_data)

# --- [최초 나의 코딩] ---
print("\n--- Department mean Salary ---")
print(employees_df.groupby("Department")["Salary"].mean().round(2))

# --- [코드 실행 결과] ---
"""
--- Department mean Salary ---
Department
HR           62333.33
IT           77500.00
Marketing    70000.00
Name: Salary, dtype: float64
"""

# --- [피드백] ---
"""
문제 6.1.1에 대한 접근과 해결 모두 훌륭합니다!

1.  **정확한 그룹화 및 집계**: `employees_df.groupby("Department")["Salary"].mean()`을 사용하여 각 부서별 'Salary'의 평균을 정확하게 계산했습니다. 이는 Pandas의 `groupby()`와 단일 집계 함수의 기본 활용법을 완벽히 이해하고 있음을 보여줍니다.
2.  **출력 형식 제어**: `mean().round(2)`를 통해 결과값의 소수점을 둘째 자리로 제한한 것은 매우 실용적이고 깔끔한 접근입니다. 실제 데이터 분석에서 결과를 보고서나 대시보드에 활용할 때 가독성을 크게 높여줍니다. f-string과 같은 문자열 포매팅 없이 **데이터 자체를 제어**했다는 점에서 효율적인 방법입니다.

이 코드는 `groupby()`의 핵심 개념을 잘 보여주는 **간결하고 효율적인 예시**입니다.
"""

# --- [모범 답안] ---
# 이미 '나의 코딩'에서 모범적으로 해결되었으므로, 추가적인 모범 답안은 생략합니다.
# 다만, 명시적으로 변수에 할당하여 재활용할 수 있는 형태로 작성할 수도 있습니다.
# department_avg_salary = employees_df.groupby("Department")["Salary"].mean().round(2)
# print("\n--- 각 부서별 평균 급여 (모범 답안 예시) ---")
# print(department_avg_salary)


# --- [학습 기록] ---
"""
**학습 질문**: Pandas `groupby()`를 통해 계산된 평균값의 소수점을 깔끔하게 처리하려면 어떻게 해야 할까? f-string처럼 출력 시에만 형식을 지정하는 방법 외에, 데이터 자체를 반올림하는 방법은 없을까?

**문제 해결**:
1.  **`groupby()`와 `mean()` 사용**: 먼저 `employees_df.groupby("Department")["Salary"].mean()`을 통해 부서별 평균 급여를 계산했습니다. 이 단계에서 결과는 부동소수점 값으로 나옵니다.
2.  **`round()` 메서드 활용**: 계산된 평균값 뒤에 **`.round(2)`**를 직접 연결하여 소수점 둘째 자리까지 반올림하도록 처리했습니다. 이는 `Series`나 `DataFrame` 객체에 직접 적용할 수 있는 유용한 메서드로, 결과의 가독성을 즉각적으로 향상시킵니다.
3.  **결과 확인**: 출력된 결과에서 각 부서의 평균 급여가 소수점 둘째 자리까지 깔끔하게 정리되어 나타남을 확인했습니다.

**추가 학습**:
* **`round()`의 유용성**: `round()` 메서드는 `numpy.round()`와 유사하게 동작하며, Pandas Series나 DataFrame의 숫자형 데이터에 직접 적용할 수 있어 편리합니다. 단순히 출력 형식 지정이 아니라, **실제 데이터 값을 특정 소수점 이하로 정제**할 때 매우 유용합니다.
* **다양한 `round()` 활용**: 특정 컬럼에만 적용하거나, 전체 DataFrame에 적용하여 모든 숫자 컬럼을 한 번에 반올림할 수도 있습니다. (예: `df.round({'col1': 2, 'col2': 0})` 또는 `df.round(2)`)
* **데이터 타입 변화**: `round()`를 적용해도 기본적으로 숫자형 데이터 타입(float)은 유지됩니다. 만약 정수형으로 변환해야 한다면 `astype(int)` 등을 추가로 고려할 수 있습니다.
"""
