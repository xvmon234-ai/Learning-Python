-----

네, 알겠습니다. 요청하신 대로 문제, 데이터프레임, 그리고 질의 내용을 `README.md` 파일 형식에 맞춰 가공하여 제공해 드리겠습니다. 이렇게 하면 GitHub 등에서 프로젝트 설명을 하듯이 과제 내용을 한눈에 파악하기 용이할 것입니다.

파이썬 코드 및 답변은 별도의 `.py` 파일로 관리하시면 됩니다.

-----

# 삼일회계법인 신입공인회계사 디지털 전형 과제 면접 - 1일차 1회차

본 문서는 삼일회계법인 신입공인회계사 디지털 전형의 과제 면접 중 **1일차 1회차 과제**에 대한 내용을 담고 있습니다.

## 과제 개요

제시된 기업의 재고 및 유형자산 데이터를 활용하여 데이터 분석 및 시각화를 수행하고, 회계적 관점에서 인사이트를 도출하는 과제입니다.

  * **주제:** 데이터 분석 및 시각화
  * **준비 시간:** 5분 (문제 분석)
  * **풀이 시간:** 20분 (AI 활용 가능, GPT 적극 활용 권장)
  * **질의 시간:** 10\~15분 (수행 과제에 대한 면접관 질의)

## 제공 데이터: `asset_inventory_data.csv`

다음은 과제 수행에 사용될 가상의 재고 및 유형자산 정보 데이터입니다. 이 데이터를 CSV 파일로 저장하거나, Pandas의 `StringIO` 등을 활용하여 DataFrame으로 불러와 사용하십시오.

```csv
Asset_ID,Asset_Type,Acquisition_Date,Quantity,Unit_Cost,Salvage_Value,Useful_Life_Years,Department,Location,Status,Last_Audit_Date
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
```

## 과제 문제

주어진 `asset_inventory_data.csv` 파일을 사용하여 다음의 과제를 수행하십시오.

1.  **데이터 불러오기 및 개요 확인:**
      * `asset_inventory_data.csv` 파일을 불러와 데이터프레임으로 변환하세요.
      * 데이터프레임의 상위 5개 행을 출력하고, 각 컬럼의 데이터 타입 및 결측치 여부를 확인하세요.
2.  **자산 유형별 총 장부가액 계산:**
      * `Asset_Type` (자산 유형)별로 현재 \*\*총 장부가액 (수량 \* 단가)\*\*을 계산하고, 그 결과를 내림차순으로 정렬하여 출력하세요. (`Asset_Type`이 'FA'로 시작하는 것은 유형자산, 'INV'로 시작하는 것은 재고로 간주합니다.)
3.  **부서별 자산 현황 분석:**
      * `Department` (부서)별로 보유하고 있는 \*\*유형자산 (Asset\_Type이 'FA'로 시작하는 자산)\*\*의 총 취득가액 (`Quantity` \* `Unit_Cost`)을 계산하고 시각화하세요.
      * 시각화는 파이 차트(Pie Chart) 또는 막대 그래프(Bar Chart) 중 적절한 것을 선택하여 작성하고, 각 부서가 차지하는 비율 또는 금액을 명확하게 표시해야 합니다.
4.  **감가상각 계산 및 시각화 (유형자산만 해당):**
      * 유형자산 (`Asset_Type`이 'FA'로 시작하는 자산)에 대해 **정액법**을 사용하여 현재 시점 (오늘 날짜: **2025년 7월 28일**)까지의 누적 감가상각액을 계산하여 새로운 컬럼으로 추가하세요.
          * 정액법 감가상각액 = (취득원가 - 잔존가치) / 내용연수
          * 현재 시점까지의 누적 감가상각액은 취득일로부터 현재까지 경과된 개월 수를 기준으로 일할 계산하여 적용합니다.
      * 누적 감가상각액이 가장 높은 상위 5개 유형자산을 막대 그래프로 시각화하고, 자산 ID와 누적 감가상각액을 명확히 표시하세요.

## 질의 내용

과제 제출 완료 후, 면접관이 아래 질문들을 기반으로 질의응답을 진행할 예정입니다.

### 면접관 (프로그래밍 개발자)

1.  경과 개월 수 계산 시 `(today - df_dep["Acquisition_Date"]).dt.days / 30.44` 방식을 사용했습니다. 이 방식의 장단점은 무엇이며, 더 정확한 월 단위 계산이 필요하다면 어떤 방법을 고려하겠습니까?
2.  DataFrame에서 특정 조건을 필터링하거나 새로운 컬럼을 추가할 때 `.copy()`를 사용했습니다. 이 `.copy()`의 역할과 중요성에 대해 설명해 주십시오.

### 면접관 (회계사)

3.  감가상각 누계액 계산 시 `df_dep[["Accumulated_Depreciation", "Max_Depreciation"]].min(axis=1)`을 사용하여 최대 감가상각액을 초과하지 않도록 했습니다. 이 로직이 회계적으로 어떤 의미를 가지며, 왜 중요하다고 생각합니까?
4.  만약 이 데이터에 새로운 자산 유형이 추가되거나, 기존 자산의 내용연수가 변경되는 등 데이터 구조나 회계 정책에 변동이 생긴다면, 작성하신 코드에서 어떤 부분을 가장 먼저 수정하거나 고려해야 합니까?

-----

이제 다음 과제(자동화 스크립트 작성)를 시작할 준비가 되셨다면 말씀해주세요.
