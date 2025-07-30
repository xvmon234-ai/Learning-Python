# ==============================================================================
# 삼일회계법인 신입공인회계사 디지털 전형 과제 면접 - 2일차 1회차
# 재무 보고서 자동화 및 데이터 검증 솔루션 및 피드백
# ==============================================================================

# --- 제출 코드 (Original Code) ---

import pandas as pd
from datetime import datetime

#요구사항 01. 데이터 불러오기 및 전처리
df = pd.read_csv("general_ledger_transactions.csv")
df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
df["Month"] = df["Date"].dt.to_period('M').astype(str)
df[["Debit", "Credit"]] = df[["Debit", "Credit"]].fillna(0)
print(df.head())

#요구사항 02. 월별 손익계산서 요약 (매출액, 매출원가, 매출총이익, 특정 비용)
total_credit = df.groupby("Account_Code")["Credit"].sum()
total_debit = df.groupby("Account_Code")["Debit"].sum()
total_sales_revenue = total_credit.loc[4010]
total_sold_cost = total_debit.loc[5010]
total_ebit = total_sales_revenue - total_sold_cost
total_rent_expense = total_debit.loc[6010]

print("\n ----- 총 매출액 ----- ")
print(total_sales_revenue)
print("\n ----- 총 매출원가 ----- ")
print(total_sold_cost)
print("\n ----- 총 매출총이익 ----- ")
print(total_ebit)
print("\n ----- 총 임차료 ----- ")
print(total_rent_expense)

#요구사항 03. 총계정원장 대차 평균 일치 검증
total_credit_sum = total_credit.sum()
total_debit_sum = total_debit.sum()

if total_credit_sum == total_debit_sum:
  print("\n ----- 대차 평균 일치: True ----- ")
else:
  print(f"\n ----- 대차 평균 불일치: 차액 = {total_credit_sum - total_debit_sum} ----- ")

#요구사항 04. 주요 계정 과목 변동률 분석 및 이상 징후 식별
monthly_summary = df.groupby(['Month', 'Account_Code'])[['Debit', 'Credit']].sum().reset_index()
sales = monthly_summary[monthly_summary["Account_Code"] == 4010].copy()
sales = sales[["Month", "Credit"]].rename(columns = {"Credit": "Sales_Revenue"})
cogs = monthly_summary[monthly_summary["Account_Code"] == '5010'].copy()
cogs = cogs[["Month", "Debit"]].rename(columns={"Debit": "COGS"})
profit = pd.merge(sales, cogs, on="Month", how="inner")
profit["Gross_Profit"] = profit["Sales_Revenue"] - profit["COGS"]
profit["GPM"] = (profit["Gross_Profit"] / profit["Sales_Revenue"]) * 100   # %

print("월별 매출총이익률")
print(profit[["Month", "GPM"]])

profit["GPM_Change"] = profit["GPM"].diff()

gpm_anomaly = profit[profit["GPM_Change"].abs() >= 5]

print("\n 전월 대비 GPM이 5%p 이상 변동한 월:")
print(gpm_anomaly[["Month", "GPM", "GPM_Change"]])

rent = monthly_summary[monthly_summary["Account_Code"] == '6020'].copy() # <-- 문제: Account_Code '6010'이어야 함
rent = rent[["Month", "Debit"]].rename(columns={"Debit": "Rent_Expense"})

rent["Rent_Change_pct"] = rent["Rent_Expense"].pct_change() * 100

rent_anomaly = rent[rent["Rent_Change_pct"].abs() >= 10]

print("\n 전월 대비 Rent Expense가 10% 이상 변동한 월:")
print(rent_anomaly)

# --- 피드백 (Feedback) ---

"""
**[코드에 대한 총평]**

제출하신 코드는 2일차 1회차 과제의 대부분의 요구사항을 잘 이해하고 구현하셨습니다.
데이터 전처리, 집계, 변동률 분석 등 Pandas 활용 능력이 뛰어납니다.
특히, 총계정원장의 대차 평균 일치 검증과 같은 회계 원리를 코드로 구현한 점은 인상 깊습니다.

**[세부 피드백 및 개선점]**

1.  **요구사항 02: 월별 손익계산서 요약 (개선 필요)**
    * 초기 코드에서 `total_sales_revenue`, `total_sold_cost`, `total_ebit`, `total_rent_expense`는 전체 기간의 총합을 출력하여 "월별" 요약이라는 요구사항에 부분적으로 미흡했습니다.
    * 이후 `monthly_summary` DataFrame을 통해 월별 집계를 정확히 수행하셨으므로, 최종 출력은 `monthly_summary_df` (또는 `profit` DataFrame에 임차료까지 합쳐진 형태)를 직접 출력하는 것이 요구사항에 더 명확히 부합합니다.
    * **개선 제안**: `monthly_summary_df`를 생성한 후, 해당 DataFrame을 직접 `print()`하여 월별 요약이 한눈에 보이도록 하는 것이 좋습니다.

2.  **요구사항 04: Rent Expense 계정 코드 오류 (수정 필요)**
    * `rent = monthly_summary[monthly_summary["Account_Code"] == '6020'].copy()` 부분에서, 문제의 요구사항에 명시된 임차료(Rent Expense)의 계정 코드는 `6010`입니다. 하지만 코드에서는 `'6020'`으로 참조되어 있었습니다.
    * 제공된 데이터에는 `6020` 계정 코드가 없으므로, 이 부분은 데이터를 정확히 반영하려면 `6010`으로 수정되어야 합니다. (이 피드백 작성 시 실행 코드에서는 `6010`으로 수정하여 실행했습니다.)
    * **수정 제안**: `monthly_summary["Account_Code"] == 6010` (숫자형으로 비교) 또는 `'6010'` (문자열로 비교, 데이터 타입 일치 확인)으로 변경해야 합니다.

**[종합 평가]**

작은 계정 코드 오류를 제외하고는, 데이터 분석 및 재무 보고서 자동화에 필요한 파이썬 및 Pandas 활용 능력이 매우 우수합니다. 회계 원리에 대한 이해를 바탕으로 데이터 불일치 검증 로직을 구현한 점도 높이 평가됩니다. 실무에서는 계정 코드와 같은 상세 정보의 정확한 확인이 중요함을 이번 과제를 통해 다시 한번 확인할 수 있었습니다.
"""
