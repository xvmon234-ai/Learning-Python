# ==============================================================================
# [문제 1-1] 고객 정보와 주문 내역 inner 조인 (Day 7 학습 내용)
# ==============================================================================

# --- [최초 나의 코딩] ---
import pandas as pd

data_customers = {'CustomerID': [1, 2, 3, 4],
                  'Name': ['Alice', 'Bob', 'Charlie', 'David'],
                  'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
customers_df = pd.DataFrame(data_customers)

data_orders = {'OrderID': [101, 102, 103, 104, 105],
               'CustomerID': [1, 2, 1, 5, 3], # CustomerID 5는 customers_df에 없음
               'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam'],
               'Price': [1200, 25, 75, 300, 50]}
orders_df = pd.DataFrame(data_orders)

df_joined = pd.merge(customers_df, orders_df, on="CustomerID", how="inner")

print("\n --- Inner Joined Dataframe --- \n")
print(df_joined)

# --- [코드 실행 결과] ---
"""
 --- Inner Joined Dataframe ---
   CustomerID     Name         City  OrderID   Product  Price
0           1    Alice     New York      101    Laptop   1200
1           1    Alice     New York      103  Keyboard     75
2           2      Bob  Los Angeles      102     Mouse     25
3           3  Charlie      Chicago      105    Webcam     50
"""

# --- [피드백] ---
"""
문제 1-1을 **완벽하게 해결**하셨습니다! `pd.merge()` 함수와 `inner` 조인 방식을 정확하게 사용하여 `customers_df`와 `orders_df`를 `CustomerID` 열을 기준으로 성공적으로 병합했습니다.

1.  **정확한 함수 사용**: `pd.merge()` 함수를 올바르게 호출했습니다.
2.  **올바른 조인 키 지정**: `on="CustomerID"`를 통해 두 DataFrame이 공유하는 `CustomerID` 열을 기준으로 병합하도록 정확히 지정했습니다. 이는 관계형 데이터베이스의 기본 키(Primary Key)와 외래 키(Foreign Key) 관계를 Pandas로 구현한 것입니다.
3.  **정확한 조인 방식**: `how="inner"`를 사용하여 양쪽 DataFrame에 모두 존재하는 `CustomerID`를 가진 레코드만 결과에 포함되도록 했습니다. `CustomerID` 5 (orders_df에만 있음)와 `CustomerID` 4 (customers_df에만 있음)에 해당하는 레코드는 결과에서 제외된 것을 통해 `inner` 조인의 동작 원리를 정확히 이해하고 있음을 알 수 있습니다.

이 풀이는 Pandas를 활용한 데이터 병합의 가장 기본적이면서도 핵심적인 예시이며, 실제 데이터 분석에서 여러 테이블을 통합하는 데 필수적인 역량을 보여줍니다.
"""

# --- [모범 답안] ---
# '최초 나의 코딩'에서 이미 모범적으로 해결되었으므로, 추가적인 모범 답안은 생략합니다.
# 다만, 결과를 변수에 할당하는 것은 좋은 습관이며, 출력 메시지를 명확히 하는 것이 좋습니다.

# combined_df = pd.merge(customers_df, orders_df, on="CustomerID", how="inner")
# print("\n--- 고객 및 주문 정보 통합 (Inner Join) 결과 ---")
# print(combined_df)


# --- [학습 기록] ---
"""
**학습 질문**: 서로 다른 데이터프레임에 분리 저장된 고객 정보와 주문 정보를 `CustomerID`를 기준으로 통합하려면 어떻게 해야 할까? `inner` 조인은 언제 사용하며, 그 특징은 무엇일까?

**문제 해결**:
1.  **데이터프레임 준비**: `customers_df`와 `orders_df`라는 두 개의 DataFrame을 생성하여 고객 정보와 주문 정보를 각각 분리하여 저장했습니다.
2.  **`pd.merge()` 함수 사용**: `pd.merge(customers_df, orders_df, on="CustomerID", how="inner")` 코드를 사용하여 두 DataFrame을 병합했습니다.
    * `customers_df`: 병합의 '왼쪽' DataFrame.
    * `orders_df`: 병합의 '오른쪽' DataFrame.
    * `on="CustomerID"`: 두 DataFrame에서 공통으로 존재하는 'CustomerID' 열을 기준으로 병합하도록 지정했습니다. 이 열의 값이 동일한 행들끼리 결합됩니다.
    * `how="inner"`: `inner` 조인 방식을 명시했습니다. 이는 양쪽 DataFrame에 모두 존재하는 `CustomerID` 값만을 기준으로 데이터를 결합하는 방식입니다. 결과적으로, `customers_df`에는 있지만 `orders_df`에 없는 고객 (예: CustomerID 4)과 `orders_df`에는 있지만 `customers_df`에 없는 고객 (예: CustomerID 5)의 정보는 최종 결과에서 제외됩니다.
3.  **결과 확인**: 병합된 `df_joined` DataFrame을 출력하여 `CustomerID` 1, 2, 3에 해당하는 고객의 이름, 도시 정보와 함께 해당 고객의 주문 ID, 상품, 가격 정보가 정확히 결합되었음을 확인했습니다.

**추가 학습 (공인회계사 업무와의 관련성 및 `inner` 조인의 활용)**:

`pd.merge()`의 `inner` 조인 방식은 공인회계사(CPA)가 데이터를 분석하는 업무에서 **데이터의 정합성을 확인하고, 핵심적인 연결 고리를 통해 정보를 통합**할 때 매우 중요합니다.

* **거래의 완전성 및 정확성 검증**:
    * **예시**: 회계 장부의 `거래내역(Transaction)` 데이터와 전표 시스템의 `전표 발행 내역` 데이터를 `전표번호`나 `거래ID`를 기준으로 `inner` 조인합니다. 이 결과는 양쪽에 모두 기록된 거래만을 보여주며, 이를 통해 **누락된 전표나 장부에 반영되지 않은 거래**를 간접적으로 식별하는 기초 자료로 활용할 수 있습니다. `inner` 조인 결과에 없는 전표 번호는 어느 한쪽에만 존재하는 것이므로, 추가적인 검토가 필요함을 의미합니다.
    * **예시**: 재고 관리 시스템의 `입출고 기록`과 회계 시스템의 `재고자산 계정 거래 내역`을 `상품코드`와 `날짜`를 기준으로 `inner` 조인하여, **실물 재고 변동과 장부상 변동이 일치하는지** 검증할 수 있습니다. 불일치하는 상품 코드는 즉시 오류 또는 감사 필요 대상으로 분류됩니다.

* **핵심 비즈니스 정보 추출**:
    * **예시**: `고객 마스터 데이터`와 `매출 데이터`를 `고객ID`로 `inner` 조인하여 **실제로 매출이 발생한 고객에 대한 상세 정보**만을 추출하고 싶을 때 유용합니다. 이는 활성 고객 분석이나 주요 고객 세분화의 시작점이 됩니다.
    * **예시**: `사원 정보`와 `급여 지급 내역`을 `사원번호`로 `inner` 조인하여 **실제 급여가 지급된 현직 사원들의 정보**를 확인하고, 퇴사자나 유령 직원에 대한 급여 지급 여부를 감사하는 데 활용됩니다.

* **재무 보고서 작성 보조**:
    * **예시**: 특정 프로젝트의 **원가 명세서**를 작성할 때, `프로젝트별 비용 집계 데이터`와 `해당 비용에 대한 증빙 문서 정보`를 `프로젝트ID` 또는 `증빙번호`로 `inner` 조인하여 **실제 비용과 증빙이 모두 존재하는 거래**만을 기반으로 보고서를 구성할 수 있습니다.

`inner` 조인은 "교차 검증"의 가장 기본적인 형태로, 두 개 이상의 데이터 소스에서 **'공통적으로 유효한' 정보만을 추출**하고자 할 때 강력한 도구로 사용됩니다. 이는 데이터의 정확성과 신뢰성을 확보하는 데 기여하며, 감사 및 재무 분석의 중요한 출발점이 됩니다.
"""
