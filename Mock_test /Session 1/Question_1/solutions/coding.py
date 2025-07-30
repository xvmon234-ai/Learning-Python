import pandas as pd
from io import StringIO

department_A_expenses = """Date,Description,Amount,Category
2025-06-01,Office Supplies,15000,Administrative
2025-06-05,Client Dinner,80000,Entertainment
2025-06-10,Software License Renewal,500000,IT
2025-06-15,Travel Expense,120000,Travel
2025-06-20,Consulting Fee,300000,Professional Service
"""

department_B_expenditures = """Transaction_Date,Item_Description,Cost,Expense_Type
2025-06-03,Marketing Campaign,200000,Marketing
2025-06-08,Utility Bill,75000,Utilities
2025-06-12,Hardware Purchase,150000,IT
2025-06-18,Seminar Registration,90000,Training
2025-06-22,Rent,250000,Rent
"""

df_A = pd.read_csv(StringIO(department_A_expenses))
df_B = pd.read_csv(StringIO(department_B_expenditures))

#요구사항 1. 데이터 불러오기
print("\n ----- Department A Expenses ----- ")
print(df_A)
print("\n ----- Department B Expenditures ----- ")
print(df_B)

#요구사항 2. 컬럼명 통일하기
df_B.rename(columns={"Transaction_Date" : "Date", "Item_Description" : "Description", "Cost" : "Amount", "Expense_Type" : "Category"}, inplace=True)
print("\n ----- Department B Expenditures Col renamed ----- ")
print(df_B)

#요구사항 3. DataFrame 병합하기
df_combined = pd.concat([df_A, df_B], ignore_index=True)
print("\n ----- Combined DataFrame ----- ")
print(df_combined)

#요구사항 4. Amount 컬럼 데이터 타입 변환
df_combined["Amount"] = df_combined["Amount"].astype(int)

#요구사항 5. Date 컬럼 날짜 형식 변환
df_combined["Date"] = pd.to_datetime(df_combined["Date"])

#요구사항 6. 특정 비용 항목 분류 및 집계
df_filtered = df_combined[df_combined["Category"].isin(["IT", "Travel"])]
df_grouped = df_filtered.groupby("Category")["Amount"].sum()
df_grouped_sorted = df_grouped.sort_values(ascending=False)
print("\n ----- Grouped DataFrame with filtered data ----- ")
print(df_grouped_sorted)

#요구사항 7. 결과 CSV 파일로 저장
df_final = df_combined[['Date', 'Description', 'Amount', 'Category']]
df_final.to_csv("monthly_expenses_report_202506.csv", index=False)

print("CSV 파일이 저장되었습니다: monthly_expenses_report_202506.csv")
