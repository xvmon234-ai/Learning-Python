-----

# Day 6: Pandas 데이터 조작 심화 - 그룹화 및 집계 (Group By & Aggregation)

## 🎯 학습 목표

Day 6의 핵심 목표는 **Pandas의 `groupby()` 메서드를 이해하고 활용**하여 데이터를 특정 기준에 따라 그룹으로 나누고, 각 그룹에 대해 요약 통계(집계)를 계산하는 능력을 심층적으로 습득하는 것입니다. 이를 통해 대규모 데이터에서 의미 있는 인사이트를 도출하고, 복잡한 비즈니스 질문에 답변할 수 있는 기반을 마련할 수 있습니다.

  * **`groupby()` 기본 개념 이해**: 데이터를 특정 컬럼의 고유 값들을 기준으로 논리적인 그룹으로 나누는 방법을 학습합니다.
  * **다양한 집계 함수 적용**: `sum()`, `mean()`, `count()`, `min()`, `max()`, `size()`, `agg()` 등 여러 집계 함수를 사용하여 그룹별 요약 통계를 계산하는 방법을 익힙니다.
  * **다중 컬럼 그룹화 및 다중 집계**: 하나 이상의 컬럼을 기준으로 데이터를 그룹화하고, 여러 집계 함수를 동시에 적용하여 다양한 관점의 요약 정보를 얻는 방법을 숙달합니다.
  * **그룹화된 데이터의 고급 활용**: `reset_index()`, `filter()`, `transform()`, `apply()` 등을 통해 집계 결과를 깔끔하게 정리하고 활용하며, 그룹별 고급 연산을 수행하는 방법을 배웁니다.

-----

## 📚 상세 학습 내용 및 문제

### 주제 6.1 / `groupby()` 기본 및 단일 집계

#### 관련 이론들:

  * **🌟🌟🌟 `df.groupby('컬럼명')`**: DataFrame을 특정 컬럼의 고유 값들을 기준으로 **그룹 객체**로 만듭니다. 이 자체로는 계산이 이루어지지 않으며, 뒤에 **집계 함수**가 와야 합니다.
  * **🌟🌟🌟 집계 함수 (Aggregation Functions)**:
      * `.sum()`: 각 그룹의 합계
      * `.mean()`: 각 그룹의 평균
      * `.count()`: 각 그룹의 개수 (NaN 제외)
      * `.size()`: 각 그룹의 크기 (NaN 포함)
      * `.min()`: 각 그룹의 최소값
      * `.max()`: 각 그룹의 최대값
      * `.std()`: 각 그룹의 표준편차
      * `.var()`: 각 그룹의 분산
  * **🌟🌟 `reset_index()`**: `groupby()` 결과는 그룹화된 컬럼이 인덱스가 되는 경우가 많습니다. `reset_index()`를 사용하면 이 인덱스를 일반 컬럼으로 다시 변환하여 **DataFrame 형태로 깔끔하게** 만들 수 있습니다.

#### 암기할 사항:

  * **`groupby()`는 항상 뒤에 집계 함수가 와야 유의미한 결과를 반환합니다.**
      * `df.groupby('기준컬럼')['집계대상컬럼'].집계함수()`
      * `df.groupby('기준컬럼').집계함수()` (이 경우 모든 숫자 컬럼에 집계 적용)
  * **`reset_index()`는 `groupby()` 결과의 형태를 다루는 데 매우 중요합니다.**

#### 문제 (난이도: 하)

##### 문제 6.1.1: 다음 `employees_df` 데이터프레임을 사용하여 각 부서별 평균 급여를 계산하세요.

**문제의 학습 목표:**
`groupby()`를 사용하여 특정 컬럼을 기준으로 그룹화하고, 단일 집계 함수 (`.mean()`)를 적용하여 그룹별 평균을 계산하는 방법을 익힙니다.

```python
import pandas as pd
data = {'Department': ['HR', 'IT', 'HR', 'IT', 'Marketing', 'HR'],
        'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
        'Salary': [60000, 75000, 62000, 80000, 70000, 65000]}
employees_df = pd.DataFrame(data)
```

**문제에 대한 가이드:**

1.  `employees_df`를 `'Department'` 컬럼으로 그룹화하세요.
2.  그룹화된 객체에서 `'Salary'` 컬럼을 선택하세요.
3.  `.mean()` 메서드를 적용하여 평균 급여를 계산하세요.

##### 문제 6.1.2: 다음 `sales_df` 데이터프레임을 사용하여 각 제품 카테고리별 총 판매 수량(Quantity)을 계산하고, 결과를 DataFrame 형태로 출력하세요.

**문제의 학습 목표:**
`groupby()`를 사용하여 그룹화하고, `sum()` 집계 함수를 적용한 후 `reset_index()`를 사용하여 결과를 DataFrame으로 변환하는 방법을 익힙니다.

```python
import pandas as pd
data = {'Category': ['Electronics', 'Clothes', 'Electronics', 'Books', 'Clothes'],
        'Product': ['TV', 'Shirt', 'Laptop', 'Novel', 'Pants'],
        'Quantity': [10, 25, 5, 15, 30],
        'Price': [500, 30, 1200, 20, 40]}
sales_df = pd.DataFrame(data)
```

**문제에 대한 가이드:**

1.  `sales_df`를 `'Category'` 컬럼으로 그룹화하세요.
2.  그룹화된 객체에서 `'Quantity'` 컬럼을 선택하고 `.sum()` 메서드를 적용하세요.
3.  `.reset_index()`를 호출하여 결과를 DataFrame 형태로 만드세요.

##### 문제 6.1.3: 다음 `weather_df` 데이터프레임을 사용하여 각 도시별 가장 높은 기온(Temperature)을 찾으세요.

**문제의 학습 목표:**
`groupby()`와 `.max()` 집계 함수를 사용하여 그룹별 최대값을 찾는 방법을 익힙니다.

```python
import pandas as pd
data = {'City': ['Seoul', 'Busan', 'Seoul', 'Jeju', 'Busan', 'Seoul'],
        'Date': ['2023-07-01', '2023-07-01', '2023-07-02', '2023-07-02', '2023-07-03', '2023-07-03'],
        'Temperature': [28, 26, 30, 25, 27, 29]}
weather_df = pd.DataFrame(data)
```

**문제에 대한 가이드:**

1.  `weather_df`를 `'City'` 컬럼으로 그룹화하세요.
2.  그룹화된 객체에서 `'Temperature'` 컬럼을 선택하고 `.max()` 메서드를 적용하세요.

-----

### 주제 6.2 / 다중 컬럼 그룹화 및 다중 집계

#### 관련 이론들:

  * **🌟🌟🌟 `df.groupby(['컬럼1', '컬럼2'])`**: 여러 컬럼을 **리스트 형태**로 전달하여 다중 기준으로 그룹화합니다.
  * **🌟🌟🌟 `df.groupby(...).agg({'컬럼명': '집계함수', ...})`**: `agg()` 메서드를 사용하여 여러 컬럼에 대해 다른 집계 함수를 동시에 적용하거나, 한 컬럼에 대해 여러 집계 함수를 적용할 수 있습니다.
      * **예시**: `df.groupby('Category').agg({'Price': 'mean', 'Stock': 'sum'})`
      * **예시 (새로운 컬럼명 지정)**: `df.groupby('Category').agg(총재고=('Stock', 'sum'), 평균가격=('Price', 'mean'))`

#### 암기할 사항:

  * **다중 그룹화**는 `['컬럼1', '컬럼2']` **리스트 형태로\!**
  * **`agg()`는 유연한 집계를 위한 필수 메서드입니다.** 딕셔너리 형태로 `{'컬럼': '함수'}`를 전달하거나, 튜플 형태로 `('새이름', '컬럼', '함수')`를 전달할 수 있습니다.

#### 문제 (난이도: 중)

##### 문제 6.2.1: `employees_df_v2` 데이터프레임을 사용하여 각 부서 및 직급(Position이라는 컬럼이 추가되었다고 가정)별 평균 급여와 최대 급여를 계산하세요.

**문제의 학습 목표:**
두 개 이상의 컬럼을 기준으로 데이터를 그룹화하고, `agg()` 메서드를 사용하여 단일 컬럼에 대해 여러 집계 함수를 동시에 적용하는 방법을 익힙니다.

```python
import pandas as pd
data = {'Department': ['HR', 'IT', 'HR', 'IT', 'Marketing', 'HR', 'IT'],
        'Position': ['Manager', 'Developer', 'Staff', 'Developer', 'Manager', 'Staff', 'Manager'],
        'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
        'Salary': [90000, 75000, 62000, 80000, 100000, 65000, 95000]}
employees_df_v2 = pd.DataFrame(data)
```

**문제에 대한 가이드:**

1.  `employees_df_v2`를 `['Department', 'Position']` 리스트를 사용하여 그룹화하세요.
2.  `agg()` 메서드를 사용하여 `'Salary'` 컬럼에 대해 `['mean', 'max']` 두 가지 집계 함수를 적용하세요.

##### 문제 6.2.2: `sales_df` 데이터프레임을 사용하여 각 제품 카테고리별로 총 판매 수량과 평균 가격을 계산하고, 결과 컬럼 이름을 '총\_수량', '평균\_가격'으로 지정하세요.

**문제의 학습 목표:**
`agg()` 메서드를 사용하여 여러 컬럼에 대해 다른 집계 함수를 적용하고, 동시에 결과 컬럼의 이름을 원하는 대로 지정하는 방법을 익힙니다.

```python
import pandas as pd
data = {'Category': ['Electronics', 'Clothes', 'Electronics', 'Books', 'Clothes'],
        'Product': ['TV', 'Shirt', 'Laptop', 'Novel', 'Pants'],
        'Quantity': [10, 25, 5, 15, 30],
        'Price': [500, 30, 1200, 20, 40]}
sales_df = pd.DataFrame(data)
```

**문제에 대한 가이드:**

1.  `sales_df`를 `'Category'` 컬럼으로 그룹화하세요.
2.  `agg()` 메서드 내에서 새로운 컬럼 이름을 지정하는 튜플 형식(`새로운_이름=('원본_컬럼', '집계_함수')`)을 사용하여 `'Quantity'`에 대한 총합과 `'Price'`에 대한 평균을 계산하세요.

##### 문제 6.2.3: 다음 `customer_orders_df` 데이터프레임을 사용하여 각 고객(CustomerID)별로 총 주문 금액(Amount)과 주문 건수(OrderCount)를 계산하세요.

**문제의 학습 목표:**
`agg()` 메서드를 사용하여 여러 컬럼에 대해 다른 집계 함수를 적용하고, `count()` 함수로 주문 건수를 계산하는 방법을 익힙니다.

```python
import pandas as pd
data = {'CustomerID': [1, 2, 1, 3, 2, 1],
        'OrderID': [101, 102, 103, 104, 105, 106],
        'Amount': [500, 250, 700, 150, 300, 400]}
customer_orders_df = pd.DataFrame(data)
```

**문제에 대한 가이드:**

1.  `customer_orders_df`를 `'CustomerID'` 컬럼으로 그룹화하세요.
2.  `agg()` 메서드를 사용하여 `'Amount'` 컬럼의 `sum()`과 `'OrderID'` 컬럼의 `count()`를 계산하세요. (또는 `count()`가 의미 있는 다른 컬럼을 사용해도 됩니다.)
3.  결과 컬럼 이름을 직관적으로 지정하세요.

-----

### 주제 6.3 / 그룹화된 데이터의 고급 활용 (필터링, 변환, 적용)

#### 관련 이론들:

  * **🌟 `df.groupby(...).filter(lambda x: 조건)`**: 그룹별로 특정 조건을 만족하는 **그룹 전체를 필터링**합니다. (원본 DataFrame의 행 수를 유지)
  * **🌟 `df.groupby(...).transform(함수)`**: 그룹별로 연산을 수행한 결과를 **원본 DataFrame의 인덱스에 맞춰 반환**합니다. (원본 DataFrame의 행 수를 유지) 예를 들어, 그룹 내 평균/최대값을 모든 해당 그룹의 행에 복사하는 데 유용합니다.
  * **🌟 `df.groupby(...).apply(함수)`**: 그룹별로 **사용자 정의 함수나 복잡한 연산**을 적용합니다. (가장 유연하지만, 성능상 주의 필요)

#### 암기할 사항:

  * **`filter()`**: 그룹 전체를 특정 조건으로 필터링할 때 사용하며, 반환되는 DataFrame의 행 수는 원본과 같거나 작습니다.
  * **`transform()`**: 그룹별 연산 결과를 원본 DataFrame의 크기에 맞춰 새로운 컬럼으로 추가할 때 유용합니다.
  * **`apply()`**: 가장 유연하며, 복잡한 그룹별 연산이나 여러 컬럼에 걸친 연산, 결과가 DataFrame 형태일 때 사용합니다.

#### 문제 (난이도: 상)

##### 문제 6.3.1: `employees_df_v2` 데이터프레임을 사용하여 평균 급여가 70,000 이상인 부서의 모든 직원을 필터링하여 출력하세요.

**문제의 학습 목표:**
`groupby()`와 `filter()` 메서드를 조합하여 특정 그룹 조건에 따라 원본 DataFrame에서 해당 그룹의 모든 행을 필터링하는 방법을 익힙니다.

```python
import pandas as pd
data = {'Department': ['HR', 'IT', 'HR', 'IT', 'Marketing', 'HR', 'IT'],
        'Position': ['Manager', 'Developer', 'Staff', 'Developer', 'Manager', 'Staff', 'Manager'],
        'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
        'Salary': [90000, 75000, 62000, 80000, 100000, 65000, 95000]}
employees_df_v2 = pd.DataFrame(data)
```

**문제에 대한 가이드:**

1.  `employees_df_v2`를 `'Department'` 컬럼으로 그룹화하세요.
2.  `filter()` 메서드에 `lambda` 함수를 전달하여 각 그룹 (`x`)의 `'Salary'` 컬럼 평균이 70000 이상인지 확인하는 조건을 적용하세요.

##### 문제 6.3.2: `employees_df_v2` 데이터프레임에 각 부서 내에서 직원의 급여가 해당 부서의 평균 급여보다 얼마나 높은지/낮은지를 나타내는 'Salary\_Deviation'라는 새 컬럼을 추가하세요.

**문제의 학습 목표:**
`groupby()`와 `transform()` 메서드를 사용하여 그룹별 연산 결과를 원본 DataFrame의 각 행에 적용하여 새로운 컬럼을 생성하는 방법을 익힙니다.

```python
import pandas as pd
data = {'Department': ['HR', 'IT', 'HR', 'IT', 'Marketing', 'HR', 'IT'],
        'Position': ['Manager', 'Developer', 'Staff', 'Developer', 'Manager', 'Staff', 'Manager'],
        'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
        'Salary': [90000, 75000, 62000, 80000, 100000, 65000, 95000]}
employees_df_v2 = pd.DataFrame(data)
```

**문제에 대한 가이드:**

1.  `employees_df_v2`를 `'Department'` 컬럼으로 그룹화하세요.
2.  `transform()` 메서드에 `lambda` 함수를 전달하여 각 그룹 (`x`)의 `'Salary'` 값에서 해당 그룹의 평균(`x.mean()`)을 빼는 연산을 수행하세요.
3.  이 결과를 `'Salary_Deviation'`이라는 새로운 컬럼으로 할당하세요.

##### 문제 6.3.3: `sales_df` 데이터프레임을 사용하여 각 제품 카테고리별로 가장 비싼 2개의 제품을 출력하세요. (힌트: `apply()`와 `nlargest()` 또는 `sort_values()`를 조합)

**문제의 학습 목표:**
`groupby()`와 `apply()` 메서드를 사용하여 각 그룹에 대해 더 복잡한 사용자 정의 연산(예: 상위 N개 항목 선택)을 적용하는 방법을 익힙니다.

```python
import pandas as pd
data = {'Category': ['Electronics', 'Clothes', 'Electronics', 'Books', 'Clothes'],
        'Product': ['TV', 'Shirt', 'Laptop', 'Novel', 'Pants'],
        'Quantity': [10, 25, 5, 15, 30],
        'Price': [500, 30, 1200, 20, 40]}
sales_df = pd.DataFrame(data)
```

**문제에 대한 가이드:**

1.  `sales_df`를 `'Category'` 컬럼으로 그룹화하세요.
2.  `apply()` 메서드에 `lambda` 함수를 전달하여 각 그룹 (`x`)에 대해 `'Price'` 컬럼을 기준으로 `nlargest(2)`를 호출하거나, `'Price'`를 기준으로 내림차순 정렬(`sort_values(by='Price', ascending=False)`)한 후 `.head(2)`를 선택하세요.

-----
