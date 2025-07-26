# further_study.py

# Q. pivot_table 외에 회계사가 파이썬을 이용해서 데이터를 분석하거나 업무에 도움을 받을 수 있는 것이 또 무엇이 있을까요?

# ==============================================================================
# 🎯 CPA를 위한 Python 데이터 분석 추가 학습: Pivot Table 그 이상
# ==============================================================================

# 공인회계사(CPA)로서 Python은 단순히 데이터 요약을 넘어, 감사, 재무 분석, 컨설팅 등 다양한 업무에서
# 데이터 기반의 통찰력을 얻고 효율성을 높이는 강력한 도구가 될 수 있습니다.
# 아래는 pivot_table 외에 Python이 CPA 업무에 기여할 수 있는 주요 영역들입니다.

# ---

## 1. 데이터 클리닝 및 전처리 (Data Cleaning & Preprocessing)

### 개요
회계 데이터는 종종 오류, 누락, 중복, 일관성 없는 형식 등으로 지저분합니다. Python의 Pandas 라이브러리는 이러한 데이터를 **정제하고 분석 가능한 형태로 가공**하는 데 탁월합니다.

### CPA 관련성
* **감사 데이터의 신뢰성 확보**: 감사 대상 기업의 원장 데이터, 증빙 자료 등이 깨끗하지 않을 때, Python을 사용해 데이터를 표준화하고 불일치를 제거하여 감사 신뢰성을 높입니다.
* **결측치 처리**: 재무 보고서에서 누락된 값(예: 특정 월의 판매 데이터)을 식별하고, 합리적인 기준으로 채우거나(예: 이전 3개월 평균) 분석에서 제외합니다.
* **이상치 탐지 전처리**: 데이터 입력 오류나 비정상적인 거래(예: 지나치게 큰 금액, 잘못된 날짜)를 식별하고 수정하여, 분석의 정확성을 높입니다.

### Python 활용 예시
```python
import pandas as pd
import numpy as np

# 가상 데이터 (오류 포함)
dirty_data = {
    'TransactionID': [1, 2, 3, 4, 5],
    'Amount': [1000, 200, np.nan, 5000000, 300],
    'Date': ['2023-01-10', '2023-01-20', '2023-01-25', '2023-01-05', '2023-13-01'], # 잘못된 날짜
    'Description': ['SALES', 'Sales', 'sales ', 'Big Sale', 'Return']
}
df = pd.DataFrame(dirty_data)

print("--- 원본 데이터 ---")
print(df)

# 1. 컬럼명 일관성 유지 (선택 사항)
# df.columns = df.columns.str.lower()

# 2. 결측치 처리 (예: 평균으로 채우기, CPA는 보통 0이나 특정 값으로 채우거나 이상치로 판단)
df['Amount'] = df['Amount'].fillna(0) # 또는 df['Amount'].fillna(df['Amount'].mean())

# 3. 데이터 형식 통일 (예: Description 컬럼의 문자열 통일)
df['Description'] = df['Description'].str.lower().str.strip().replace({'sales': 'Sales', 'big sale': 'Sales'})

# 4. 날짜 형식 변환 및 오류 감지
# errors='coerce'는 변환 불가능한 값을 NaT (Not a Time)로 만듭니다.
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
# 잘못된 날짜 행 제거 (또는 수정)
df = df.dropna(subset=['Date'])

# 5. 이상치 제거 (간단한 예시: Amount가 너무 큰 값)
df = df[df['Amount'] < 1000000] # 상식적인 수준에서 너무 큰 금액 제거

print("\n--- 클리닝된 데이터 ---")
print(df)
