# Q. agg 메서드를 이용할 경우, (x = ("특정 칼럼", "집계 함수"))를 이용해서 새로운 칼럼을 부여할 수 있는 것으로 아는데,
#    이게 가능한 이유를 리스트, 딕셔너리, 튜플의 기본 개념과 엮어서 설명해줄 수 있어?

import pandas as pd
import numpy as np

# --- 0. 예시 데이터프레임 생성 ---
data = {'Department': ['HR', 'IT', 'HR', 'IT', 'Marketing', 'HR', 'IT', 'HR'],
        'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi'],
        'Salary': [60000, 75000, 62000, 80000, 70000, 65000, 78000, 63000]}
employees_df_for_agg = pd.DataFrame(data)

print("\n\n" + "="*70)
print("--- 섹션 6: agg() 메서드와 컬럼 재명명 심화 학습 ---")
print("="*70)

print("\n--- 원본 employees_df_for_agg DataFrame ---")
print(employees_df_for_agg)
print("-" * 50)

# --- 1. agg() 메서드의 기본 역할 ---
# agg() (aggregation) 메서드는 데이터를 집계(요약)할 때 사용됩니다.
# 주로 groupby()와 함께 사용되어 그룹별 통계량을 계산합니다.

print("\n--- agg() 기본 예시: Department별 Salary 평균과 최댓값 ---")
# Salary 컬럼에 대해 평균과 최댓값을 동시에 계산
basic_agg_result = employees_df_for_agg.groupby('Department')['Salary'].agg(['mean', 'max'])
print(basic_agg_result)
print("-" * 50)

# --- 2. agg()에서 컬럼 재명명 (Renaming)의 필요성 ---
# 위 기본 예시처럼 'mean', 'max'와 같이 함수 이름을 그대로 컬럼명으로 사용하면 편리합니다.
# 하지만, 때로는 결과 컬럼의 이름을 더 명확하게 지정하고 싶을 때가 있습니다.
# 예를 들어 'mean' 대신 'Average_Salary'와 같이 원하는 이름을 쓰고 싶을 때입니다.

# --- 3. (새로운_컬럼_이름 = ("기존_컬럼_이름", "집계_함수")) 문법의 이해 ---
# 이 문법은 Pandas agg() 메서드의 강력한 기능 중 하나로,
# 파이썬의 딕셔너리, 튜플, 리스트의 기본 개념을 활용합니다.

## 3.1. Python 딕셔너리 (Dictionary)의 역할: 새로운 컬럼 이름 정의
# 딕셔너리는 'key: value' 쌍으로 데이터를 저장합니다.
# agg()에 딕셔너리를 전달할 때, 딕셔너리의 'key'가 새로 생성될 결과 컬럼의 이름이 됩니다.
# 예: {'Average_Salary': 'mean'} => 'Average_Salary'라는 컬럼이 생김

## 3.2. Python 튜플 (Tuple)의 역할: 집계 대상과 함수 매핑
# 튜플은 순서가 있고 변경 불가능한 요소들의 컬렉션입니다.
# agg() 메서드에서는 딕셔너리의 'value'로 튜플을 사용하여
# "어떤 원본 컬럼에 어떤 집계 함수를 적용할지"를 명시합니다.
# 형태: ("원본_컬럼_이름", "집계_함수_이름")
# 예: ('Salary', 'mean') => 원본 'Salary' 컬럼에 'mean' 함수 적용

## 3.3. 키워드 인자(Keyword Arguments)로서의 활용
# Python에서 함수를 호출할 때, `함수(키워드=값)` 형태로 인자를 전달할 수 있습니다.
# agg() 메서드는 이러한 키워드 인자를 특별히 해석합니다.
# `agg(새로운_컬럼명 = (원본_컬럼명, 집계_함수명))` 형태로 전달하면,
# Pandas는 `새로운_컬럼명`을 결과 컬럼의 이름으로 사용하고,
# 괄호 안의 튜플 `(원본_컬럼명, 집계_함수명)`을 해당 컬럼을 집계할 지침으로 사용합니다.

print("\n--- agg()를 이용한 컬럼 재명명 예시 ---")

# 'Department'별로 그룹화한 후, agg()를 사용하여 여러 통계량을 계산하고 컬럼명 지정
# min_salary: 'Salary' 컬럼의 최솟값
# max_salary: 'Salary' 컬럼의 최댓값
# avg_salary: 'Salary' 컬럼의 평균
# num_employees: 'Employee' 컬럼의 개수 (즉, 그룹 내 직원 수)
department_stats_renamed = employees_df_for_agg.groupby('Department').agg(
    # 새로운_컬럼_이름 = (원본_컬럼_이름, "집계_함수_이름")
    min_salary=('Salary', 'min'),
    max_salary=('Salary', 'max'),
    avg_salary=('Salary', 'mean'),
    num_employees=('Employee', 'count')
)

print(department_stats_renamed)
print("-" * 50)

# --- 4. 왜 이 문법이 유용한가? ---
# 1. 명확성: 결과 컬럼의 이름이 바로 코딩 시점에 지정되므로 가독성이 높습니다.
# 2. 유연성: 하나의 agg() 호출 내에서 여러 원본 컬럼에 대해 다양한 집계 함수를 적용하고,
#            각 결과에 원하는 이름을 부여할 수 있습니다.
# 3. 간결성: 특히 여러 집계를 동시에 수행할 때, 코드가 훨씬 간결해집니다.
#    (예: employees_df.groupby('Dept')['Salary'].agg(['mean', 'max']) 대신
#          employees_df.groupby('Dept').agg(avg_sal=('Salary','mean'), max_sal=('Salary','max')))

print("\n--- 이 문법의 동작 원리 요약 ---")
print("Pandas는 agg()에 전달된 키워드 인자(예: `새로운_컬럼_이름=`)를 새로운 컬럼명으로 사용합니다.")
print("해당 키워드 인자의 값으로 전달된 튜플 `('원본_컬럼_이름', '집계_함수_이름')`을")
print("원본 데이터에서 어떤 컬럼을 가져와 어떤 함수로 집계할지에 대한 지침으로 해석합니다.")
print("이것은 파이썬 딕셔너리의 '키'와 '값' 개념, 그리고 튜플의 순서 있는 데이터 저장 방식이")
print("Pandas의 유연한 파싱 로직과 결합되어 가능한 강력한 기능입니다.")
print("="*70)
