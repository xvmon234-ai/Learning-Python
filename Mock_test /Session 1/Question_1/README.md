# 삼일회계법인 신입공인회계사 디지털 전형 과제 면접 - 1일차 1회차 (정식 과제)

본 문서는 삼일회계법인 신입공인회계사 디지털 전형의 정식 과제 면접 중 **1일차 1회차 과제**에 대한 내용을 담고 있습니다.

## 과제 개요

회계 법인에서 매달 반복적으로 수행되는 재무 보고서의 데이터 취합 및 정규화 작업을 자동화하는 과제입니다. 특히, 여러 부서에서 각기 다른 형식으로 제출되는 비용 보고서 데이터를 통일된 형식으로 정리하는 스크립트 작성을 목표로 합니다.

  * **주제:** 자동화 스크립트 작성
  * **준비 시간:** 5분 (문제 분석)
  * **풀이 시간:** 20분 (AI 활용 가능, GPT 적극 활용 권장)
  * **질의 시간:** 10\~15분 (수행 과제에 대한 면접관 질의)

## 제공 데이터

과제 수행에 사용될 가상의 비용 보고서 데이터입니다. 이 내용을 사용하여 `department_A_expenses.csv`와 `department_B_expenditures.csv` 두 개의 파일을 생성하거나, Pandas의 `StringIO` 등을 활용하여 DataFrame으로 불러와 사용하십시오.

### `department_A_expenses.csv`

```csv
Date,Description,Amount,Category
2025-06-01,Office Supplies,15000,Administrative
2025-06-05,Client Dinner,80000,Entertainment
2025-06-10,Software License Renewal,500000,IT
2025-06-15,Travel Expense,120000,Travel
2025-06-20,Consulting Fee,300000,Professional Service
```

### `department_B_expenditures.csv`

```csv
Transaction_Date,Item_Description,Cost,Expense_Type
2025-06-03,Marketing Campaign,200000,Marketing
2025-06-08,Utility Bill,75000,Utilities
2025-06-12,Hardware Purchase,150000,IT
2025-06-18,Seminar Registration,90000,Training
2025-06-22,Rent,250000,Rent
```

## 과제 요구사항

주어진 CSV 파일들을 사용하여 다음의 과제를 수행하는 Python 스크립트를 작성하십시오.

1.  **두 CSV 파일 불러오기:** 제공된 `department_A_expenses.csv`와 `department_B_expenditures.csv` 파일을 각각 Pandas DataFrame으로 불러오세요.
2.  **컬럼명 통일:** 두 DataFrame의 컬럼명을 다음 표준 형식으로 통일하여 병합 가능한 형태로 만드세요.
      * `Date` (날짜)
      * `Description` (내용)
      * `Amount` (금액)
      * `Category` (비용 항목)
      * **참고:** `department_B_expenditures.csv`의 컬럼명(`Transaction_Date`, `Item_Description`, `Cost`, `Expense_Type`)을 위 통일된 컬럼명으로 변경해야 합니다.
3.  **데이터 병합:** 컬럼명이 통일된 두 DataFrame을 하나의 통합된 DataFrame으로 병합하세요.
4.  **`Amount` 컬럼 데이터 타입 변환:** `Amount` 컬럼이 숫자형(예: int 또는 float)으로 정확히 인식되도록 변환하세요.
5.  **`Date` 컬럼 날짜 형식 변환:** `Date` 컬럼이 날짜 형식(`YYYY-MM-DD`)으로 정확히 인식되도록 변환하세요.
6.  **특정 비용 항목 분류 및 집계:**
      * 통합된 데이터에서 **'IT' 및 'Travel' 카테고리**에 해당하는 비용만 필터링하세요.
      * 필터링된 데이터를 `Category`별로 그룹화하여 총 금액을 집계하고, 결과를 내림차순으로 출력하세요.
7.  **결과 CSV 파일로 저장:** 최종적으로 통합되고 처리된 데이터를 `monthly_expenses_report_202506.csv`라는 이름의 새 CSV 파일로 저장하세요. 이 파일에는 `Date`, `Description`, `Amount`, `Category` 컬럼만 포함되어야 합니다.


[**전체 코딩 보러가기**](https://github.com/xvmon234-ai/Learning-Python/blob/main/Mock_test%20/Session%201/Question_1/solutions/coding.py)


## 질의 내용

과제 제출 완료 후, 면접관이 아래 질문들을 기반으로 질의응답을 진행할 예정입니다.

### 면접관 (프로그래밍 개발자)

1.  두 개의 DataFrame을 병합할 때 `pd.concat`을 사용했습니다. `pd.concat` 외에 DataFrame을 병합하는 다른 방법(예: `pd.merge`)이 있는데, 이 과제에서는 왜 `pd.concat`을 선택했습니까? 그리고 `pd.concat`과 `pd.merge`의 주요 차이점은 무엇이라고 생각합니까?
2.  데이터를 CSV 파일로 저장할 때 `index=False` 옵션을 사용했습니다. 이 옵션의 역할은 무엇이며, 이를 생략했을 때 발생할 수 있는 잠재적인 문제점은 무엇일까요?

### 면접관 (회계사)

3.  다른 부서에서 제출된 비용 보고서의 컬럼명이 다른 경우를 처리했습니다. 실제 업무 환경에서 이처럼 데이터 형식이 통일되지 않을 때 발생할 수 있는 회계 실무적 문제점은 무엇이며, 이를 방지하기 위한 통제 방안은 무엇이 있을까요?
4.  'IT' 및 'Travel' 카테고리의 비용을 필터링하고 집계했습니다. 만약 여러 부서의 비용 데이터가 통합된 상황에서, 특정 부서의 'IT' 비용만 추가적으로 분석해야 한다면 어떤 방식으로 데이터를 필터링하고 집계할 수 있을까요?


[**전체 질의응답 보러가기**](https://github.com/xvmon234-ai/Learning-Python/blob/main/Mock_test%20/Session%201/Question_1/solutions/qa.py)

-----
