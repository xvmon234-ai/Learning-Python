# ==============================================================================
# 추가 학습: Pandas DataFrame 생성 방식 비교 (컬럼 기준 vs 행 기준)
# ==============================================================================

# Pandas DataFrame은 데이터를 표 형태로 다루는 핵심 객체입니다.
# DataFrame을 생성하는 여러 방법 중, 데이터를 구성하는 방식에 따라
# 크게 '컬럼 기준'과 '행 기준' 두 가지를 비교해 보겠습니다.

import pandas as pd
import numpy as np

print("--- DataFrame 생성 방식 비교 ---")

# ------------------------------------------------------------------------------
# 1. 딕셔너리-리스트 조합 (컬럼 기준) 📚
# ------------------------------------------------------------------------------
# 정의: {'컬럼명1': [값1, 값2, ...], '컬럼명2': [값1, 값2, ...], ...} 형태입니다.
#       즉, 딕셔너리의 '키'가 컬럼명이 되고, '값'으로 각 컬럼에 들어갈 데이터(리스트)가 옵니다.

print("\n## 1. 딕셔너리-리스트 조합 (컬럼 기준)")

# 👍 장점:
#   - 직관적이고 표준적: 대부분의 표 데이터를 컬럼 단위로 이해하고 구성하기 쉽습니다.
#     Pandas가 내부적으로 데이터를 처리하는 방식과도 잘 맞아 가장 흔히 권장되는 방법입니다.
#   - 코드 가독성: 컬럼별로 어떤 데이터가 들어가는지 한눈에 파악하기 용이합니다.
#   - 메모리 효율성: 대용량 데이터를 처리할 때 컬럼별로 묶는 것이 유리할 수 있습니다.

# 👎 단점:
#   - 데이터 길이 일치 필수: 모든 컬럼(리스트)의 길이가 반드시 같아야 합니다.
#     만약 하나라도 길이가 다르면 ValueError가 발생하여 DataFrame을 생성할 수 없습니다.

# [예시 코드]
data_col_wise = {
    '이름': ['김민준', '이서연', '박지훈'],
    '나이': [25, 30, 35],
    '도시': ['서울', '부산', '제주']
}
df_col_wise = pd.DataFrame(data_col_wise)
print("\n[딕셔너리-리스트 조합 DataFrame]")
print(df_col_wise)
print("-" * 50)


# ------------------------------------------------------------------------------
# 2. 리스트-딕셔너리 조합 (행 기준) 📜
# ------------------------------------------------------------------------------
# 정의: [{'컬럼명1': 값1-1, '컬럼명2': 값1-2, ...}, {'컬럼명1': 값2-1, '컬럼명2': 값2-2, ...}, ...] 형태입니다.
#       즉, 리스트 안에 각 '행'을 나타내는 딕셔너리들이 요소로 들어갑니다.

print("## 2. 리스트-딕셔너리 조합 (행 기준)")

# 👍 장점:
#   - ⭐ 중구난방인 자료에 매우 탁월함 ⭐: 각 행(딕셔너리)마다 가지고 있는 컬럼의 종류나 수가 달라도 문제없습니다.
#     누락된 컬럼은 자동으로 NaN (결측치)으로 채워져 유연하게 DataFrame을 생성할 수 있습니다.
#     예를 들어, 웹 스크래핑이나 API 호출로 데이터를 행 단위로 가져올 때 각 레코드의 데이터 구성이 일정치 않아도 쉽게 처리 가능합니다.
#   - 행 단위 데이터 수집에 용이: 데이터를 한 번에 한 행씩 수집하거나 생성할 때
#     파이썬 리스트에 딕셔너리를 바로 추가하는 방식으로 편리하게 구성할 수 있습니다.

# 👎 단점:
#   - 상대적으로 비직관적일 수 있음: 컬럼별 데이터 분포를 한눈에 파악하기 어렵습니다.
#   - 잠재적 성능 문제: 데이터의 양이 매우 많아질 경우, 행 단위로 딕셔너리를 구성하는 것이
#     컬럼 단위보다 성능상 불리할 수 있습니다 (하지만 일반적인 사용에서는 크게 체감되지 않을 수 있습니다).

# [예시 코드]
data_row_wise = [
    {'이름': '최유진', '나이': 40, '도시': '대구'},
    {'이름': '김도현', '나이': 28}, # '도시' 컬럼이 누락됨
    {'이름': '이지원', '도시': '광주', '직업': '개발자'} # 새로운 컬럼 추가
]
df_row_wise = pd.DataFrame(data_row_wise)
print("\n[리스트-딕셔너리 조합 DataFrame (NaN과 새 컬럼 자동 처리)]")
print(df_row_wise)
print("-" * 50)

# ==============================================================================
# 요약:
# - 컬럼 기준 (딕셔너리-리스트): 정형 데이터, 모든 컬럼 길이 동일 시 가장 효율적이고 직관적.
# - 행 기준 (리스트-딕셔너리): 비정형 또는 가변적인 행 단위 데이터 수집에 유연함.
# ==============================================================================
