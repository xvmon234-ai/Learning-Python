# ==============================================================================
# [문제 6. 데이터프레임 중복값 처리 (duplicated, drop_duplicates 활용)]
# ==============================================================================

# 관련 주제: 5.4 / 중복값(Duplicates) 처리
# 요구사항:
# 다음 `customer_data` 데이터프레임을 생성하세요:
# import pandas as pd
# data = {'CustomerID': [101, 102, 101, 103, 102, 104],
#         'Name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'David'],
#         'Email': ['a@example.com', 'b@example.com', 'a@example.com', 'c@example.com', 'b@example.com', 'd@example.com'],
#         'OrderDate': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-03', '2023-01-02', '2023-01-04']}
# customer_data = pd.DataFrame(data)
# 생성된 데이터프레임에서 다음 작업을 수행하고 각각의 결과를 출력하세요:
# 1.  **전체 행을 기준**으로 완전히 중복되는 모든 행(첫 등장 포함)을 식별하고 출력하세요. (힌트: `keep=False` 사용)
# 2.  **전체 행을 기준**으로 완전히 중복되는 모든 행을 제거하고 출력하세요. (힌트: `keep=False` 사용)
# 3.  **'CustomerID' 컬럼만을 기준**으로 중복되는 모든 행(첫 등장 포함)을 식별하고 출력하세요. (힌트: `subset`, `keep=False` 사용)
# 4.  **'CustomerID' 컬럼만을 기준**으로 중복되는 모든 행을 제거하고 출력하세요. (힌트: `subset`, `keep=False` 사용)
# 학습 목표: Pandas DataFrame에서 `duplicated()`와 `drop_duplicates()` 메서드를 사용하여 중복되는 행을 효율적으로 식별하고 제거하는 방법을 학습합니다. `keep` 및 `subset` 매개변수의 다양한 활용법을 이해합니다.
# 가이드:
# - `duplicated()`는 중복 여부를 불리언 Series로 반환합니다.
# - `drop_duplicates()`는 중복된 행을 실제로 제거합니다.
# - `keep='first'`, `keep='last'`, `keep=False` 옵션의 차이를 이해하고 적용하세요.
# - `subset` 매개변수로 특정 컬럼(들)만 기준으로 중복을 검사할 수 있습니다.

# --- [최초 나의 코딩] ---
import pandas as pd
data = {'CustomerID': [101, 102, 101, 103, 102, 104],
        'Name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'David'],
        'Email': ['a@example.com', 'b@example.com', 'a@example.com', 'c@example.com', 'b@example.com', 'd@example.com'],
        'OrderDate': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-03', '2023-01-02', '2023-01-04']}
customer_data = pd.DataFrame(data)

print("\n --- Origin: Customer Data --- ")
print(customer_data)

duplicated_row = customer_data.duplicated(keep=False)
print("\n --- Duplicated Row --- ")
print(customer_data[duplicated_row])

print("\n --- Duplicated Row deleted --- ")
print(customer_data.drop_duplicates(keep=False))

duplicated_ID = customer_data.duplicated(subset="CustomerID", keep=False)
print("\n --- Duplicated Customer ID --- ")
print(customer_data[duplicated_ID])

print("\n --- Duplicated Customer ID deleted --- ")
print(customer_data.drop_duplicates(subset="CustomerID", keep=False))


# --- [코드 실행 결과] ---
"""
 --- Origin: Customer Data ---
   CustomerID     Name           Email   OrderDate
0         101    Alice   a@example.com  2023-01-01
1         102      Bob   b@example.com  2023-01-02
2         101    Alice   a@example.com  2023-01-01
3         103  Charlie   c@example.com  2023-01-03
4         102      Bob   b@example.com  2023-01-02
5         104    David   d@example.com  2023-01-04

 --- Duplicated Row ---
   CustomerID   Name         Email   OrderDate
0         101  Alice a@example.com  2023-01-01
1         102    Bob b@example.com  2023-01-02
2         101  Alice a@example.com  2023-01-01
4         102    Bob b@example.com  2023-01-02

 --- Duplicated Row deleted ---
   CustomerID     Name           Email   OrderDate
3         103  Charlie   c@example.com  2023-01-03
5         104    David   d@example.com  2023-01-04

 --- Duplicated Customer ID ---
   CustomerID     Name           Email   OrderDate
0         101    Alice   a@example.com  2023-01-01
1         102      Bob   b@example.com  2023-01-02
2         101    Alice   a@example.com  2023-01-01
4         102      Bob   b@example.com  2023-01-02

 --- Duplicated Customer ID deleted ---
   CustomerID     Name           Email   OrderDate
3         103  Charlie   c@example.com  2023-01-03
5         104    David   d@example.com  2023-01-04
"""

# --- [피드백] ---
"""
훌륭합니다! 문제 5의 모든 요구사항을 정확하게 이해하고 `duplicated()`와 `drop_duplicates()` 메서드를 다양하게 활용하여 중복값 처리 방법을 잘 보여주셨습니다.

몇 가지 세부 사항과 더 명확하게 할 수 있는 부분이 있어 피드백 드립니다.

1.  **전체 행 기준 중복 확인 및 제거 (keep=False)**:
    * `customer_data.duplicated(keep=False)`: 전체 행을 기준으로 완전히 중복되는 모든 행(첫 등장 포함)을 True로 표시하여 잘 추출했습니다. 이는 중복된 데이터를 모두 보고 싶을 때 유용합니다.
    * `customer_data.drop_duplicates(keep=False)`: 중복되는 행을 모두 제거했습니다. 이 경우 중복된 쌍이 완전히 사라지므로, 중복된 값 중 **유일한 값만** 남게 됩니다. 이 동작은 문제 의도에 부합합니다. (원본에서 `(101, 'Alice', 'a@example.com', '2023-01-01')`은 0번, 2번 인덱스에 두 번 나옵니다. `keep=False`는 둘 다 삭제하여 아무것도 남기지 않습니다. `(102, 'Bob', 'b@example.com', '2023-01-02')`도 마찬가지입니다.)

2.  **'CustomerID' 기준 중복 확인 및 제거 (keep=False)**:
    * `customer_data.duplicated(subset="CustomerID", keep=False)`: 'CustomerID'만을 기준으로 중복되는 모든 행을 잘 확인했습니다. 이 역시 `keep=False`가 적용되어 `CustomerID`가 101인 두 행(인덱스 0, 2)과 102인 두 행(인덱스 1, 4)이 모두 중복으로 간주됩니다.
    * `customer_data.drop_duplicates(subset="CustomerID", keep=False)`: 이 경우, `CustomerID`가 101인 모든 행이 제거되고, `CustomerID`가 102인 모든 행이 제거됩니다. 따라서 결과적으로 `CustomerID`가 101, 102인 행은 하나도 남지 않고, 103, 104인 행만 남게 됩니다. 이 또한 `keep=False`의 정확한 동작입니다.

**개선할 점**:
* 문제의 3번 요구사항 "첫 번째 등장하는 행은 제외하고, 이후 중복되는 행만 True로 표시"는 `df.duplicated()`의 기본값인 `keep='first'`를 사용했을 때의 동작과 일치합니다. 현재 `keep=False`를 사용했기 때문에 모든 중복값을 표시하지만, 문제의 정확한 의도에 맞추려면 `keep='first'`를 사용하는 것이 더 적절합니다.

전반적으로 `duplicated()`와 `drop_duplicates()`의 강력한 기능을 잘 활용하셨습니다. 특히 `keep` 매개변수의 의미를 직접 실험하며 이해하신 점이 돋보입니다.
"""

# --- [모범 답안] ---
import pandas as pd
data = {'CustomerID': [101, 102, 101, 103, 102, 104],
        'Name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'David'],
        'Email': ['a@example.com', 'b@example.com', 'a@example.com', 'c@example.com', 'b@example.com', 'd@example.com'],
        'OrderDate': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-03', '2023-01-02', '2023-01-04']}
customer_data = pd.DataFrame(data)

print("--- 원본 customer_data ---")
print(customer_data)

# 1. 전체 행을 기준으로 완전히 중복되는 행 확인 (모든 중복 인스턴스 표시)
# keep=False는 중복되는 모든 행을 True로 표시합니다.
df_all_duplicates_check = customer_data.duplicated(keep=False)
print("\n--- 1. 전체 행 기준, 모든 중복되는 행 ---")
print(customer_data[df_all_duplicates_check])

# 2. 전체 행을 기준으로 완전히 중복되는 행 제거 (모든 중복 인스턴스 삭제)
# keep=False는 중복된 행을 모두 제거하여 유일한 행만 남깁니다.
# (예: (101, Alice, a@example.com, 2023-01-01)은 2개이므로 둘 다 제거됨)
df_no_full_duplicates = customer_data.drop_duplicates(keep=False)
print("\n--- 2. 전체 행 기준, 중복되는 행 모두 제거 후 ---")
print(df_no_full_duplicates)

# 3. 'CustomerID' 컬럼만을 기준으로 중복되는 행 확인 (첫 번째는 제외, 이후 중복만 True)
# keep='first' (기본값): 첫 번째 등장하는 중복은 False, 이후 중복만 True로 표시됩니다.
df_customer_id_duplicates_check = customer_data.duplicated(subset='CustomerID', keep='first')
print("\n--- 3. 'CustomerID' 기준, 첫 번째 제외한 중복되는 행 ---")
print(customer_data[df_customer_id_duplicates_check])

# 4. 'CustomerID' 컬럼만을 기준으로 중복되는 행 제거 (첫 번째 등장하는 행 유지)
# keep='first' (기본값): 중복될 경우 첫 번째 등장하는 행을 유지합니다.
df_unique_customer_id = customer_data.drop_duplicates(subset='CustomerID', keep='first')
print("\n--- 4. 'CustomerID' 기준, 중복 제거 후 (첫 번째 유지) ---")
print(df_unique_customer_id)


# --- [학습 기록] ---
"""
**학습 질문**: `DataFrame`에서 중복된 행을 식별하고 제거하는 다양한 방법은 무엇일까? 특히 전체 행 기준으로 또는 특정 컬럼(들) 기준으로 중복을 처리할 때 `duplicated()`와 `drop_duplicates()`의 `keep` 및 `subset` 매개변수는 어떻게 활용해야 할까?

**문제 해결**:
1.  **DataFrame 생성 및 원본 확인**: 주어진 고객 데이터를 사용하여 `customer_data` DataFrame을 생성하고 원본을 출력하여 데이터 구조를 확인했습니다.
2.  **전체 행 중복 확인 및 제거 (`keep=False`)**:
    * `customer_data.duplicated(keep=False)`: 이 코드는 DataFrame의 **모든 컬럼 값**이 동일한 행들을 찾아 True로 표시했습니다. `keep=False`는 중복되는 모든 인스턴스(첫 번째 등장하는 것도 포함)를 True로 반환하여, 모든 중복된 행을 확인하고자 할 때 유용합니다.
    * `customer_data.drop_duplicates(keep=False)`: `keep=False` 옵션을 사용하면, 완전히 중복되는 행 그룹에서 **모든 인스턴스를 제거**합니다. 즉, 중복된 행 쌍은 모두 사라지고 유일한 행만 남게 됩니다.
3.  **특정 컬럼 기준 중복 확인 및 제거 (`subset='CustomerID'`, `keep=False` 또는 `keep='first'`)**:
    * `customer_data.duplicated(subset="CustomerID", keep=False)`: 'CustomerID' 컬럼의 값만을 기준으로 중복을 검사하고, 중복되는 모든 'CustomerID'를 가진 행들을 True로 표시했습니다. 이 역시 `keep=False`가 적용되어 해당 ID를 가진 모든 행이 중복으로 간주됩니다.
    * `customer_data.drop_duplicates(subset="CustomerID", keep=False)`: 이 코드는 'CustomerID' 기준으로 중복되는 모든 행을 제거합니다. 즉, `CustomerID`가 101인 모든 행과 102인 모든 행이 삭제되어, 103과 104만 남게 됩니다.
    * **모범 답안에서는 `keep='first'`를 사용**: 실제 사용 시 `drop_duplicates(subset='컬럼명', keep='first')`는 해당 `CustomerID`를 가진 첫 번째 행만 남기고 나머지 중복된 행을 제거하는 더 일반적인 시나리오를 보여줍니다. 이 경우, 고객별 고유한 레코드를 유지하면서 중복을 정리할 수 있습니다.

**추가 학습**:
* **`duplicated()`의 `keep` 매개변수**:
    * `keep='first'` (기본값): 첫 번째 중복은 `False`로, 이후 중복은 `True`로 표시합니다.
    * `keep='last'`: 마지막 중복은 `False`로, 그 이전의 중복은 `True`로 표시합니다.
    * `keep=False`: 모든 중복되는 인스턴스(첫 등장 포함)를 `True`로 표시합니다.
* **`drop_duplicates()`의 `keep` 매개변수**:
    * `keep='first'` (기본값): 중복되는 행 그룹에서 **첫 번째 행만 유지**하고 나머지를 삭제합니다. 가장 흔하게 사용됩니다.
    * `keep='last'`: 중복되는 행 그룹에서 **마지막 행만 유지**하고 나머지를 삭제합니다.
    * `keep=False`: 중복되는 행 그룹에서 **모든 행을 삭제**합니다. (원본에 유일한 행만 남기고자 할 때 사용)
* **`subset` 매개변수**: 특정 컬럼(들)의 값만을 기준으로 중복 여부를 판단하고자 할 때 사용합니다. 예를 들어, `subset=['컬럼1', '컬럼2']`와 같이 리스트 형태로 여러 컬럼을 지정할 수 있습니다.

* **[공인회계사 업무 관련 추가 학습]**:
    `duplicated()`와 `drop_duplicates()`를 활용한 중복값 처리는 공인회계사(CPA)가 **재무 데이터의 무결성을 확보하고, 정확한 분석 및 보고를 수행하는 데 필수적인 데이터 정제 작업**입니다. 중복 데이터는 분석 결과를 왜곡하고 비효율성을 야기할 수 있기 때문입니다.

    * **거래의 이중 기록 방지 (전체 행 중복 제거)**:
        * **예시**: 회계 시스템에서 특정 거래가 실수로 두 번 입력되어 **모든 정보(거래일자, 계정, 금액, 거래처 등)가 완전히 동일한 행**이 발생할 수 있습니다. `drop_duplicates(keep='first')`나 `drop_duplicates(keep=False)`를 사용하여 이러한 이중 기록을 제거하여, **매출, 비용, 현금 흐름 등의 집계가 과대/과소 계상되는 것을 방지**합니다.
        * **활용**: CPA는 총계정원장, 전표, 매입/매출장 등의 데이터를 분석할 때, **재무제표의 금액적 오류를 야기할 수 있는 완전 중복 거래를 식별하고 제거**하여 재무 보고의 정확성을 확보합니다.

    * **마스터 데이터의 유일성 확보 (특정 컬럼 기준 중복 제거)**:
        * **예시**: **고객 마스터, 공급업체 마스터, 품목 마스터** 등에는 각 엔티티(고객, 공급업체, 품목)를 식별하는 고유 ID가 있어야 합니다. 만약 `CustomerID`나 `VendorID`가 중복되는 경우, 이는 동일한 고객/공급업체가 여러 번 등록되었거나 데이터 입력 오류일 수 있습니다. `drop_duplicates(subset=['CustomerID'], keep='first')`를 사용하여 **각 고객/공급업체에 대한 단일하고 유일한 레코드**만 남깁니다.
        * **활용**: CPA는 데이터 기반 감사에서 **데이터의 정확성과 신뢰성**을 검증할 때, 마스터 데이터의 중복 여부를 확인하고 제거하여 **관계형 데이터베이스의 무결성을 유지**합니다. 이는 향후 데이터 조인(join)이나 집계 분석의 정확도를 보장합니다.

    * **데이터 분석의 효율성 증대**:
        * 중복된 데이터는 불필요한 연산 부하를 증가시키고, 분석 결과의 해석을 어렵게 만듭니다. 중복 제거를 통해 **데이터셋의 크기를 줄이고, 분석 속도를 향상**시키며, **의미 있는 고유한 정보에 집중**할 수 있도록 돕습니다.
        * **활용**: CPA는 대용량 거래 데이터를 다룰 때 중복 제거를 통해 **보고서 생성 시간 단축, 모델 학습 효율성 향상** 등 전반적인 데이터 분석 프로세스의 효율성을 높일 수 있습니다.

    `duplicated()`와 `drop_duplicates()`는 CPA가 **데이터 품질을 관리하고, 재무 보고 및 감사 분석의 신뢰성과 효율성을 극대화하는 데 필수적인 기초 역량**이라고 할 수 있습니다.
"""
