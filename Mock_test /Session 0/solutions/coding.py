import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
from datetime import datetime

asset_inventory_data = """Asset_ID,Asset_Type,Acquisition_Date,Quantity,Unit_Cost,Salvage_Value,Useful_Life_Years,Department,Location,Status,Last_Audit_Date
FA001,Machinery,2022-01-15,1,150000000,15000000,10,Production,Factory A,Active,2024-06-01
INV001,Raw Material A,2023-03-10,5000,5000,0,0,Production,Warehouse 1,In Stock,2024-05-15
FA002,Office Equipment,2022-06-20,10,500000,50000,5,Administration,Office B,Active,2024-06-01
INV002,Finished Goods X,2023-04-01,2000,15000,0,0,Sales,Warehouse 2,In Stock,2024-05-15
FA003,Vehicle,2022-09-01,1,30000000,3000000,7,Logistics,Depot C,Active,2024-06-01
INV003,Raw Material B,2023-05-05,3000,7000,0,0,Production,Warehouse 1,In Stock,2024-05-15
FA004,Computer Server,2022-11-12,5,10000000,1000000,8,IT,Data Center,Active,2024-06-01
INV004,Work-in-Progress Y,2023-06-18,1000,8000,0,0,Production,Factory A,In Stock,2024-05-15
FA005,Building,2021-03-01,1,500000000,50000000,20,Management,Head Office,Active,2024-06-01
INV005,Finished Goods Z,2023-07-20,1500,20000,0,0,Sales,Warehouse 2,In Stock,2024-05-15
FA006,Furniture,2022-04-25,20,300000,30000,5,Administration,Office B,Active,2024-06-01
INV006,Raw Material C,2023-08-10,4000,6000,0,0,Production,Warehouse 1,In Stock,2024-05-15
FA007,Forklift,2022-10-01,2,25000000,2500000,7,Logistics,Factory A,Active,2024-06-01
INV007,Packaging Material,2023-09-01,8000,1000,0,0,Production,Warehouse 1,In Stock,2024-05-15
FA008,Network Device,2022-12-05,3,7000000,700000,6,IT,Data Center,Active,2024-06-01
INV008,Maintenance Spares,2023-10-15,100,50000,0,0,Production,Warehouse 1,In Stock,2024-05-15
FA009,Production Line,2022-02-10,1,200000000,20000000,15,Production,Factory A,Active,2024-06-01
INV009,Chemicals,2023-11-20,2000,9000,0,0,Production,Warehouse 1,In Stock,2024-05-15
FA010,Generator,2022-07-01,1,40000000,4000000,10,Production,Factory A,Active,2024-06-01
INV010,Office Supplies,2023-12-01,1000,2000,0,0,Administration,Office B,In Stock,2024-05-15
FA011,Drone,2023-01-01,1,10000000,1000000,5,Logistics,Depot C,Active,2024-06-01
INV011,Spare Parts,2024-01-10,500,12000,0,0,Production,Warehouse 1,In Stock,2024-05-15
FA012,3D Printer,2023-02-15,1,5000000,500000,4,Production,Factory A,Active,2024-06-01
INV012,Safety Equipment,2024-02-01,200,25000,0,0,Production,Warehouse 1,In Stock,2024-05-15
"""

#1. 데이터 불러오기 및 개요 확인
df = pd.read_csv(StringIO(asset_inventory_data))
print("\n ----- 1. 데이터 불러오기 및 개요 확인 ----- ")
print(df.head())
df.info()

#2. 자산 유형별 총장부가액 계산
df["Book Value"] = df["Quantity"] * df["Unit_Cost"]
df_grouped = df.groupby("Asset_Type").sum()
df_sorted = df_grouped.sort_values(by="Book Value", ascending=False)
print("\n ----- 2. 자산 유형별 총장부가액 계산 ----- ")
print(df_sorted)

#3. 부서별 자산 현황 분석
df_fa = df[df["Asset_Type"].str.startswith("FA")]
df_fa["Acquisition_Cost"] = df_fa["Quantity"] * df_fa["Unit_Cost"]
dept_cost = df_fa.groupby("Department")["Acquisition_Cost"].sum()

plt.figure(figsize=(10, 6))
bars = plt.bar(dept_cost.index, dept_cost.values, color='skyblue')
plt.title("Department Total Acquisition Cost", fontsize=14)
plt.xlabel("Department")
plt.ylabel("Acquisition Cost")
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + yval*0.01, f'{yval:,.0f}', ha='center', va='bottom')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#4. 감가상각 계산 및 시각화
today = pd.Timestamp("2025-07-28")
df["Acquisition_Date"] = pd.to_datetime(df["Acquisition_Date"])
df_dep = df[df["Asset_Type"].str.startswith("FA")].copy()
df_dep["Annual_Depreciation"] = (df_dep["Unit_Cost"] - df_dep["Salvage_Value"]) / df_dep["Useful_Life_Years"]
df_dep["Monthly_Depreciation"] = df_dep["Annual_Depreciation"] / 12
df_dep["Elapsed_Months"] = ((today - df_dep["Acquisition_Date"]).dt.days / 30.44).clip(lower=0).astype(int)
df_dep["Accumulated_Depreciation"] = df_dep["Monthly_Depreciation"] * df_dep["Elapsed_Months"]
df_dep["Max_Depreciation"] = df_dep["Unit_Cost"] - df_dep["Salvage_Value"]
df_dep["Accumulated_Depreciation"] = df_dep[["Accumulated_Depreciation", "Max_Depreciation"]].min(axis=1)
top5 = df_dep.sort_values(by="Accumulated_Depreciation", ascending=False).head(5)

plt.figure(figsize=(10, 6))
bars = plt.bar(top5["Asset_ID"], top5["Accumulated_Depreciation"], color='orange')
plt.title("Top 5 FA Accumulated_Depreciation (2025-07-28)", fontsize=14)
plt.xlabel("Asset ID")
plt.ylabel("Accumulated_Depreciation")

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + yval*0.01, f'{yval:,.0f}', ha='center', va='bottom')

plt.tight_layout()
plt.show()


