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
profit["GPM"] = (profit["Gross_Profit"] / profit["Sales_Revenue"]) * 100  # %

print("월별 매출총이익률")
print(profit[["Month", "GPM"]])

profit["GPM_Change"] = profit["GPM"].diff()

gpm_anomaly = profit[profit["GPM_Change"].abs() >= 5]

print("\n 전월 대비 GPM이 5%p 이상 변동한 월:")
print(gpm_anomaly[["Month", "GPM", "GPM_Change"]])

rent = monthly_summary[monthly_summary["Account_Code"] == '6020'].copy()
rent = rent[["Month", "Debit"]].rename(columns={"Debit": "Rent_Expense"})

rent["Rent_Change_pct"] = rent["Rent_Expense"].pct_change() * 100

rent_anomaly = rent[rent["Rent_Change_pct"].abs() >= 10]

print("\n 전월 대비 Rent Expense가 10% 이상 변동한 월:")
print(rent_anomaly)
