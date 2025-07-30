# 삼일회계법인 신입공인회계사 디지털 전형 과제 면접 - 2일차 1회차

본 문서는 삼일회계법인 신입공인회계사 디지털 전형의 정식 과제 면접 중 **2일차 1회차 과제**에 대한 내용을 담고 있습니다.

## 과제 개요

재무 컨설팅 팀 소속 공인회계사로서, 고객사의 월별 손익계산서(Income Statement) 데이터를 자동화하여 생성하고, 주요 계정 과목의 변동을 분석하며, 데이터 불일치(Inconsistency)를 검증하는 스크립트를 개발하는 과제입니다. 특히, 매출액과 매출원가의 관계, 그리고 특정 비용 항목의 급격한 변동을 식별하는 데 중점을 둡니다.

  * **주제:** 재무 보고서 자동화 및 데이터 검증 (가상 시나리오)
  * **준비 시간:** 5분 (문제 분석)
  * **풀이 시간:** 20분 (AI 활용 가능, GPT 적극 활용 권장)
  * **질의 시간:** 10\~15분 (수행 과제에 대한 면접관 질의)

## 제공 데이터: `general_ledger_transactions.csv`

다음은 과제 수행에 사용될 가상의 고객사 거래 데이터입니다. 이 데이터를 CSV 파일로 저장하거나, Pandas의 `StringIO` 등을 활용하여 DataFrame으로 불러와 사용하십시오.

```csv
Transaction_ID,Date,Account_Code,Account_Name,Debit,Credit,Description
T001,2024-01-05,4010,Sales Revenue,,10000000,Product A Sales
T002,2024-01-05,1110,Cash,10000000,,Cash from Sales
T003,2024-01-10,5010,Cost of Goods Sold,6000000,,COGS for Product A
T004,2024-01-10,1130,Inventory,,6000000,Inventory Reduction
T005,2024-01-15,4010,Sales Revenue,,8000000,Product B Sales
T006,2024-01-15,1110,Cash,8000000,,Cash from Sales
T007,2024-01-20,5010,Cost of Goods Sold,5000000,,COGS for Product B
T008,2024-01-20,1130,Inventory,,5000000,Inventory Reduction
T009,2024-01-25,6010,Rent Expense,2000000,,January Rent
T010,2024-01-25,1110,Cash,,2000000,Cash for Rent
T011,2024-02-05,4010,Sales Revenue,,12000000,Product C Sales
T012,2024-02-05,1110,Cash,12000000,,Cash from Sales
T013,2024-02-10,5010,Cost of Goods Sold,7000000,,COGS for Product C
T014,2024-02-10,1130,Inventory,,7000000,Inventory Reduction
T015,2024-02-15,4010,Sales Revenue,,9000000,Product D Sales
T016,2024-02-15,1110,Cash,9000000,,Cash from Sales
T017,2024-02-20,5010,Cost of Goods Sold,5500000,,COGS for Product D
T018,2024-02-20,1130,Inventory,,5500000,Inventory Reduction
T019,2024-02-25,6010,Rent Expense,2000000,,February Rent
T020,2024-02-25,1110,Cash,,2000000,Cash for Rent
T021,2024-03-05,4010,Sales Revenue,,15000000,Product E Sales
T022,2024-03-05,1110,Cash,15000000,,Cash from Sales
T023,2024-03-10,5010,Cost of Goods Sold,8000000,,COGS for Product E
T024,2024-03-10,1130,Inventory,,8000000,Inventory Reduction
T025,2024-03-15,4010,Sales Revenue,,10000000,Product F Sales
T026,2024-03-15,1110,Cash,10000000,,Cash from Sales
T027,2024-03-20,5010,Cost of Goods Sold,6000000,,COGS for Product F
T028,2024-03-20,1130,Inventory,,6000000,Inventory Reduction
T029,2024-03-25,6010,Rent Expense,2000000,,March Rent
T030,2024-03-25,1110,Cash,,2000000,Cash for Rent
T031,2024-04-05,4010,Sales Revenue,,18000000,Product G Sales
T032,2024-04-05,1110,Cash,18000000,,Cash from Sales
T033,2024-04-10,5010,Cost of Goods Sold,10000000,,COGS for Product G
T034,2024-04-10,1130,Inventory,,10000000,Inventory Reduction
T035,2024-04-15,4010,Sales Revenue,,12000000,Product H Sales
T036,2024-04-15,1110,Cash,12000000,,Cash from Sales
T037,2024-04-20,5010,Cost of Goods Sold,7000000,,COGS for Product H
T038,2024-04-20,1130,Inventory,,7000000,Inventory Reduction
T039,2024-04-25,6010,Rent Expense,2000000,,April Rent
T040,2024-04-25,1110,Cash,,2000000,Cash for Rent
```

## 과제 요구사항

주어진 `general_ledger_transactions.csv` 파일을 사용하여 다음의 과제를 수행하는 Python 스크립트를 작성하십시오.

1.  **데이터 불러오기 및 전처리:**
      * `general_ledger_transactions.csv` 파일을 불러와 DataFrame으로 변환하세요.
      * `Date` 컬럼을 날짜/시간 형식(`datetime`)으로 변환하고, 이를 사용하여 **'Month'** (월: 예: 'YYYY-MM' 형식) 컬럼을 새로 추가하세요.
      * `Debit`과 `Credit` 컬럼의 결측값(NaN)을 0으로 처리하세요.
2.  **월별 손익계산서 요약 (매출액, 매출원가, 매출총이익, 특정 비용):**
      * 각 **'Month'별로 다음 계정 과목의 합계**를 계산하여 출력하세요:
          * **매출액 (Sales Revenue - 계정코드 4010)**: Credit 합계
          * **매출원가 (Cost of Goods Sold - 계정코드 5010)**: Debit 합계
          * **매출총이익 (Gross Profit)**: 매출액 - 매출원가
          * **임차료 (Rent Expense - 계정코드 6010)**: Debit 합계
      * 결과는 월별로 정렬하여 출력하세요.
3.  **총계정원장 대차 평균 일치 검증:**
      * 전체 거래에서 `Debit` 컬럼의 총합과 `Credit` 컬럼의 총합이 일치하는지 확인하는 검증 로직을 작성하고, 그 결과를 출력하세요. (회계의 대차 평균 원리 검증)
      * 만약 일치하지 않는다면, 불일치 금액을 함께 출력하세요.
4.  **주요 계정 과목 변동률 분석 및 이상 징후 식별:**
      * \*\*월별 매출총이익률 (Gross Profit Margin)\*\*을 계산하고 출력하세요. (매출총이익 / 매출액)
      * 전월 대비 **매출총이익률이 5%p(퍼센트포인트) 이상 변동**한 월을 찾아 출력하세요.
      * 전월 대비 **'Rent Expense'가 10% 이상 변동**한 월을 찾아 출력하고, 해당 변동이 일반적이지 않음을 설명하세요. (변동률 = (당월 금액 - 전월 금액) / 전월 금액 \* 100)

## 질의 내용

과제 제출 완료 후, 면접관이 아래 질문들을 기반으로 질의응답을 진행할 예정입니다.

### 면접관 (프로그래밍 개발자)

1.  요구사항 2에서 월별 손익계산서 요약을 위해 `df.groupby('Month').apply(lambda x: pd.Series(...))` 방식을 사용했습니다. 이 방식은 유연하지만, 특정 경우에는 성능상의 오버헤드가 발생할 수 있습니다. 만약 처리해야 할 거래 데이터가 수백만 건 이상으로 매우 크다면, 이 `apply` 대신 어떤 Pandas 기능이나 다른 접근 방식을 고려할 수 있을까요? (예: `pivot_table`, 여러 `groupby().sum()` 결과를 병합 등)
2.  총계정원장 대차 평균 일치 검증 로직을 작성했습니다. 만약 대차 불일치가 발생했을 때, 스크립트가 단순히 차액을 출력하는 것을 넘어, 불일치의 원인이 될 수 있는 \*\*특정 거래(Transaction\_ID)\*\*를 자동으로 식별하거나, 불일치가 발생하는 **계정 코드**를 찾아내는 로직을 추가하려면 어떻게 코드를 개선할 수 있을까요?

### 면접관 (회계사)

3.  월별 매출총이익률 변동(특히 5%p 이상)과 임차료 변동(10% 이상)을 이상 징후로 식별했습니다. 회계 감사 관점에서 이러한 주요 손익 계정의 변동이 의미하는 바는 무엇이며, 실제로 감사 과정에서 이러한 변동이 탐지되었을 때 어떤 추가적인 감사 절차를 계획하고 수행해야 할까요?
4.  총계정원장의 대차 평균 일치 검증은 회계의 가장 기본적인 원칙입니다. 만약 이 검증에서 불일치가 발생했다면, 이는 재무 보고서의 신뢰성에 어떤 영향을 미치며, 감사인은 이를 어떻게 평가하고 어떤 조치를 취해야 할까요?

-----
