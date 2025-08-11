# Day 7: Pandas 데이터 병합 및 결합 (Merge, Concat) 📊

## 학습 목표 🎯

본 학습의 핵심 목표는 **Pandas DataFrame 객체들을 효율적으로 병합하고 연결하는 방법을 숙달**하는 것입니다. 다양한 데이터 소스를 통합하여 분석 가능한 형태로 가공하는 역량은 실제 비즈니스 환경에서 데이터를 다루는 데 필수적입니다. 특히, 여러 테이블 간의 관계를 이해하고 적절한 조인(Join) 방식을 선택하며, 데이터를 요약/재구조화하는 능력은 데이터 분석가의 중요한 자질입니다.

-----

## 1\. `pd.merge()`를 이용한 데이터 병합: 관계형 데이터 통합 🤝

`pd.merge()`는 두 DataFrame을 특정 열(key) 또는 인덱스를 기준으로 결합하여 새로운 DataFrame을 생성하는 강력한 함수입니다. SQL의 `JOIN` 연산과 유사하며, 다양한 조인 방식을 지원하여 데이터 통합의 유연성을 제공합니다.

### 1.1 관련 이론

  * **`pd.merge()` 기본 동작**: 두 DataFrame을 특정 열(key)의 값을 기반으로 연결합니다. 지정된 키 값이 일치하는 행들을 찾아 결합합니다.
      * **중요도**: ⭐⭐⭐
  * **다양한 `how` 매개변수 (조인 방식)**:
      * **`inner` (기본값)**: 양쪽 DataFrame에 모두 존재하는 키 값의 행만 포함합니다. 교집합의 개념입니다.
      * **`left`**: 왼쪽 DataFrame의 모든 키 값을 유지하고, 오른쪽 DataFrame에서 일치하는 값만 가져옵니다. 일치하지 않는 경우 `NaN`으로 채워집니다.
      * **`right`**: 오른쪽 DataFrame의 모든 키 값을 유지하고, 왼쪽 DataFrame에서 일치하는 값만 가져옵니다. 일치하지 않는 경우 `NaN`으로 채워집니다.
      * **`outer`**: 양쪽 DataFrame의 모든 키 값을 포함합니다 (합집합). 일치하지 않는 부분은 `NaN`으로 채워집니다.
      * **중요도**: ⭐⭐⭐
  * **`on`, `left_on`, `right_on`**:
      * `on`: 양쪽 DataFrame에 동일한 이름의 키 열이 있을 때 사용합니다.
      * `left_on`, `right_on`: 양쪽 DataFrame의 키 열 이름이 다를 때 각각 지정합니다.
      * **중요도**: ⭐⭐
  * **`left_index=True`, `right_index=True`**: 인덱스를 기준으로 병합할 때 사용합니다.
      * **중요도**: ⭐⭐

### 1.2 암기할 사항

  * `pd.merge(left_df, right_df, on='common_key', how='inner')`
  * `pd.merge(df1, df2, left_on='df1_key', right_on='df2_key', how='left')`
  * `pd.merge(df_customers, df_orders, on='CustomerID', how='outer')`
  * `pd.merge(df_data, df_lookup, left_index=True, right_on='ID')`

### 1.3 문제

#### 문제 1-1: 고객 정보와 주문 내역 `inner` 조인 🎯

  * **난이도**: 🟢 (하)

  * **학습 목표**: `pd.merge()`의 기본 사용법과 `inner` 조인의 개념을 이해하고 적용할 수 있는지 확인합니다.

  * **문제 내용**:
    고객 정보가 담긴 `customers_df`와 주문 내역이 담긴 `orders_df` 두 DataFrame이 있습니다. 이 두 DataFrame을 `CustomerID` 열을 기준으로 **`inner` 조인**하여 고객의 이름과 해당 고객의 주문 상품 정보를 함께 볼 수 있는 DataFrame을 생성하세요.

  * **문제 데이터프레임 제시**:

    ```python
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

    print("customers_df:")
    print(customers_df)
    print("\norders_df:")
    print(orders_df)
    ```

  * **문제 풀이 가이드**:

    1.  `pd.merge()` 함수를 사용합니다.
    2.  첫 번째 인자로 `customers_df`, 두 번째 인자로 `orders_df`를 전달합니다.
    3.  `on` 매개변수에 조인 기준이 되는 열 이름 (`'CustomerID'`)을 지정합니다.
    4.  `how` 매개변수는 `inner`가 기본값이므로 생략하거나 명시적으로 `'inner'`로 설정합니다.

[▶️ **정답 코드 보러가기**](./solutions/day7_inner_joined.py) 


[📚 **추가 학습 보러가기**](./further_study/outer_join.py)


#### 문제 1-2: 직원 정보와 부서 정보 `left` 조인 (누락 데이터 처리) 🧩

  * **난이도**: 🟡 (중)

  * **학습 목표**: `left` 조인의 동작 방식을 이해하고, 조인 키가 일치하지 않는 경우 `NaN` 값으로 어떻게 채워지는지 확인합니다.

  * **문제 내용**:
    직원 정보 `employees_df`와 부서 정보 `departments_df`가 있습니다. 모든 직원의 정보를 유지하면서, 각 직원의 부서 이름과 위치를 포함하도록 두 DataFrame을 **`left` 조인**하세요. `employees_df`에는 있지만 `departments_df`에는 없는 `DepartmentID`를 가진 직원의 부서 정보는 `NaN`으로 표시되어야 합니다.

  * **문제 데이터프레임 제시**:

    ```python
    import pandas as pd

    data_employees = {'EmployeeID': [101, 102, 103, 104, 105],
                      'Name': ['John', 'Jane', 'Mike', 'Sarah', 'Paul'],
                      'DepartmentID': [1, 2, 99, 1, 3]} # DepartmentID 99는 departments_df에 없음
    employees_df = pd.DataFrame(data_employees)

    data_departments = {'DeptID': [1, 2, 3],
                        'DepartmentName': ['HR', 'IT', 'Marketing'],
                        'Location': ['Seoul', 'Busan', 'Jeju']}
    departments_df = pd.DataFrame(data_departments)

    print("employees_df:")
    print(employees_df)
    print("\ndepartments_df:")
    print(departments_df)
    ```

  * **문제 풀이 가이드**:

    1.  `pd.merge()` 함수를 사용합니다.
    2.  `left_on`과 `right_on` 매개변수를 사용하여 서로 다른 이름의 조인 키 (`'DepartmentID'`와 `'DeptID'`)를 지정합니다.
    3.  `how` 매개변수를 `'left'`로 설정하여 `employees_df`의 모든 레코드를 유지하도록 합니다.


[▶️ **정답 코드 보러가기**](./solutions/day7_left_joined.py) 




#### 문제 1-3: 다중 키 및 상이한 키 이름 병합 🔑🔑

  * **난이도**: 🔴 (상)

  * **학습 목표**: 여러 열을 조인 키로 사용하거나, 서로 다른 이름의 키 열을 동시에 활용하여 데이터를 병합하는 복합적인 시나리오를 해결합니다.

  * **문제 내용**:
    물품 판매 기록 `sales_records_df`와 제품 상세 정보 `product_details_df`가 있습니다. `sales_records_df`의 `ItemCode`와 `SaleDate`를, `product_details_df`의 `ProductCode`와 `ManufacturingDate`를 기준으로 **`inner` 조인**하여 판매된 물품의 상세 정보를 조회하세요. `ItemCode`는 `ProductCode`에 해당하고, `SaleDate`는 `ManufacturingDate`에 해당한다고 가정합니다.

  * **문제 데이터프레임 제시**:

    ```python
    import pandas as pd

    data_sales_records = {'RecordID': [1, 2, 3, 4],
                          'ItemCode': ['A101', 'B202', 'A101', 'C303'],
                          'SaleDate': ['2023-01-10', '2023-01-12', '2023-01-10', '2023-01-15'],
                          'Quantity': [5, 2, 8, 3]}
    sales_records_df = pd.DataFrame(data_sales_records)

    data_product_details = {'ProductCode': ['A101', 'B202', 'D404'],
                            'ManufacturingDate': ['2023-01-10', '2023-01-12', '2023-01-15'],
                            'Description': ['Laptop', 'Mouse', 'Monitor'],
                            'UnitCost': [800, 20, 250]}
    product_details_df = pd.DataFrame(data_product_details)

    print("sales_records_df:")
    print(sales_records_df)
    print("\nproduct_details_df:")
    print(product_details_df)
    ```

  * **문제 풀이 가이드**:

    1.  `pd.merge()` 함수를 사용합니다.
    2.  `left_on`과 `right_on` 매개변수에 각각 리스트 형태로 조인할 열들을 지정합니다. (예: `left_on=['ItemCode', 'SaleDate']`)
    3.  필요한 경우 `how` 매개변수를 지정합니다.


[▶️ **정답 코드 보러가기**](./solutions/day7_multi_keys.py) 



-----

## 2\. `pd.concat()`를 이용한 데이터 연결: 단순 행/열 결합 🔗

`pd.concat()`는 하나 이상의 DataFrame을 단순히 행(위아래) 또는 열(좌우) 방향으로 이어 붙이는 데 사용됩니다. `pd.merge()`와 달리 특정 키를 기반으로 하는 논리적인 결합이 아닌, 물리적인 연결에 가깝습니다.

### 2.1 관련 이론

  * **`pd.concat()` 기본 동작**: 리스트 형태로 전달된 DataFrame들을 지정된 축(`axis`)을 따라 연결합니다.
      * **중요도**: ⭐⭐⭐
  * **`axis` 매개변수**:
      * `axis=0` (기본값): 행 방향(수직)으로 DataFrame들을 쌓습니다. 열 이름이 같으면 해당 열에 값이 채워지고, 다르면 `NaN`이 발생합니다.
      * `axis=1`: 열 방향(수평)으로 DataFrame들을 붙입니다. 인덱스가 일치하는 행끼리 연결됩니다.
      * **중요도**: ⭐⭐⭐
  * **`ignore_index=True`**: 연결 후 기존의 인덱스를 무시하고 0부터 시작하는 새로운 정수 인덱스를 부여합니다. 중복 인덱스 문제를 방지하고 깔끔한 결과 DataFrame을 만들 때 유용합니다.
      * **중요도**: ⭐⭐

### 2.2 암기할 사항

  * `pd.concat([df1, df2, df3], axis=0, ignore_index=True)`
  * `pd.concat([df_info, df_details], axis=1)`

### 2.3 문제

#### 문제 2-1: 분기별 판매 데이터 수직 결합 및 인덱스 초기화 📈

  * **난이도**: 🟡 (중)

  * **학습 목표**: `pd.concat()`를 이용한 다중 DataFrame의 수직 연결과 `ignore_index` 매개변수의 활용법을 익힙니다.

  * **문제 내용**:
    2024년 1분기(`q1_sales_df`), 2분기(`q2_sales_df`), 3분기(`q3_sales_df`)의 판매 데이터가 각각 다른 DataFrame에 저장되어 있습니다. 이 세 DataFrame을 **수직으로 연결**하여 2024년 전체 판매 데이터를 나타내는 하나의 DataFrame을 만드세요. 연결 후에는 **인덱스를 초기화**하여 새로운 연속적인 인덱스를 부여해야 합니다.

  * **문제 데이터프레임 제시**:

    ```python
    import pandas as pd

    data_q1 = {'Product': ['A', 'B', 'C'],
               'Sales': [100, 150, 200],
               'Quarter': ['Q1', 'Q1', 'Q1']}
    q1_sales_df = pd.DataFrame(data_q1)

    data_q2 = {'Product': ['A', 'B', 'D'],
               'Sales': [120, 180, 90],
               'Quarter': ['Q2', 'Q2', 'Q2']}
    q2_sales_df = pd.DataFrame(data_q2)

    data_q3 = {'Product': ['B', 'C', 'E'],
               'Sales': [250, 130, 70],
               'Quarter': ['Q3', 'Q3', 'Q3']}
    q3_sales_df = pd.DataFrame(data_q3)

    print("q1_sales_df:")
    print(q1_sales_df)
    print("\nq2_sales_df:")
    print(q2_sales_df)
    print("\nq3_sales_df:")
    print(q3_sales_df)
    ```

  * **문제 풀이 가이드**:

    1.  `pd.concat()` 함수를 사용합니다.
    2.  연결할 DataFrame들을 리스트 `[]` 안에 넣어 첫 번째 인자로 전달합니다.
    3.  수직 연결이므로 `axis` 매개변수를 기본값(`0`)으로 두거나 명시적으로 `0`으로 설정합니다.
    4.  인덱스 초기화를 위해 `ignore_index=True` 매개변수를 사용합니다.


[▶️ **정답 코드 보러가기**](./solutions/day7_concat_1.py) 



#### 문제 2-2: 고객 연락처 및 주소 정보 수평 결합 🏠

  * **난이도**: 🔴 (상)

  * **학습 목표**: `pd.concat()`를 사용하여 열 방향으로 DataFrame을 연결하는 방법을 이해하고, 인덱스가 일치하지 않을 때의 `NaN` 처리 방식을 파악합니다.

  * **문제 내용**:
    고객 이름과 이메일 정보가 담긴 `contact_info_df`와 고객 ID 및 주소 정보가 담긴 `address_info_df`가 있습니다. 두 DataFrame은 동일한 고객에 대한 정보를 담고 있지만, 열 구성이 다르고 인덱스가 일부 일치하지 않을 수 있습니다. `CustomerID` 열을 기준으로 데이터를 정렬한 후, 이 두 DataFrame을 **수평으로 연결**하여 모든 고객의 연락처와 주소 정보를 한눈에 볼 수 있는 DataFrame을 생성하세요.

  * **문제 데이터프레임 제시**:

    ```python
    import pandas as pd

    data_contact = {'CustomerID': [1, 2, 3, 5], # CustomerID 5는 address_info_df에 없음
                    'Name': ['Alice', 'Bob', 'Charlie', 'Eve'],
                    'Email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'eve@example.com']}
    contact_info_df = pd.DataFrame(data_contact).set_index('CustomerID')

    data_address = {'CustomerID': [1, 2, 4, 3], # CustomerID 4는 contact_info_df에 없음
                    'Address': ['123 Main St', '456 Oak Ave', '789 Pine Ln', '101 Maple Dr'],
                    'ZipCode': ['10001', '90001', '60001', '70001']}
    address_info_df = pd.DataFrame(data_address).set_index('CustomerID')

    print("contact_info_df:")
    print(contact_info_df)
    print("\naddress_info_df:")
    print(address_info_df)
    ```

  * **문제 풀이 가이드**:

    1.  각 DataFrame의 인덱스가 `CustomerID`가 되도록 `set_index('CustomerID')`를 사용합니다. (문제 데이터프레임에 이미 적용되어 있음)
    2.  `pd.concat()` 함수를 사용합니다.
    3.  수평 연결이므로 `axis=1`을 지정합니다.
    4.  인덱스가 일치하지 않는 경우 어떤 결과가 나오는지 확인합니다. (이 문제에서는 `ignore_index=True`를 사용하지 않음)


[▶️ **정답 코드 보러가기**](./solutions/day7_concat_2.py) 


-----

## 3\. 선택 학습: `pivot_table()`을 이용한 데이터 요약 및 재구조화 🔄

`pivot_table()`은 데이터를 특정 기준에 따라 재구성하고 요약(집계)하는 데 사용되는 강력한 기능입니다. 엑셀의 피벗 테이블과 유사하며, 복잡한 데이터를 원하는 형태로 변환하여 인사이트를 도출하는 데 매우 유용합니다.

### 3.1 관련 이론

  * **`pivot_table()` 기본 개념**: 데이터를 지정된 `index`와 `columns`를 기준으로 재정렬하고, `values`에 해당하는 데이터를 `aggfunc` (집계 함수)를 사용하여 요약합니다.
      * **중요도**: ⭐⭐
  * **주요 매개변수**:
      * `index`: 새로운 DataFrame의 행(row) 인덱스로 사용할 열 이름 또는 열 이름 리스트.
      * `columns`: 새로운 DataFrame의 열(column) 헤더로 사용할 열 이름 또는 열 이름 리스트.
      * `values`: 집계할 데이터가 있는 열 이름.
      * `aggfunc`: `values`를 어떻게 집계할지 지정하는 함수 (예: `'mean'`, `'sum'`, `'count'`, `np.sum` 등). 리스트 형태로 여러 함수를 지정할 수 있습니다. 기본값은 `'mean'`입니다.
      * `fill_value`: 피벗 테이블 결과에서 결측치(`NaN`)가 발생할 경우, 해당 값을 채울 때 사용합니다.
      * **중요도**: ⭐⭐

### 3.2 암기할 사항

  * `df.pivot_table(index='Category', values='Sales', aggfunc='sum')`
  * `df.pivot_table(index='Date', columns='Region', values='Revenue', aggfunc=['mean', 'sum'], fill_value=0)`

### 3.3 문제

#### 문제 3-1: 지역별, 제품별 평균 판매액 집계 📊

  * **난이도**: 🔴 (상)

  * **학습 목표**: `pd.pivot_table()`을 사용하여 복잡한 데이터를 여러 기준으로 요약하고 분석하는 능력을 함양합니다.

  * **문제 내용**:
    다음 판매 데이터 `sales_data_df`가 주어졌을 때, 각 `Region`별, `Product`별 **평균 `Sales` 금액**을 계산하는 피벗 테이블을 생성하세요.

  * **문제 데이터프레임 제시**:

    ```python
    import pandas as pd
    import numpy as np # aggfunc에 np.sum 등을 사용할 수 있음을 보여주기 위함

    data_sales = {
        'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03', '2023-01-03', '2023-01-04'],
        'Region': ['East', 'West', 'East', 'West', 'East', 'West', 'East'],
        'Product': ['A', 'B', 'A', 'C', 'B', 'A', 'C'],
        'Sales': [100, 150, 120, 200, 180, 110, 250]
    }
    sales_data_df = pd.DataFrame(data_sales)

    print("sales_data_df:")
    print(sales_data_df)
    ```


[▶️ **정답 코드 보러가기**](./solutions/day7_pivot_tables_1.py) 



  * **문제 풀이 가이드**:

    1.  `sales_data_df`에 `.pivot_table()` 메서드를 호출합니다.
    2.  `index` 매개변수에 행(row) 기준으로 사용할 열 (`'Region'`)을 지정합니다.
    3.  `columns` 매개변수에 열(column) 기준으로 사용할 열 (`'Product'`)을 지정합니다.
    4.  `values` 매개변수에 집계할 값 (`'Sales'`)을 지정합니다.
    5.  `aggfunc` 매개변수에 집계 함수 (`'mean'` 또는 `np.mean`)를 지정합니다.

#### 문제 3-2: 월별 제품 판매량 및 총 판매액 집계 (복수 집계 함수 및 결측치 처리) 📈📊

  * **난이도**: 🔴 (상)

  * **학습 목표**: `pivot_table()`에 여러 개의 집계 함수를 동시에 적용하고, `fill_value`를 사용하여 결과 DataFrame의 결측치를 특정 값으로 채우는 방법을 익힙니다.

  * **문제 내용**:
    다음 판매 기록 `monthly_sales_df`가 있습니다. 각 `Product`별로 월(`Month`)별 \*\*총 판매량(`Quantity`의 합계)\*\*과 \*\*총 판매액(`Sales`의 합계)\*\*을 계산하는 피벗 테이블을 생성하세요. 만약 특정 월에 특정 제품의 판매 기록이 없는 경우, 해당 값은 `0`으로 표시되도록 처리하세요.

  * **문제 데이터프레임 제시**:

    ```python
    import pandas as pd

    data_monthly_sales = {
        'Month': [1, 1, 2, 2, 2, 3, 3, 1],
        'Product': ['Laptop', 'Mouse', 'Laptop', 'Keyboard', 'Mouse', 'Mouse', 'Laptop', 'Monitor'],
        'Quantity': [5, 10, 3, 7, 12, 8, 4, 2],
        'Sales': [5000, 200, 3000, 350, 240, 160, 4000, 600]
    }
    monthly_sales_df = pd.DataFrame(data_monthly_sales)

    print("monthly_sales_df:")
    print(monthly_sales_df)
    ```

  * **문제 풀이 가이드**:

    1.  `monthly_sales_df`에 `.pivot_table()` 메서드를 호출합니다.
    2.  `index` 매개변수에 `'Product'`를 지정하여 제품별로 행을 구성합니다.
    3.  `columns` 매개변수에 `'Month'`를 지정하여 월별로 열을 구성합니다.
    4.  `values` 매개변수에 집계할 값들(`'Quantity'`, `'Sales'`)을 리스트 형태로 전달합니다.
    5.  `aggfunc` 매개변수에 각 `values`에 적용할 집계 함수(`'sum'`)를 지정합니다. `values`가 여러 개일 경우 `aggfunc`도 각 `values`에 해당하는 함수를 지정하거나, 모든 `values`에 공통으로 적용될 함수를 지정할 수 있습니다.
    6.  결과 DataFrame의 `NaN` 값을 `0`으로 채우기 위해 `fill_value=0` 매개변수를 사용합니다.
   

[▶️ **정답 코드 보러가기**](./solutions/day7_pivot_tables_2.py)


[📚 **추가 학습 보러가기**](./further_study/what_else.py)


-----
