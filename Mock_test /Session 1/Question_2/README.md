# 삼일회계법인 신입공인회계사 디지털 전형 과제 면접 - 1일차 2회차

본 문서는 삼일회계법인 신입공인회계사 디지털 전형의 정식 과제 면접 중 **1일차 2회차 과제**에 대한 내용을 담고 있습니다.

## 과제 개요

제조 기업의 월별 판매 데이터를 분석하여 매출 추이와 제품별 기여도를 파악하고, 주요 재무 의사결정을 위한 시각화 자료를 작성하는 과제입니다.

  * **주제:** 데이터 분석 및 시각화
  * **준비 시간:** 5분 (문제 분석)
  * **풀이 시간:** 20분 (AI 활용 가능, GPT 적극 활용 권장)
  * **질의 시간:** 10\~15분 (수행 과제에 대한 면접관 질의)

### 제공 데이터: `monthly_sales_data.csv`

다음은 과제 수행에 사용될 가상의 월별 제품 판매 데이터입니다. 이 데이터를 CSV 파일로 저장하거나, Pandas의 `StringIO` 등을 활용하여 DataFrame으로 불러와 사용하십시오.

```csv
Sale_Date,Product_Category,Product_Name,Quantity_Sold,Unit_Price,Region
2023-01-10,Electronics,Smartphone,150,800000,North
2023-01-15,Apparel,T-Shirt,500,25000,South
2023-01-20,Home Goods,Blender,80,120000,East
2023-02-05,Electronics,Laptop,100,1500000,North
2023-02-10,Apparel,Jeans,300,50000,West
2023-02-18,Home Goods,Coffee Maker,120,70000,South
2023-03-01,Electronics,Tablet,200,600000,East
2023-03-08,Apparel,Hoodie,400,35000,North
2023-03-12,Home Goods,Vacuum Cleaner,70,200000,West
2023-04-03,Electronics,Smartwatch,250,300000,South
2023-04-09,Apparel,Dress,150,60000,East
2023-04-14,Home Goods,Air Fryer,90,100000,North
2023-05-01,Electronics,Headphones,300,100000,West
2023-05-07,Apparel,Jacket,100,100000,South
2023-05-11,Home Goods,Toaster,180,40000,East
2023-06-02,Electronics,Gaming Console,80,700000,North
2023-06-09,Apparel,Shorts,600,20000,West
2023-06-16,Home Goods,Microwave,110,150000,South
2023-07-05,Electronics,Camera,70,400000,East
2023-07-12,Apparel,Skirt,250,30000,North
2023-07-19,Home Goods,Dishwasher,50,600000,West
2023-08-01,Electronics,Drone,60,900000,South
2023-08-08,Apparel,Sweater,350,45000,East
2023-08-15,Home Goods,Refrigerator,30,800000,North
2023-09-03,Electronics,VR Headset,90,500000,West
2023-09-10,Apparel,Pants,450,40000,South
2023-09-17,Home Goods,Washing Machine,40,700000,East
2023-10-01,Electronics,E-Reader,200,150000,North
2023-10-08,Apparel,Socks,800,10000,West
2023-10-15,Home Goods,Oven,60,300000,South
2023-11-04,Electronics,Projector,40,250000,East
2023-11-11,Apparel,Gloves,200,15000,North
2023-11-18,Home Goods,Heater,100,90000,West
2023-12-01,Electronics,Smart TV,120,1200000,South
2023-12-08,Apparel,Scarf,300,20000,East
2023-12-15,Home Goods,Robot Vacuum,70,400000,North
2024-01-10,Electronics,Smartphone,180,800000,North
2024-01-15,Apparel,T-Shirt,600,25000,South
2024-01-20,Home Goods,Blender,90,120000,East
2024-02-05,Electronics,Laptop,110,1500000,North
2024-02-10,Apparel,Jeans,350,50000,West
2024-02-18,Home Goods,Coffee Maker,130,70000,South
2024-03-01,Electronics,Tablet,220,600000,East
2024-03-08,Apparel,Hoodie,450,35000,North
2024-03-12,Home Goods,Vacuum Cleaner,75,200000,West
2024-04-03,Electronics,Smartwatch,270,300000,South
2024-04-09,Apparel,Dress,160,60000,East
2024-04-14,Home Goods,Air Fryer,95,100000,North
2024-05-01,Electronics,Headphones,320,100000,West
2024-05-07,Apparel,Jacket,110,100000,South
2024-05-11,Home Goods,Toaster,200,40000,East
2024-06-02,Electronics,Gaming Console,85,700000,North
2024-06-09,Apparel,Shorts,650,20000,West
2024-06-16,Home Goods,Microwave,120,150000,South
2024-07-05,Electronics,Camera,75,400000,East
2024-07-12,Apparel,Skirt,280,30000,North
2024-07-19,Home Goods,Dishwasher,55,600000,West
2024-08-01,Electronics,Drone,65,900000,South
2024-08-08,Apparel,Sweater,380,45000,East
2024-08-15,Home Goods,Refrigerator,33,800000,North
2024-09-03,Electronics,VR Headset,95,500000,West
2024-09-10,Apparel,Pants,480,40000,South
2024-09-17,Home Goods,Washing Machine,42,700000,East
2024-10-01,Electronics,E-Reader,220,150000,North
2024-10-08,Apparel,Socks,850,10000,West
2024-10-15,Home Goods,Oven,65,300000,South
2024-11-04,Electronics,Projector,45,250000,East
2024-11-11,Apparel,Gloves,220,15000,North
2024-11-18,Home Goods,Heater,110,90000,West
2024-12-01,Electronics,Smart TV,130,1200000,South
2024-12-08,Apparel,Scarf,320,20000,East
2024-12-15,Home Goods,Robot Vacuum,75,400000,North
```

## 과제 요구사항

주어진 `monthly_sales_data.csv` 파일을 사용하여 다음의 과제를 수행하는 Python 스크립트를 작성하십시오.

1.  **데이터 불러오기 및 전처리:**
      * `monthly_sales_data.csv` 파일을 불러와 DataFrame으로 변환하세요.
      * `Sale_Date` 컬럼을 날짜/시간 형식(`datetime`)으로 변환하고, 이를 사용하여 **'Sales\_Month'** (월별: 예: 'YYYY-MM' 형식) 컬럼을 새로 추가하세요.
      * **'Total\_Revenue'** (총 매출액: `Quantity_Sold * Unit_Price`) 컬럼을 새로 추가하세요.
2.  **월별 총 매출액 추이 분석 및 시각화:**
      * **'Sales\_Month'별로 'Total\_Revenue'의 합계**를 계산하고, 그 결과를 오름차순(시간 순서)으로 정렬하여 출력하세요.
      * 계산된 월별 총 매출액 추이를 \*\*꺾은선 그래프(Line Chart)\*\*로 시각화하세요. x축은 월, y축은 총 매출액으로 설정하고, 적절한 제목과 축 레이블을 포함하세요.
3.  **제품 카테고리별 매출 기여도 분석 및 시각화:**
      * **'Product\_Category'별로 'Total\_Revenue'의 총합**을 계산하고, 각 카테고리가 전체 매출에서 차지하는 **비율**을 계산하여 내림차순으로 출력하세요.
      * 계산된 제품 카테고리별 매출 기여도(총합 또는 비율)를 \*\*파이 차트(Pie Chart)\*\*로 시각화하세요. 각 카테고리의 이름과 비율을 명확하게 표시하고, 적절한 제목을 포함하세요.
4.  **지역별 상위 3개 제품 카테고리 분석:**
      * 각 `Region` (지역)별로 `Product_Category`의 'Total\_Revenue' 합계를 계산하고, 각 지역 내에서 \*\*매출이 가장 높은 상위 3개 `Product_Category`\*\*를 출력하세요. (예: North 지역의 상위 3개 카테고리, South 지역의 상위 3개 카테고리 등)


[**정답 코드 보러가기**](https://github.com/xvmon234-ai/Learning-Python/blob/main/Mock_test%20/Session%201/Question_2/solutions/coding.py)


## 질의 내용

과제 제출 완료 후, 면접관이 아래 질문들을 기반으로 질의응답을 진행할 예정입니다.

### 면접관 (프로그래밍 개발자)

1.  `Sale_Date` 컬럼을 `pd.to_datetime()`으로 변환할 때 `errors='coerce'` 옵션을 사용했습니다. 이 옵션의 역할은 무엇이며, 데이터 전처리 과정에서 이와 같은 오류 처리 방식이 유용하거나, 반대로 주의해야 할 경우는 언제일까요?
2.  월별 매출 추이 시각화 시 `monthly_revenue.index.astype(str)`을 사용하여 x축 레이블을 문자열로 변환했습니다. 만약 데이터가 더 길어져 수십 년간의 월별 데이터가 있다면, 현재와 같은 방식의 x축 레이블 처리나 `xticks` 설정이 어떤 문제를 일으킬 수 있으며, 이를 개선하기 위한 `matplotlib` 활용 방안은 무엇이 있을까요?

### 면접관 (회계사)

3.  월별 매출 추이와 제품 카테고리별 매출 기여도를 시각화했습니다. 만약 경영진이 특정 월의 매출이 급격히 감소했거나, 특정 카테고리의 매출 기여도가 예상보다 낮을 때, 추가적으로 어떤 재무적 분석 지표나 시각화 방법을 활용하여 원인을 파악하고 설명할 수 있을까요?
4.  지역별 상위 3개 제품 카테고리를 분석했습니다. 이 결과를 기반으로 회계 및 재무적 관점에서 기업의 전략 수립(예: 투자, 생산 계획, 마케팅 예산 배분 등)에 어떤 도움을 줄 수 있을까요? 구체적인 예를 들어 설명해 주세요.


[**질의 응답 보러가기**](https://github.com/xvmon234-ai/Learning-Python/blob/main/Mock_test%20/Session%201/Question_2/solutions/qa.py)


-----
