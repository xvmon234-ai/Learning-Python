# ==============================================================================
# [문제 6.1.2] Pandas 그룹화 및 집계 (Day 6 학습 내용)
# ==============================================================================

import pandas as pd
import numpy as np # numpy는 현재 문제에 직접 사용되지 않지만, Pandas와 함께 자주 사용되므로 포함할 수 있습니다.

# --- [문제 데이터프레임 정의] ---
sales_data = {'Category': ['Electronics', 'Clothes', 'Electronics', 'Books', 'Clothes'],
              'Product': ['TV', 'Shirt', 'Laptop', 'Novel', 'Pants'],
              'Quantity': [10, 25, 5, 15, 30],
              'Price': [500, 30, 1200, 20, 40]}
sales_df = pd.DataFrame(sales_data)

# --- [최초 나의 코딩] ---
sum_sales_df = sales_df.groupby("Category")["Quantity"].sum()

print("\n--- Category Total Sales ---")
print(sum_sales_df.reset_index())

# --- [코드 실행 결과] ---
"""
--- Category Total Sales ---
      Category  Quantity
0        Books        15
1      Clothes        55
2  Electronics        15
"""

# --- [피드백] ---
"""
문제 6.1.2를 완벽하게 해결하셨습니다! `groupby()`와 `sum()`을 활용하여 카테고리별 총 판매 수량을 정확히 계산하고, `reset_index()`를 통해 결과를 깔끔한 DataFrame 형태로 만든 점이 매우 좋습니다.

**`reset_index()` 사용법에 대한 질문 (어떤 방식이 더 좋을까?):**
제시하신 두 가지 방식, 즉 `(sales_df.groupby("Category")["Quantity"].sum()).reset_index()`와 `sales_df.groupby("Category")["Quantity"].sum().reset_index()`는 **결과적으로 동일한 출력을 제공하며, 기능적으로는 차이가 없습니다.**

하지만 **가독성과 일반적인 관례 측면**에서는 `sum_sales_df.reset_index()` 또는 이 모든 과정을 체이닝하여 `sales_df.groupby(...).sum().reset_index()`처럼 한 줄로 작성하는 것이 더 선호됩니다.

* **가독성:** 대부분의 Pandas 메서드는 연속적으로 호출(체이닝)될 수 있도록 설계되었습니다. `sum().reset_index()`처럼 메서드를 연달아 사용하는 것이 `groupby` 연산의 최종 결과에 대한 변환임을 명확히 보여줍니다.
* **중간 변수 필요성:** `sum_sales_df = sales_df.groupby("Category")["Quantity"].sum()`처럼 중간 변수에 할당하는 방식은 `sum_sales_df`를 다른 곳에서도 **재사용해야 할 필요가 있을 때** 유용합니다. 하지만 단순히 최종 출력 형태를 맞추기 위한 것이라면, 체이닝 방식이 코드를 더 간결하게 만들 수 있습니다.

따라서, **재사용이 필요 없다면 한 줄로 체이닝하는 방식 (`sales_df.groupby("Category")["Quantity"].sum().reset_index()`)이 좀 더 간결하고 Pandas의 철학에 부합**하며, **재사용이 필요하거나 복잡한 연산 단계를 나누고 싶다면 중간 변수를 활용하는 방식 (`sum_sales_df = ...; sum_sales_df.reset_index()`)도 좋습니다.** 현재 풀이도 충분히 이해하기 쉽고 좋은 코드입니다.
"""

# --- [모범 답안] ---
# 각 제품 카테고리별 총 판매 수량 계산 및 DataFrame 형태로 출력
# 일반적으로 더 간결하게 선호되는 체이닝 방식
category_total_quantity_df = sales_df.groupby("Category")["Quantity"].sum().reset_index()

print("\n--- Category Total Sales (모범 답안 예시) ---")
print(category_total_quantity_df)


# --- [학습 기록] ---
"""
**학습 질문**: `groupby()`와 `sum()`을 이용해 그룹별 합계를 구한 후, 결과를 DataFrame 형태로 만들기 위해 `reset_index()`를 언제 호출해야 효율적이고 가독성이 좋을까?

**문제 해결**:
1.  **그룹화 및 합계 계산**: `sales_df.groupby("Category")["Quantity"].sum()`을 사용하여 각 제품 카테고리별로 'Quantity'의 총합을 계산했습니다. 이 결과는 `Category`가 인덱스가 되는 `Series` 형태로 반환됩니다.
2.  **`reset_index()` 적용**: `Series` 형태로 반환된 결과에 `.reset_index()` 메서드를 호출하여 `Category` 인덱스를 다시 일반 컬럼으로 변환하고, 이를 통해 깔끔한 DataFrame 형태로 만들었습니다.

**`reset_index()` 위치에 대한 추가 학습**:
* `sum_sales_df = sales_df.groupby(...).sum()` 후 `sum_sales_df.reset_index()`:
    * **장점**: 중간 결과(`sum_sales_df`)를 명확하게 볼 수 있고, 필요하다면 이 중간 결과를 다른 곳에서 재사용할 수 있습니다. 코드가 여러 단계로 나뉘어 있어 복잡한 로직을 디버깅하기 쉬울 수 있습니다.
    * **단점**: 한 번만 사용될 결과를 위해 별도의 변수를 선언해야 하므로, 코드가 길어질 수 있습니다.
* `sales_df.groupby(...).sum().reset_index()` (체이닝 방식):
    * **장점**: 코드가 한 줄로 간결해지며, Pandas의 메서드 체이닝 철학에 잘 부합합니다. 결과물을 바로 DataFrame으로 얻을 수 있습니다.
    * **단점**: 각 단계의 중간 결과가 변수에 할당되지 않아 디버깅 시 중간 상태를 확인하기 어렵거나, 특정 중간 결과를 재사용하기 어려울 수 있습니다.

**결론**:
두 방식 모두 유효하며 올바른 결과를 도출합니다.
**가독성과 간결성**을 중시하고 중간 결과의 **재사용 필요성이 없다면 체이닝 방식**이 선호됩니다.
**코드의 각 단계를 명확히 구분**하고 중간 결과의 **재사용 가능성**을 열어두고 싶다면 중간 변수를 사용하는 방식도 좋습니다. 현재 제출하신 코드는 명확하고 이해하기 쉬우며, 충분히 좋은 접근 방식입니다.
"""
