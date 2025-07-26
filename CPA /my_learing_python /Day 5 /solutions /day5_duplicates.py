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
   CustomerID     Name          Email   OrderDate
0         101    Alice  a@example.com  2023-01-01
1         102      Bob  b@example.com  2023-01-02
2         101    Alice  a@example.com  2023-01-01
3         103  Charlie  c@example.com  2023-01-03
4         102      Bob  b@example.com  2023-01-02
5         104    David  d@example.com  2023-01-04

 --- Duplicated Row ---
   CustomerID   Name          Email   OrderDate
0         101  Alice  a@example.com  2023-01-01
1         102    Bob  b@example.com  2023-01-02
2         101  Alice  a@example.com  2023-01-01
4         102    Bob  b@example.com  2023-01-02

 --- Duplicated Row deleted ---
   CustomerID     Name          Email   OrderDate
3         103  Charlie  c@example.com  2023-01-03
5         104    David  d@example.com  2023-01-04

 --- Duplicated Customer ID ---
   CustomerID     Name          Email   OrderDate
0         101    Alice  a@example.com  2023-01-01
1         102      Bob  b@example.com  2023-01-02
2         101    Alice  a@example.com  2023-01-01
4         102      Bob  b@example.com  2023-01-02

 --- Duplicated Customer ID deleted ---
   CustomerID     Name          Email   OrderDate
3         103  Charlie  c@example.com  2023-01-03
5         104    David  d@example.com  2023-01-04
"""

# --- [피드백] ---
"""
훌륭합니다! 문제 6의 모든 요구사항을 정확하게 이해하고 `duplicated()`와 `drop_duplicates()` 메서드를 다양하게 활용하여 중복값 처리 방법을 잘 보여주셨습니다.

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
