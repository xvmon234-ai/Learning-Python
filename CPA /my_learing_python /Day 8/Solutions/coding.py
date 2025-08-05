"""
Day 8 (7/29 화) - 실전 모의고사 1회: 데이터 처리 및 정제
문제 해결을 위한 코딩 기록
"""

# ==============================================================================
# [1] 최초 작성한 코드 (사용자 제공)
# ==============================================================================

import pandas as pd
import numpy as np

#요구사항 01. 데이터 데이터 불러오기 및 기본 정보 확인
df = pd.read_csv("asset_inventory_data.csv")
df.info()
print(df.head())

#요구사항 02. 데이터 전처리 및 정제
df['Status'] = df['Status'].fillna('Unknown') #최초에 df['Status']가 아니라  df 라고 적어서 'Status'에 대해서만 fillna를 수행한 것이 아니라 df를 하나의 시리즈로 만들어버리는 오류를 범함
df['Acquisition_Date'] = pd.to_datetime(df['Acquisition_Date'])
df['Last_Audit_Date'] = pd.to_datetime(df['Last_Audit_Date'])
df['Book_Value'] = (df["Unit_Cost"] - df['Salvage_Value']) * df['Quantity'] #salbage_value가 0보다 큰 경우에도 작동하도록 코딩을 짜진 못함
df['Depreciation_Status'] = np.where(
    df['Useful_Life_Years'] > 0,
    "Depreciating",
    "Non-Depreciating"
)
#ValueError가 발생해서 이를 해결하기 위해 처음에는 앞에 int()를 붙였는데, series를 int로 변환할 수 없다는 TypeError 발생
#np.where에 대한 추가 학습이 필요함

#요구사항 03. 데이터 분석 및 필터링
condition1 = (df['Status'] == 'Active')
condition2 = (df['Acquisition_Date'] >= '2023-01-01')
condition3 = (df['Book_Value'] >= 100000000)
#조건문을 직접 안에 하드코딩하는 것보다 이렇게 별도 변수로 빼내는 것에 대한 이점을 잘 기억해둘 것

df_filtered = df[condition1 & condition2 & condition3]

print(df_filtered.head())

#요구사항 04. 데이터 집계 및 요약
df_grouped = df_filtered.groupby("Department")['Book_Value'].sum()
df_filtered["Total_Book_Value"] = df_grouped
print(df_filtered.head())

# ==============================================================================
# [2] 피드백 및 수정된 코드
# ==============================================================================

# 문제점 1: df = df['Status'].fillna('Unknown') 에서 전체 df가 Series로 변경되는 문제
# 문제점 2: if df['Useful_Life_Years'] > 0: 에서 ValueError 발생하는 문제
# 문제점 3: groupby 결과를 기존 df_filtered에 합치는 과정에서 인덱스 불일치 문제

# 수정된 코드:
# ------------------------------------------------------------------------------
# 1. 파일 불러오기 및 기본 정보 확인
df = pd.read_csv("asset_inventory_data.csv")
df.info()
print("\n[Original DataFrame Head]\n", df.head())

# 2. 데이터 전처리 및 정제
# 2-1. 'Status' 컬럼 결측치 처리 (원본 컬럼에 재할당)
df['Status'] = df['Status'].fillna('Unknown')

# 2-2. 날짜 형식 변환
df['Acquisition_Date'] = pd.to_datetime(df['Acquisition_Date'])
df['Last_Audit_Date'] = pd.to_datetime(df['Last_Audit_Date'])

# 2-3. 'Book_Value' 컬럼 생성
df['Book_Value'] = (df["Unit_Cost"] - df['Salvage_Value']) * df['Quantity']

# 2-4. 'Depreciation_Status' 컬럼 생성 (np.where 사용)
df['Depreciation_Status'] = np.where(
    df['Useful_Life_Years'] > 0,
    "Depreciating",
    "Non-Depreciating"
)

print("\n[Processed DataFrame Info]\n")
df.info()
print("\n[Processed DataFrame Head]\n", df.head())

# 3. 데이터 분석 및 필터링
# 3-1. 다중 필터링 조건 설정
condition1 = (df['Status'] == 'Active')
condition2 = (df['Acquisition_Date'] >= '2023-01-01')
condition3 = (df['Book_Value'] >= 100000000)

# 3-2. 필터링된 데이터프레임 생성
df_filtered = df[condition1 & condition2 & condition3]
print("\n[Filtered DataFrame Head]\n", df_filtered.head())

# 4. 데이터 집계 및 요약
# 4-1. 부서별 'Book_Value' 총합 계산 및 인덱스 초기화
df_summary = df_filtered.groupby("Department")['Book_Value'].sum().reset_index()

print("\n[Grouped Summary DataFrame]\n", df_summary)

# 5. 최종 결과 저장
df_summary.to_csv("department_book_value_summary.csv", index=False)
print("\n'department_book_value_summary.csv' 파일이 성공적으로 저장되었습니다.")


# ==============================================================================
# [3] 추가 학습 내용
# ==============================================================================

# 1. 벡터화 연산의 중요성:
#    - Python의 기본 for 반복문 대신, Pandas나 NumPy의 벡터화된 연산을 사용하면 코드가 훨씬 빠르고 효율적이다.
#    - 예: df['컬럼'] > 0 와 같은 조건식은 각 행에 대해 반복적으로 실행되는 것이 아니라, 전체 컬럼에 대해 한 번에 병렬 처리된다.
#
# 2. np.where() 함수 활용법:
#    - np.where(condition, value_if_true, value_if_false) 형태로 사용한다.
#    - 시리즈 전체에 대해 if-else 논리를 적용할 때 ValueError를 피하고 효율적인 코딩을 가능하게 한다.
#
# 3. groupby()와 reset_index():
#    - groupby()는 그룹화된 컬럼을 새로운 인덱스로 만든다.
#    - 집계 결과를 다시 일반 데이터프레임 형태로 만들고 싶을 때 .reset_index()를 사용하면, 그룹화 기준 컬럼이 다시 일반 컬럼으로 돌아온다.
#
# 4. DataFrame과 Series 구분:
#    - DataFrame은 2차원 테이블 형태의 데이터 구조이고, Series는 1차원 데이터 구조이다.
#    - df['컬럼명'] = df['컬럼명'].fillna(...) 와 같이 연산 결과를 원본 컬럼에 재할당해야 DataFrame의 구조가 유지된다.
#
# 5. 다중 조건 필터링:
#    - 각 조건을 괄호 ()로 묶고 & (and), | (or) 논리 연산자로 연결해야 한다.
#    - 예: df[(condition1) & (condition2)]
