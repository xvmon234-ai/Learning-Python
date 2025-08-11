# ==============================================================================
# [문제 6.2.1] Pandas 다중 컬럼 그룹화 및 다중 집계 (Day 6 학습 내용)
# ==============================================================================

# --- [최초 나의 코딩] ---
import pandas as pd
data = {'Department': ['HR', 'IT', 'HR', 'IT', 'Marketing', 'HR', 'IT'],
        'Position': ['Manager', 'Developer', 'Staff', 'Developer', 'Manager', 'Staff', 'Manager'],
        'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
        'Salary': [90000, 75000, 62000, 80000, 100000, 65000, 95000]}
employees_df_v2 = pd.DataFrame(data)

group_df_v1 = employees_df_v2.groupby(["Department", "Position"]).agg(최고연봉=("Salary", "max"), 평균연봉=("Salary", "mean"))
# 최초 답변에서는 최고연봉 = ("Salary":"max")로 해서 SyntaxError 발생

print("\n--- Department and Position with Max and Avg Salary ---")
print(group_df_v1)

# --- [코드 실행 결과] ---
"""
--- Department and Position with Max and Avg Salary ---
                       최고연봉    평균연봉
Department Position                  
HR         Manager   90000.0  90000.0
           Staff     65000.0  63500.0
IT         Developer 80000.0  77500.0
           Manager   95000.0  95000.0
Marketing  Manager  100000.0 100000.0
"""

# --- [피드백] ---
"""
문제 6.2.1을 **매우 정확하고 효율적으로 해결**하셨습니다! 다중 컬럼 그룹화와 `agg()` 메서드를 사용한 다중 집계를 완벽하게 구현했습니다.

1.  **다중 컬럼 그룹화**: `employees_df_v2.groupby(["Department", "Position"])`을 통해 'Department'와 'Position'이라는 **두 가지 기준**으로 데이터를 효과적으로 그룹화했습니다. 이는 실제 복잡한 데이터를 분석할 때 매우 중요한 기법입니다.
2.  **`agg()`를 사용한 다중 집계**: `agg(최고연봉=("Salary", "max"), 평균연봉=("Salary", "mean"))` 구문은 `agg()` 메서드의 **가장 강력한 활용법 중 하나**를 보여줍니다.
    * 새로운 컬럼 이름(`최고연봉`, `평균연봉`)을 지정하면서, 원본 컬럼(`"Salary"`)에 대해 여러 다른 집계 함수(`"max"`, `"mean"`)를 동시에 적용했습니다. 이 방식은 결과 DataFrame의 컬럼명을 사용자 정의할 수 있어 가독성을 크게 높입니다.
3.  **SyntaxError 해결**: `최고연봉 = ("Salary":"max")`에서 `최고연봉 = ("Salary", "max")`로 수정하여 `SyntaxError`를 해결하신 점은 칭찬할 만합니다. Python 딕셔너리 또는 함수 인자에서 키-값 쌍을 지정할 때는 콜론(`:`)이 아닌 쉼표(`,`)를 사용하여 튜플 형태로 전달해야 함을 정확히 파악했습니다.

이 풀이는 Pandas의 `groupby()`와 `agg()`를 이용한 다중 집계의 모범적인 예시이며, 데이터 요약 및 심층 분석에 대한 뛰어난 이해를 보여줍니다.
"""

# --- [모범 답안] ---
# 이미 '나의 코딩'에서 모범적으로 해결되었으므로, 추가적인 모범 답안은 생략합니다.
# 다만, 결과를 변수에 할당하는 것은 좋은 습관입니다.
# department_position_salaries = employees_df_v2.groupby(["Department", "Position"]).agg(
#     최고연봉=("Salary", "max"),
#     평균연봉=("Salary", "mean")
# )
# print("\n--- Department and Position with Max and Avg Salary (모범 답안 예시) ---")
# print(department_position_salaries)


# --- [학습 기록] ---
"""
**학습 질문**: 여러 컬럼을 기준으로 데이터를 그룹화하고, 동시에 여러 집계 함수를 적용하여 새로운 컬럼 이름으로 결과를 얻으려면 어떻게 해야 할까?

**문제 해결**:
1.  **다중 컬럼으로 그룹화**: `employees_df_v2.groupby(["Department", "Position"])`을 사용하여 `'Department'`와 `'Position'` 두 컬럼을 기준으로 데이터를 그룹화했습니다. `groupby()`에 컬럼 이름 리스트를 전달하여 다중 그룹화를 수행합니다.
2.  **`agg()` 메서드를 이용한 다중 집계**: 그룹화된 객체에 `.agg()` 메서드를 적용하여 여러 집계 연산을 한 번에 수행했습니다.
    * `agg()` 메서드 내부에 딕셔너리 형태로 `새로운_컬럼명=(원본_컬럼명, '집계_함수명')`의 구문을 사용했습니다. 예를 들어, `최고연봉=("Salary", "max")`는 `'Salary'` 컬럼에 대해 `max` 함수를 적용하고 그 결과를 `최고연봉`이라는 새 컬럼에 저장하라는 의미입니다.
    * 동일한 방식으로 `평균연봉=("Salary", "mean")`을 사용하여 `'Salary'` 컬럼에 대해 `mean` 함수를 적용하고 `평균연봉` 컬럼에 저장했습니다.
3.  **SyntaxError 수정**: 처음 시도했던 `("Salary":"max")` 형태가 Python 문법 오류임을 파악하고, `("Salary", "max")`와 같이 튜플 형태로 수정하여 정확한 `agg()` 구문을 사용했습니다.

**추가 학습**:
* **`agg()`의 유연성**: `agg()` 메서드는 단일 컬럼에 여러 집계 함수를 적용하거나, 여러 컬럼에 각각 다른 집계 함수를 적용하는 등 매우 유연하게 사용할 수 있습니다.
    * 예시 1 (단일 컬럼에 여러 함수): `df.groupby('A')['B'].agg(['sum', 'mean', 'count'])`
    * 예시 2 (여러 컬럼에 각각 다른 함수): `df.groupby('A').agg({'B': 'sum', 'C': 'mean'})`
    * 예시 3 (새로운 컬럼명 지정): `df.groupby('A').agg(total_B=('B', 'sum'), avg_C=('C', 'mean'))`
* **MultiIndex 결과**: 다중 그룹화의 결과는 기본적으로 MultiIndex DataFrame이 됩니다. 필요에 따라 `.reset_index()`를 추가하여 일반 컬럼으로 변환할 수 있습니다. (이 문제에서는 `reset_index`를 사용하지 않았지만, 결과 확인 시 인덱스 구조를 이해하는 것이 중요합니다.)
"""
