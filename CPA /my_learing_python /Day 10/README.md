# Day 10: 고급 Pandas 기법 및 데이터 변환

## 🎯 학습 목표

  - 데이터 조작 및 변환을 위한 고급 Pandas 기법을 숙달하고, 실제 데이터에 적용하는 능력 확보.

### ✔️ 오늘 할 일

  - **`apply()`와 `lambda` 함수 (1.5시간)**
      - DataFrame의 행/열에 사용자 정의 함수 적용.
  - **`map()`과 `replace()` (1시간)**
      - 특정 값을 다른 값으로 매핑하거나 교체하는 방법 익히기.
  - **범주형 데이터 처리 (1시간)**
      - `astype('category')`를 이용한 메모리 효율화 및 범주형 연산.
  - **날짜/시간 데이터 처리 기초 (30분)**
      - `pd.to_datetime()`, 날짜별 그룹화, 시간대별 데이터 추출.

-----

### 📝 실습 문제 및 요구사항

#### 데이터 준비

아래 코드를 실행하여 실습에 사용할 DataFrame을 생성합니다.

```python
import pandas as pd
import numpy as np

data = {
    'product_id': ['A101', 'B202', 'A101', 'C303', 'B202', 'A101', 'C303'],
    'order_date': ['2024-03-01', '2024-03-02', '2024-03-03', '2024-03-04', '2024-03-05', '2024-03-06', '2024-03-07'],
    'customer_id': ['cust1', 'cust2', 'cust1', 'cust3', 'cust2', 'cust1', 'cust3'],
    'quantity': [5, 10, 8, 12, 7, 3, 15],
    'price_per_item': [1000, 2000, 1000, 1500, 2000, 1000, 1500],
    'status': ['Pending', 'Completed', 'Completed', 'Cancelled', 'Completed', 'Pending', 'Completed']
}
df = pd.DataFrame(data)
```

#### 문제 1: `apply()`와 `lambda` 함수 활용

  - `price_per_item`과 `quantity`를 사용하여 'total\_price'라는 새로운 열을 만드세요.
  - `total_price`가 10000 이상이면 'High', 5000 이상 10000 미만이면 'Medium', 그 외는 'Low'로 분류하는 'price\_level' 열을 `apply`와 `lambda`를 사용해 추가하세요.

[**정답 코드 보러가기**](https://github.com/xvmon234-ai/Learning-Python/blob/main/CPA%20/my_learing_python%20/Day%2010/solutions/coding_1.py)

#### 문제 2: `map()`과 `replace()` 활용

  - `customer_id`를 사용하여 각 고객별로 고유한 숫자 ID(1, 2, 3...)를 부여하는 'customer\_num\_id' 열을 `map()`을 사용해 추가하세요.
  - `status` 열의 'Pending'을 '처리 중', 'Completed'를 '완료', 'Cancelled'를 '취소'로 바꾸는 변환을 `replace()`를 사용해 수행하세요.

[**정답 코드 보러가기**](https://github.com/xvmon234-ai/Learning-Python/blob/main/CPA%20/my_learing_python%20/Day%2010/solutions/coding_2.py)

#### 문제 3: 범주형 데이터 처리

  - `product_id`, `customer_id`, `status` 열의 데이터 타입을 `category`로 변환하세요.
  - 변환 전후의 DataFrame 메모리 사용량을 `df.info(memory_usage='deep')`를 사용해 비교하고, 그 결과를 분석하세요.

[**정답 코드 보러가기**](https://github.com/xvmon234-ai/Learning-Python/blob/main/CPA%20/my_learing_python%20/Day%2010/solutions/coding_3.py)

#### 문제 4: 날짜/시간 데이터 처리

  - `order_date` 열을 `datetime` 타입으로 변환하세요.
  - `order_date`를 기반으로 'order\_month'와 'day\_of\_week' (요일) 열을 추가하세요.
  - 요일별 평균 주문 수량(`quantity`)을 계산하세요.


  - **요일별 평균 주문 수량:**
    (여기에 계산된 결과를 작성하세요)

[**정답 코드 보러가기**](https://github.com/xvmon234-ai/Learning-Python/blob/main/CPA%20/my_learing_python%20/Day%2010/solutions/coding_4.py)
