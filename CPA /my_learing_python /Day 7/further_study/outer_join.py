# ==============================================================================
# [Day 7 추가 학습] pd.merge()의 Outer Join과 공인회계사 업무의 연관성
# ==============================================================================

import pandas as pd

"""
💡 Outer Join의 기본 개념 💡

`pd.merge()`에서 `how='outer'`를 사용하는 `outer join`은 두 DataFrame의 모든 레코드를 포함하여 병합합니다.
즉, 왼쪽 DataFrame에만 존재하는 키, 오른쪽 DataFrame에만 존재하는 키, 그리고 양쪽에 모두 존재하는 키를 가진 레코드들이 모두 최종 결과에 포함됩니다.
일치하는 키가 없는 경우에는 해당 DataFrame의 다른 열들은 `NaN` (Not a Number) 값으로 채워집니다.

이는 `inner join`이 '공통된' 정보만을 추출하는 것과 달리, `outer join`은 '전체적인 그림'을 보고자 할 때 유용합니다.
"""

# --- 공인회계사(CPA) 데이터 분석 업무와 Outer Join의 연관성 ---

"""
공인회계사가 데이터를 분석하는 업무에서 `outer join`은 특히 데이터의 '완전성(Completeness)'과 '정합성(Reconciliation)'을 검증하는 데 매우 중요한 역할을 합니다.

1.  **데이터 완전성 검증 (Completeness Testing)**:
    * 특정 기간의 모든 거래나 모든 자산/부채가 적절히 기록되었는지 확인할 때 사용됩니다.
    * 예를 들어, 모든 구매 주문서(PO)가 실제 송장(Invoice)으로 연결되었는지, 또는 모든 판매 계약이 매출로 인식되었는지 등을 검증합니다.
    * 누락된 거래나 기록되지 않은 항목을 찾아낼 때 효과적입니다.

2.  **계정 간 대사 (Account Reconciliation)**:
    * 두 개 이상의 시스템 또는 보고서 간의 불일치(discrepancy)를 식별할 때 유용합니다.
    * 예를 들어, 은행 계정 명세서와 회사 내부 현금 계정 장부를 대사하거나, 총계정원장(GL)과 보조장부(Sub-ledger)의 잔액을 대사할 때 사용됩니다.
    * 양쪽 모두에 없는 거래(오류), 한쪽에만 있는 거래(누락 또는 잘못된 기록)를 명확히 보여줍니다.

3.  **마스터 데이터 관리 및 불일치 식별**:
    * 고객, 공급업체, 제품 등 마스터 데이터의 일관성을 유지하고, 서로 다른 시스템에 등록된 마스터 데이터 간의 불일치를 식별하는 데 사용됩니다.
    * 예를 들어, ERP 시스템의 공급업체 목록과 구매 시스템의 공급업체 목록을 대사하여, 한쪽에만 등록된 공급업체를 찾아내고 그 원인을 분석합니다.

4.  **예외 사항 및 이상 거래 탐지**:
    * 특정 기준을 벗어나는 예외적인 거래나, 정의된 패턴에 맞지 않는 이상 거래를 찾아낼 때 도움이 됩니다.
    * `outer join`을 통해 매칭되지 않는 레코드들을 식별하고, 해당 레코드에 대한 추가적인 조사를 수행하여 잠재적인 부정 또는 오류를 탐지합니다.
"""

# --- Outer Join 실제 적용 예시 (CPA 업무 시나리오) ---

# 예시 1: 은행 계정 명세서와 회사 장부 대사 (Reconciliation)
print("--- 예시 1: 은행 계정 명세서와 회사 장부 대사 ---")

# 가상 은행 명세서 데이터
bank_stmt = pd.DataFrame({
    'TransactionID_Bank': ['B001', 'B002', 'B003', 'B004'],
    'Date': ['2024-06-01', '2024-06-02', '2024-06-03', '2024-06-04'],
    'Amount': [1000, -200, 500, -150],
    'Description_Bank': ['Deposit', 'Withdrawal', 'Deposit', 'Fee']
})

# 가상 회사 장부 데이터
company_ledger = pd.DataFrame({
    'TransactionID_Ledger': ['L001', 'L002', 'L003', 'L005'], # L005는 은행 명세서에 없음 (미수금 등)
    'Date': ['2024-06-01', '2024-06-02', '2024-06-03', '2024-06-05'],
    'Amount': [1000, -200, 500, 300],
    'Description_Ledger': ['Sales Rev', 'Exp Payment', 'Loan', 'Other Income']
})

print("\n은행 명세서 (bank_stmt):\n", bank_stmt)
print("\n회사 장부 (company_ledger):\n", company_ledger)

# TransactionID가 명시적으로 동일하지 않으므로, Date와 Amount를 기준으로 대사한다고 가정
# 실제 상황에서는 더 복잡한 매칭 로직이 필요할 수 있습니다.
# 여기서는 예시를 위해 단순화합니다.
reconciliation_df = pd.merge(
    bank_stmt,
    company_ledger,
    left_on=['Date', 'Amount'], # 은행 명세서 기준 매칭
    right_on=['Date', 'Amount'], # 회사 장부 기준 매칭
    how='outer', # 양쪽에 존재하는 모든 거래를 확인
    suffixes=('_Bank', '_Ledger') # 컬럼명 충돌 방지
)

print("\n--- 은행 명세서와 회사 장부 Outer Join 결과 (대사 결과) ---")
print(reconciliation_df)

"""
➡️ 분석:
* `reconciliation_df`를 보면, 'TransactionID_Bank'와 'TransactionID_Ledger' 중 한쪽만 값이 있고 다른 쪽은 `NaN`인 행들이 있습니다.
* 예시에서 B004 (은행 수수료 -150)는 회사 장부에 없으므로 `Description_Ledger` 등이 `NaN`으로 나옵니다.
* L005 (회사 장부의 Other Income 300)는 은행 명세서에 없으므로 `Description_Bank` 등이 `NaN`으로 나옵니다.
* CPA는 이 `NaN`이 포함된 행들을 집중적으로 검토하여, 누락된 기록이 있는지, 시점 차이(Timing Differences)인지, 아니면 실제 불일치인지 원인을 파악합니다.
"""

print("\n" + "="*80 + "\n")

# 예시 2: 공급업체 마스터 데이터 일관성 검증 (Master Data Integrity)
print("--- 예시 2: 공급업체 마스터 데이터 일관성 검증 ---")

# ERP 시스템의 공급업체 목록
erp_vendors = pd.DataFrame({
    'VendorID': ['V001', 'V002', 'V003', 'V004'],
    'VendorName_ERP': ['Supplier A', 'Supplier B', 'Supplier C', 'Supplier D'],
    'Status_ERP': ['Active', 'Active', 'Inactive', 'Active']
})

# 구매 시스템의 공급업체 목록
purchase_vendors = pd.DataFrame({
    'VendorID': ['V001', 'V002', 'V005', 'V004'], # V005는 ERP에 없음 (신규 등록 예정/오류)
    'VendorName_Purchase': ['Supplier A', 'Supplier B', 'New Vendor E', 'Supplier D'],
    'Contact_Purchase': ['john@a.com', 'jane@b.com', 'mike@e.com', 'sarah@d.com']
})

print("\nERP 공급업체 (erp_vendors):\n", erp_vendors)
print("\n구매 시스템 공급업체 (purchase_vendors):\n", purchase_vendors)

# VendorID를 기준으로 outer join
vendor_master_check = pd.merge(
    erp_vendors,
    purchase_vendors,
    on='VendorID',
    how='outer'
)

print("\n--- 공급업체 마스터 데이터 Outer Join 결과 ---")
print(vendor_master_check)

"""
➡️ 분석:
* 'V003'은 ERP에만 있고 구매 시스템에는 없습니다. (Inactive라서 구매 활동이 없거나, 구매 시스템에 누락)
* 'V005'는 구매 시스템에만 있고 ERP에는 없습니다. (ERP에 등록되지 않은 신규 공급업체이거나, 잘못 등록된 공급업체)
* CPA는 이러한 불일치(NaN이 있는 행)를 통해 마스터 데이터의 정합성을 확인하고, 관리 절차가 적절히 지켜지고 있는지, 또는 시스템 간 동기화 문제가 없는지 등을 감사할 수 있습니다.
"""

print("\n" + "="*80 + "\n")

# 예시 3: 프로젝트별 예산 및 실제 비용 비교 (Gap Analysis)
print("--- 예시 3: 프로젝트별 예산 및 실제 비용 비교 ---")

# 프로젝트 예산 데이터
project_budget = pd.DataFrame({
    'ProjectID': ['P001', 'P002', 'P003'],
    'BudgetedAmount': [10000, 15000, 8000],
    'BudgetCategory': ['Development', 'Marketing', 'Admin']
})

# 프로젝트 실제 비용 데이터
project_actuals = pd.DataFrame({
    'ProjectID': ['P001', 'P002', 'P004'], # P004는 예산에 없음 (예산 외 지출/누락)
    'ActualAmount': [9500, 16000, 2000],
    'ActualCategory': ['Dev', 'Mkt', 'Sales']
})

print("\n프로젝트 예산 (project_budget):\n", project_budget)
print("\n프로젝트 실제 비용 (project_actuals):\n", project_actuals)

# ProjectID를 기준으로 outer join
budget_actuals_comparison = pd.merge(
    project_budget,
    project_actuals,
    on='ProjectID',
    how='outer'
)

print("\n--- 프로젝트 예산과 실제 비용 Outer Join 결과 ---")
print(budget_actuals_comparison)

"""
➡️ 분석:
* 'P003'은 예산은 있지만 실제 비용 기록이 없습니다. (아직 비용 발생 전이거나, 기록 누락)
* 'P004'는 실제 비용은 발생했지만 예산에 없는 프로젝트입니다. (예산 통제 위반 또는 비상 지출)
* CPA는 `outer join` 결과를 바탕으로 예산 대비 실적을 분석하고, 예산 외 지출, 미집행 예산, 비용 누락 등의 감사 포인트를 식별할 수 있습니다.
* 여기서 `fill_value=0` 등을 활용하여 `NaN`을 0으로 채운 후 차이를 계산하면 더 직관적인 분석이 가능합니다.
"""
