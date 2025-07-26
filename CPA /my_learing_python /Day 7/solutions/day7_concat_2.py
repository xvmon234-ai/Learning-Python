# ==============================================================================
# [문제 2-2] 고객 연락처 및 주소 정보 수평 결합 (Day 7 학습 내용)
# ==============================================================================

# --- [최초 나의 코딩] ---
import pandas as pd

data_contact = {'CustomerID': [1, 2, 3, 5], # CustomerID 5는 address_info_df에 없음
                'Name': ['Alice', 'Bob', 'Charlie', 'Eve'],
                'Email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'eve@example.com']}
contact_info_df = pd.DataFrame(data_contact).set_index('CustomerID')

data_address = {'CustomerID': [1, 2, 4, 3], # CustomerID 4는 contact_info_df에 없음
                'Address': ['123 Main St', '456 Oak Ave', '789 Pine Ln', '101 Maple Dr'],
                'ZipCode': ['10001', '90001', '60001', '70001']}
address_info_df = pd.DataFrame(data_address).set_index('CustomerID')

# 내가 제시해주는 답안 (주석 유지)
# pd.concat에 axis=1과 ignore_index=True를 함께 사용하면 CustomerID 인덱스 정렬이 무시됩니다.
# 이 코드는 문제의 의도와 다르게 작동합니다.
joined_customer_df = pd.concat([contact_info_df, address_info_df], axis=1, ignore_index=True)

print("\n --- Joined Customer Dataframe --- \n")
print(joined_customer_df)

# --- [코드 실행 결과] ---
"""
 --- Joined Customer Dataframe ---

      Name                Email      Address ZipCode
0     Alice      alice@example.com          NaN     NaN
1       Bob        bob@example.com          NaN     NaN
2   Charlie    charlie@example.com          NaN     NaN
3       Eve        eve@example.com          NaN     NaN
4       NaN                      NaN  123 Main St   10001
5       NaN                      NaN  456 Oak Ave   90001
6       NaN                      NaN  789 Pine Ln   60001
7       NaN                      NaN  101 Maple Dr  70001
"""

# --- [피드백] ---
"""
문제 2-2의 목표인 `CustomerID`를 기준으로 하는 수평 연결을 시도하신 점은 좋았으나, `pd.concat()` 함수에서 `axis=1`과 `ignore_index=True`를 함께 사용한 결과가 문제의 의도와는 다르게 나왔습니다.

1.  **`axis=1`의 올바른 사용**: `axis=1`을 사용하여 DataFrame을 수평(열 방향)으로 연결하려는 시도는 정확했습니다. 이는 DataFrame 옆에 다른 DataFrame의 열을 붙이는 작업을 의미합니다.

2.  **`ignore_index=True`의 오해 (수평 결합 시)**:
    * **수직 결합(`axis=0`)**: `ignore_index=True`는 원본 DataFrame들의 행 인덱스를 무시하고 새롭고 연속적인 행 인덱스를 부여합니다. 이 경우 매우 유용합니다.
    * **수평 결합(`axis=1`)**: `ignore_index=True`는 원본 DataFrame들의 **열 인덱스(컬럼명)**를 무시하고 0부터 시작하는 새로운 숫자형 열 인덱스를 부여합니다. 이 매개변수는 **행 인덱스(Row Index)의 정렬을 무시하지 않습니다.** 오히려, 각 DataFrame의 *열(Column)*을 순서대로 가져와 새로운 열 이름을 부여하는 방식으로 동작합니다. 결과적으로 `contact_info_df`의 모든 행이 먼저 나오고, 그 다음에 `address_info_df`의 모든 행이 나오면서 인덱스 `CustomerID` 기준으로 데이터가 정렬되지 않고 positional하게 붙어버려 `NaN`이 많이 생성된 것을 볼 수 있습니다.

3.  **문제의 의도**: 문제의 목표는 `CustomerID` 인덱스를 기준으로 각 고객의 연락처와 주소 정보를 합쳐서 '고객의 통합된 프로필'을 만드는 것이었습니다. 이는 사실상 `CustomerID` 인덱스를 기반으로 하는 `outer` 조인과 같은 결과를 기대합니다.

따라서, `pd.concat()`를 사용하여 인덱스 기반의 수평 결합을 수행하려면 `ignore_index=True`를 사용하지 않아야 합니다. `pd.concat()`는 기본적으로 `axis=1`일 때 **공통된 인덱스를 기준으로 열을 정렬하여 붙이는 동작**을 수행합니다. 또는 `pd.merge()`를 사용하여 명시적으로 인덱스를 기준으로 조인하는 방법도 있습니다.
"""

# --- [모범 답안] ---
# pd.concat()을 인덱스 기반으로 수평 결합하려면 `ignore_index=True`를 제거해야 합니다.
# 이 경우 pd.concat()은 기본적으로 인덱스를 기준으로 매칭됩니다.
# 또한, 명시적으로 merge 함수를 사용하는 것이 의도를 더 잘 나타낼 수 있습니다.

# 방법 1: pd.concat() 사용 (ignore_index=True 제거)
# pd.concat은 axis=1일 때 기본적으로 인덱스를 기준으로 정렬합니다.
correct_joined_concat_df = pd.concat([contact_info_df, address_info_df], axis=1)

print("\n--- 모범 답안 1: pd.concat()을 이용한 인덱스 기반 수평 결합 ---")
print(correct_joined_concat_df)

# 방법 2: pd.merge() 사용 (인덱스 기반 outer 조인)
# CustomerID가 인덱스이므로 left_index=True, right_index=True를 사용하고 how='outer'로 모든 정보 포함
correct_joined_merge_df = pd.merge(
    contact_info_df,
    address_info_df,
    left_index=True,
    right_index=True,
    how='outer'
)

print("\n--- 모범 답안 2: pd.merge()를 이용한 인덱스 기반 Outer Join ---")
print(correct_joined_merge_df)


# --- 결과 검증 (추가) ---
# 예상 결과 (어떤 방식으로 합치든 동일해야 함)
expected_data_concat = {
    'Name': ['Alice', 'Bob', 'Charlie', pd.NA, 'Eve'],
    'Email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', pd.NA, 'eve@example.com'],
    'Address': ['123 Main St', '456 Oak Ave', '101 Maple Dr', '789 Pine Ln', pd.NA],
    'ZipCode': ['10001', '90001', '70001', '60001', pd.NA]
}
expected_index_concat = [1, 2, 3, 4, 5] # CustomerID 순서
expected_df_concat = pd.DataFrame(expected_data_concat, index=expected_index_concat)
expected_df_concat.index.name = 'CustomerID'

# 타입 불일치 가능성을 줄이기 위해 astype(str)로 변환 후 비교
# pd.NA와 np.nan 처리 및 컬럼 순서 유연하게 비교
pd.testing.assert_frame_equal(
    correct_joined_concat_df.sort_index().astype(str),
    expected_df_concat.sort_index().astype(str),
    check_dtype=False # NaN/pd.NA 처리 및 타입 불일치 가능성 고려
)
pd.testing.assert_frame_equal(
    correct_joined_merge_df.sort_index().astype(str),
    expected_df_concat.sort_index().astype(str),
    check_dtype=False # NaN/pd.NA 처리 및 타입 불일치 가능성 고려
)

print("\n✔ 모범 답안 DataFrame이 예상과 일치합니다. 성공!")


# --- [학습 기록] ---
"""
**학습 질문**: 서로 다른 데이터프레임에 고객 ID를 인덱스로 하여 분리 저장된 연락처와 주소 정보를 **고객 ID를 기준으로 합치고 싶을 때** 어떻게 해야 할까? 특히, 한쪽에만 존재하는 고객 정보도 모두 포함시키려면? `pd.concat(axis=1)`과 `pd.merge()`는 어떤 차이가 있을까?

**문제 해결**:
1.  **데이터프레임 준비**: `CustomerID`를 인덱스로 하는 `contact_info_df`와 `address_info_df`를 생성했습니다. 두 DataFrame에는 `CustomerID`가 겹치거나 한쪽에만 존재하는 경우가 있습니다.
2.  **`pd.concat()`의 `axis=1` 동작 이해**:
    * `pd.concat([df1, df2], axis=1)`: 여러 DataFrame을 열(컬럼)을 기준으로 연결합니다. 이때, **기본적으로 행 인덱스(Row Index)를 기준으로 정렬(align)하여 붙입니다.** 즉, 동일한 인덱스를 가진 행끼리 옆으로 합쳐지고, 한쪽에만 있는 인덱스의 경우 다른 쪽 컬럼들은 `NaN`으로 채워집니다. 이는 `outer` 조인과 유사한 결과를 만듭니다.
    * **`ignore_index=True`의 주의**: `axis=1`일 때 `ignore_index=True`를 사용하면 **열 인덱스(컬럼명)를 새로 부여**하게 됩니다. 하지만 이는 행 인덱스의 정렬 기능까지 무시하게 만들어, 각 DataFrame의 행들을 단순히 순서대로 옆에 붙여버리는 결과를 초래합니다. (예: 첫 번째 DataFrame의 첫 번째 행 옆에 두 번째 DataFrame의 첫 번째 행이 붙는 식). 이는 `CustomerID` 기준으로 정보를 합치려는 문제의 의도와는 맞지 않습니다.

3.  **`pd.merge()`를 통한 인덱스 기반 조인**:
    * `pd.merge(df1, df2, left_index=True, right_index=True, how='outer')`: `pd.merge()` 함수는 인덱스를 기준으로 조인할 때 `left_index=True`와 `right_index=True`를 사용합니다. `how='outer'`를 사용하여 양쪽 DataFrame의 모든 인덱스(CustomerID)를 결과에 포함시키고, 매칭되지 않는 부분은 `NaN`으로 채웁니다. 이는 `pd.concat(..., axis=1)`이 기본적으로 수행하는 인덱스 기반 정렬 동작과 동일한 결과를 생성합니다.
4.  **결과 확인**: 올바른 방법으로 연결된 DataFrame에서는 `CustomerID` 1, 2, 3이 정확히 합쳐졌고, `CustomerID` 4(주소만)와 5(연락처만)의 정보도 `NaN`과 함께 모두 포함된 것을 확인했습니다.

**추가 학습 (공인회계사 업무와의 관련성 및 `pd.concat(axis=1)`/인덱스 기반 Merge의 활용)**:

CPA가 데이터를 분석하는 업무에서 `pd.concat(axis=1)` 또는 인덱스 기반의 `pd.merge()`는 **고객, 공급업체, 자산 등 '개별 엔티티(Entity)'의 통합된 프로필을 생성하고, 엔티티별 정보의 완전성과 일관성을 검증**하는 데 필수적인 도구입니다.

* **통합된 엔티티 프로필 생성 (360-degree View)**:
    * **예시**: **모든 고객 ID를 인덱스로 하는 마스터 고객 리스트**를 기준으로, 고객별 '연락처 정보', '주소 정보', '구매 이력 요약', '미수금 잔액' 등 **다양한 시스템에 흩어져 있는 정보를 수평으로 연결**하여 `고객 360도 뷰`를 만듭니다.
    * **활용**: CPA는 이를 통해 특정 고객의 재무 상태, 거래 패턴, 연락처 정보 등을 한눈에 파악하여 감사 목적에 맞는 심층 분석(예: 대규모 미수금 고객의 신용 평가, 불량 고객 관리)을 수행할 수 있습니다.

* **데이터 일관성 및 정합성 검증**:
    * **예시**: ERP 시스템의 `벤더 마스터 데이터`와 구매 시스템의 `실제 거래 발생 벤더 데이터`를 `벤더 ID`를 인덱스로 하는 DataFrame으로 만든 후 수평 연결합니다.
    * **활용**: 양쪽에 모두 존재하는 벤더의 정보가 일치하는지 확인하고, **한쪽에만 존재하는 벤더(예: ERP에 미등록된 신규 벤더, 구매 시스템에서 더 이상 사용하지 않는 벤더)**를 식별하여 데이터의 불일치 원인을 조사하고 마스터 데이터 관리 절차의 준수 여부를 감사합니다.

* **감사 증거 연결 및 분석**:
    * **예시**: 각 '거래 ID'를 인덱스로 하는 **'거래 승인 기록' DataFrame**과 **'실제 회계 전표 기록' DataFrame**을 수평 연결하여, 모든 거래가 적절하게 승인되었는지, 승인된 거래가 모두 회계에 반영되었는지 등을 검증합니다.
    * **활용**: '자산 ID'를 인덱스로 하는 **'자산 대장'**과 **'보험 가입 현황'**을 수평 연결하여 모든 자산이 적절히 보험에 가입되어 있는지 확인하는 등, 보조적인 정보들을 통합하여 감사 범위를 확장합니다.

* **보고서 포맷팅 및 가독성 향상**:
    * CPA는 다양한 원천에서 얻은 데이터를 최종 보고서 형태로 가공할 때, 관련 정보를 옆으로 붙여 가독성을 높이고 분석가가 한눈에 필요한 정보를 볼 수 있도록 만듭니다.

`pd.concat(axis=1)` (인덱스 정렬) 또는 인덱스 기반 `pd.merge()`는 CPA가 **개별 엔티티에 대한 풍부한 정보를 통합하고, 분산된 정보 간의 일관성을 검증하며, 감사 및 재무 분석의 효율성을 극대화**하는 데 매우 유용한 고급 데이터 통합 기법입니다.
"""
