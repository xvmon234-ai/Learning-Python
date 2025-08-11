# Day 11: 실전 모의고사 2회: 고급 데이터 처리 및 분석

## 🎯 학습 목표

  - Pandas를 활용하여 복잡한 데이터 병합, 전처리, 분석 문제를 해결하는 능력 강화.
  - 데이터 분석 결과를 적절한 시각화와 함께 설명하고 인사이트를 도출하는 과정 숙달.

### ✔️ 오늘 할 일

  - **실전 코딩 (약 2.5시간)**:
      - `고객 구매 데이터(CSV)`와 `상품 정보 데이터(Excel)`를 병합하고 전처리하는 문제 해결.
      - 문제 파악 및 계획 수립: 5분
      - 코딩 실행: 20분
      - 문제 풀이 마무리 및 코드 최적화: 나머지 시간
  - **자기 분석 및 설명 연습 (약 1.5시간)**:
      - 해결 과정을 말로 설명하는 연습을 하고 기록합니다.
      - 각 시각화(막대 그래프, 꺾은선 그래프)를 선택한 이유와 차트를 통해 도출한 인사이트를 상세히 작성합니다.

-----

### 📝 실습 문제 및 요구사항

#### 데이터 준비

아래 코드를 실행하여 물리적인 파일 생성 없이 메모리 상에 DataFrame을 준비할 수 있습니다.

```python
import pandas as pd
import numpy as np
import io

# 1. 고객 구매 데이터 생성 (CSV 형식)
cust_data = {
    'order_id': range(101, 201),
    'customer_id': np.random.choice(range(1, 21), 100),
    'product_id': np.random.choice(range(1001, 1016), 100),
    'purchase_date': pd.to_datetime(pd.date_range(start='2024-01-01', periods=100, freq='D')),
    'quantity': np.random.randint(1, 10, 100),
}
cust_df = pd.DataFrame(cust_data)
cust_df.loc[[10, 20], 'customer_id'] = np.nan
cust_df.loc[[30, 40], 'quantity'] = -1

cust_csv = cust_df.to_csv(index=False)
cust_io = io.StringIO(cust_csv)

# 2. 상품 정보 데이터 생성 (Excel 형식)
prod_data = {
    'product_id': range(1001, 1016),
    'product_name': [f'상품_{i}' for i in range(1, 16)],
    'category': ['전자제품', '의류', '식품', '전자제품', '의류', '식품', '전자제품', '의류', '식품', '전자제품', '의류', '식품', '전자제품', '의류', '식품'],
    'price': np.random.randint(10000, 50001, 15)
}
prod_df = pd.DataFrame(prod_data)

# DataFrame을 Excel 바이너리로 변환하고 BytesIO로 래핑
prod_excel_io = io.BytesIO()
prod_df.to_excel(prod_excel_io, index=False)
prod_excel_io.seek(0) # 파일 포인터를 처음으로 이동

# StringIO/BytesIO 객체에서 DataFrame 불러오기
df_purchases = pd.read_csv(cust_io)
df_products = pd.read_excel(prod_excel_io)
```

#### 모의 문제

제공된 `df_purchases`와 `df_products`를 사용하여 다음을 수행하시오.

1.  **데이터 병합 및 전처리:**

      - 두 DataFrame을 `product_id`를 기준으로 병합하시오.
      - `customer_id`의 결측치를 'Unknown'으로 처리하시오.
      - `quantity`가 음수인 이상치를 1로 처리하시오.
      - `purchase_date` 열을 `datetime` 타입으로 변환하시오.

[**정답 코드 보러가기**](https://github.com/xvmon234-ai/Learning-Python/blob/main/CPA%20/my_learing_python%20/Day%2011/solutions/coding_1.py)

2.  **분석 및 시각화:**

      - **가장 많이 판매된 상품 카테고리 Top 5**를 찾고 막대 그래프로 시각화하시오.
      - **월별 총 매출액 추이**를 꺾은선 그래프로 시각화하시오. (매출액 = `quantity` \* `price`)

[**정답 코드 보러가기**](https://github.com/xvmon234-ai/Learning-Python/blob/main/CPA%20/my_learing_python%20/Day%2011/solutions/coding_2.py)

3.  **데이터 저장:**

      - **고객 연령대별 평균 구매 금액**을 계산하고, 이 결과를 새로운 `customer_age_summary.csv` 파일로 저장하시오. (고객 연령대 정보는 없으므로, `customer_id`를 활용하여 연령대를 임의로 그룹화하여 분석하시오. 예: ID 1-5는 10대, 6-10은 20대 등)

[**정답 코드 보러가기**](https://github.com/xvmon234-ai/Learning-Python/blob/main/CPA%20/my_learing_python%20/Day%2011/solutions/coding_3.py)

-----

### 🧠 자기 분석 및 설명 연습

#### **✅ 모범 답안**

  - **시각화 선택 이유:**

      - "판매량 TOP 5 카테고리"는 각 카테고리별로 값을 비교하는 것이 핵심입니다. 따라서 항목 간의 상대적인 크기를 직관적으로 파악할 수 있는 **막대 그래프**를 선택했습니다.
      - "월별 총 매출액 추이"는 시간의 흐름에 따른 연속적인 데이터의 변화를 보여주어야 합니다. 매출액의 상승/하락 추세를 명확히 파악하기 위해 **꺾은선 그래프**가 가장 적합하다고 판단했습니다.

  - **도출된 인사이트:**

      - 막대 그래프를 통해 **'전자제품' 카테고리가 다른 카테고리에 비해 압도적인 판매량**을 기록했음을 알 수 있습니다. 이는 해당 카테고리가 주요 매출원임을 시사하며, 관련 상품에 대한 마케팅을 강화하거나 재고 관리에 우선순위를 두는 전략을 세울 수 있습니다.
      - 꺾은선 그래프를 보면 **3월에 매출이 급격하게 증가하는 추세**를 보였습니다. 이는 3월에 진행된 특정 프로모션이나 이벤트(예: 신학기 세일, 봄맞이 할인)의 영향을 받았을 가능성이 높다고 분석할 수 있습니다.

  - **개선점 및 추가 분석 아이디어:**

      - **개선점:** 데이터 병합 시 `_x`, `_y`와 같은 중복 열 이름이 발생할 수 있는 상황에 대비해 `suffixes` 인자를 활용하는 방법을 숙지해야겠습니다. 또한 `np.nan`이 포함된 `customer_id` 열의 타입을 `int`로 바꾸려 할 때 발생하는 오류를 더 견고하게 처리하는 방법을 고민해봐야겠습니다.
      - **추가 분석 아이디어:**
        1.  **고객 구매 행동 분석:** `customer_id`별 구매 횟수, 평균 구매 금액 등을 분석하여 VIP 고객을 식별하고 맞춤형 마케팅 전략을 제안해 보고 싶습니다.
        2.  **상품별 계절성 분석:** `product_id`와 `purchase_date`를 활용하여 특정 상품이 특정 월이나 계절에 더 많이 팔리는지 분석해보고 싶습니다.
