# **Day 8 : 실전 모의고사 1회: 데이터 처리 및 정제**

#### **1. 학습 목표**

* Pandas 기능을 종합하여 실제 데이터 처리 문제를 해결하는 능력을 강화합니다.
* 데이터 불러오기, 결측치 처리, 데이터 타입 변환, 다중 조건 필터링, 데이터 집계 등 Pandas 핵심 기능을 복합적으로 활용합니다.
* 문제 해결 전략을 스스로 수립하고, 효율적인 코드를 작성하는 연습을 합니다.

#### **2. 문제 시나리오**

여러 부서에서 취합된 자산 및 재고 현황 데이터(`asset_inventory_data.csv`)를 기반으로 다음과 같은 분석을 수행해야 합니다.

* **원본 파일:** `asset_inventory_data.csv`
* **문제:** 자산 관리 데이터를 분석하여 특정 조건에 맞는 자산을 식별하고, 각 부서의 자산 가치를 평가한 후, 최종 분석 결과를 CSV 파일로 저장하시오.

#### **3. 요구사항 (수행 태스크)**

1.  **데이터 불러오기 및 기본 정보 확인:** `asset_inventory_data.csv` 파일을 Pandas DataFrame으로 불러오고, `df.info()`와 `df.head()`를 사용하여 기본 정보를 확인합니다.
2.  **데이터 전처리 및 정제:**
    * `Status` 컬럼의 결측치를 `'Unknown'`으로 채웁니다.
    * `Acquisition_Date`와 `Last_Audit_Date` 컬럼을 `datetime` 형식으로 변환합니다.
    * `Book_Value` (장부가액) 컬럼을 새로 생성합니다. (`(Unit_Cost - Salvage_Value) * Quantity` 공식 사용)
    * `Useful_Life_Years`가 0보다 크면 `'Depreciating'`, 그렇지 않으면 `'Non-Depreciating'` 값을 가지는 `Depreciation_Status` 컬럼을 생성합니다.
3.  **데이터 분석 및 필터링:**
    * 다음 세 가지 조건을 모두 만족하는 행만 추출합니다.
        * `Status`가 `'Active'`인 자산
        * `Acquisition_Date`가 **2023년 1월 1일 이후**인 자산
        * `Book_Value`가 **100,000,000(1억원) 이상**인 자산
4.  **데이터 집계 및 요약:**
    * 위의 필터링 조건을 통과한 자산들을 대상으로, **`Department`별로 `Book_Value`의 총합을 계산**합니다.
5.  **최종 결과 저장:**
    * 집계된 결과를 `department_book_value_summary.csv` 파일로 저장합니다.
  
[**전체 코딩 보러가기**](https://github.com/xvmon234-ai/Learning-Python/blob/main/CPA%20/my_learing_python%20/Day%208/solutions/coding.py)

[**추가 학습 보러가기**](https://github.com/xvmon234-ai/Learning-Python/blob/main/CPA%20/my_learing_python%20/Day%208/further_study/study.py)
