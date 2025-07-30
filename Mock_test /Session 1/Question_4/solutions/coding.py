import pandas as pd
from datetime import datetime

#요구사항.01 데이터 불러오기 및 전처리
df = pd.read_csv("accounts_receivable_data.csv")
date_cols = ['Transaction_Date', 'Due_Date', 'Payment_Date']
df[date_cols] = df[date_cols].apply(lambda col: pd.to_datetime(col, errors='coerce'))

#요구사항.02 매출채권 회수 기간 분석
df_paid = df[df["Status"] == "Paid"].copy()
df_paid["Collection_Days"] = df_paid["Payment_Date"] - df_paid["Transaction_Date"]
avg_collection_days = df_paid["Collection_Days"].mean()
threshold = avg_collection_days + pd.Timedelta(days=30)
df_anomaly = df_paid[df_paid['Collection_Days'] > threshold].copy()

print(f"\n 평균 회수 기간: {avg_collection_days.days}일")
print(f"\n 임계값 (평균 + 30일): {threshold.days}일")
print("\n 이상 징후 매출채권 목록:")
print(df_anomaly)

#요구사항.03 장기 미회수 매출채권 식별
today = datetime(2024, 4, 30)
df_due = df[df["Status"].isin(["Outstanding", "Overdue"])].copy()
df_due["Days_Overdue"] = (today - df["Due_Date"]).dt.days
df_over_60 = df_due[df_due["Days_Overdue"] > 60]
print("\n 60일 이상 초과한 매출채권")
print(df_over_60)

#요구사항.04 고객별 채권 잔액 변동 분석
df_customer = df_due.groupby("Customer_ID")["Amount"].sum()
print("\n Overdue 고객별 잔액")
print(df_customer)
df_high_customer = df_customer[df_customer > 30000000]
print(df_high_customer)
