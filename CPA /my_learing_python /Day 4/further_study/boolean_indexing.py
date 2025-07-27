# ==============================================================================
# [문제 4.4] 추가 학습: 불리언 인덱싱의 원리 및 CPA 활용
# ==============================================================================

# 데이터 준비 예시
# (이론 설명을 위한 데이터로, 문제 4.3의 데이터와 동일합니다.)
students_data = """StudentID,Name,Math,English,Grade
S001,Alice,90,85,A
S002,Bob,78,80,B
S003,Charlie,95,92,A
S004,David,60,70,C
"""
df_students = pd.read_csv(StringIO(students_data)).set_index("StudentID")

print("--- 예시 DataFrame (df_students) ---")
print(df_students)

# 핵심 이론: 불리언 인덱싱 (Boolean Indexing)
"""
Pandas에서 데이터를 필터링하는 가장 강력하고 유연한 방법 중 하나는 **불리언 인덱싱 (Boolean Indexing)**입니다. 이는 특정 조건을 만족하는 행(또는 열)만을 선택할 때 사용됩니다.

**원리**:
1.  **조건식 생성**: 먼저, DataFrame의 특정 컬럼에 대해 조건을 적용하여 `True` 또는 `False` 값으로 이루어진 `Series`를 생성합니다. 이 `Series`의 인덱스는 원본 DataFrame의 인덱스와 동일해야 합니다.
    * 예: `df_students["Math"] >= 80`
        * 이 연산의 결과는 각 학생의 'Math' 점수가 80점 이상인지 여부를 나타내는 `True/False` Series가 됩니다.
        * `S001: True, S002: False, S003: True, S004: False`

2.  **불리언 Series 적용**: 이렇게 생성된 불리언 Series를 원본 DataFrame의 대괄호 `[]` 안에 넣어줍니다.
    * 예: `df_students[df_students["Math"] >= 80]`
        * Pandas는 이 불리언 Series를 사용하여 `True`에 해당하는 행들만 선택하여 새로운 DataFrame을 반환합니다. `False`에 해당하는 행은 결과에서 제외됩니다.

**주요 특징**:
* **유연성**: 숫자, 문자열, 날짜 등 다양한 데이터 타입에 조건을 적용할 수 있습니다.
* **직관성**: 조건식을 자연어처럼 작성할 수 있어 코드의 가독성이 높습니다.
* **다중 조건**: `&` (AND), `|` (OR), `~` (NOT) 연산자를 사용하여 여러 조건을 조합할 수 있습니다. 이때 각 개별 조건은 반드시 소괄호 `()`로 묶어야 합니다.

**왜 중요한가?**:
실제 데이터 분석에서는 특정 기준을 만족하는 데이터만을 추출하여 분석하는 경우가 대부분입니다. 불리언 인덱싱은 이러한 '조건부 선택'을 매우 효율적이고 강력하게 수행할 수 있게 해주므로, 데이터 탐색, 클리닝, 분석의 핵심적인 기술입니다.
"""

# 불리언 Series 생성 과정 이해 및 적용
math_condition = df_students["Math"] >= 80
print("\n--- 'Math' 점수 80점 이상 조건 (불리언 Series) 생성 ---")
print(math_condition)
print(f"타입: {type(math_condition)}")

# 불리언 Series를 이용한 필터링
filtered_students = df_students[math_condition]
print("\n--- 불리언 Series를 적용하여 필터링된 학생들 (수학 80점 이상) ---")
print(filtered_students)

# 다른 조건 예시: Grade가 'A'인 학생
grade_A_students = df_students[df_students["Grade"] == "A"]
print("\n--- 'Grade'가 'A'인 학생들 필터링 ---")
print(grade_A_students)

# 다중 조건 필터링 예시 (수학 80점 이상이면서 등급이 'A'인 학생)
multi_condition_students = df_students[(df_students["Math"] >= 80) & (df_students["Grade"] == "A")]
print("\n--- 수학 80점 이상 & 등급 'A'인 학생들 필터링 ---")
print(multi_condition_students)


print("\n[공인회계사(CPA) 업무와의 관련성]:")
"""
Pandas의 **불리언 인덱싱을 활용한 단일 조건 필터링**은 공인회계사(CPA)가
**대량의 재무 및 운영 데이터에서 특정 기준을 충족하는 정보를 신속하게 식별하고 추출**하는 데 매우 필수적인 기능입니다.
이는 감사 절차, 재무 분석, 데이터 검증 등 다양한 업무에 활용됩니다.

* **매출/비용의 유의성 검토**:
    * **활용**: 특정 금액(예: 100만 원)을 초과하는 **고액의 매출 또는 비용 거래**만 필터링하여 검토할 때 사용합니다. `df_transactions[df_transactions['Amount'] >= 1000000]`와 같이 필터링하여 잠재적 위험 거래를 집중적으로 확인합니다.
    * **의미**: CPA는 이를 통해 내부 통제상의 허점이나 부정의 가능성을 탐지하고, 중요성에 기반한 감사 접근 방식을 적용할 수 있습니다.

* **특정 조건 만족하는 계약/자산 식별**:
    * **활용**: '계약 종료일'이 특정 날짜(예: 이번 분기 말) 이전에 도래하는 계약들만 필터링하거나, '자산의 장부가치'가 일정 금액 이상인 유형 자산만 추출하여 **재평가 필요성 또는 손상 징후**를 파악합니다.
    * **의미**: `df_contracts[df_contracts['EndDate'] < '2025-03-31']` 또는 `df_assets[df_assets['Book_Value'] > 500000]` 와 같이 사용하여 관련 회계 처리의 적절성을 검토합니다.

* **재고 또는 채권의 건전성 평가**:
    * **활용**: '재고 평가액'이 일정 기준 이하로 떨어지는 품목이나, '미수금 회수 기한'이 지난 채권들만 필터링하여 **재고 자산의 진부화 또는 채권의 회수 불능 가능성**을 평가합니다.
    * **의미**: 이는 충당금 설정 등 관련 회계 추정의 적정성을 검토하는 데 중요한 데이터를 제공합니다.

* **특정 부서/사업부의 성과 분석**:
    * **활용**: 특정 '부서 코드'에 해당하는 데이터만 필터링하여 해당 부서의 손익이나 비용 구조를 심층적으로 분석합니다.
    * **의미**: `df_expenses[df_expenses['Department_Code'] == 'SALES']`와 같이 사용함으로써, CPA는 부서별 성과를 평가하고 효율성을 증대시킬 방안을 모색할 수 있습니다.

결론적으로, 불리언 인덱싱을 통한 단일 조건 필터링은 CPA가 **정의된 기준에 따라 대량의 데이터에서 핵심적인 정보를 선별적으로 추출하고, 이를 기반으로 재무 분석, 감사 위험 평가, 회계 처리의 적정성 검토 등 다양한 실무를 수행하는 데 필수적인 기초 데이터 핸들링 기술**입니다.
"""


# ==============================================================================
# [추가 학습] Pandas drop() 메서드의 axis와 inplace 파라미터 심층 이해
# ==============================================================================

# 1. axis (축) 파라미터: '어떤 방향으로 작업할까?'
"""
`axis` 파라미터는 Pandas 함수가 **어떤 축(방향)**을 따라 연산을 수행할지 지정합니다.
DataFrame은 2차원 구조이므로 두 개의 주요 축을 가집니다.

-   **`axis=0` (또는 `axis='index'`)**:
    * **행(Row)**을 따라 연산을 수행합니다.
    * 기본값입니다. 예를 들어, `df.sum(axis=0)`은 각 **컬럼별로** 합계를 계산합니다.
    * `df.drop()` 메서드에서 `axis=0`은 특정 **행을 삭제**하라는 의미입니다.
    * 상상해보세요: 위에서 아래로(행 방향으로) 스캔하며 특정 행을 찾거나, 행들을 합치는 작업입니다.

-   **`axis=1` (또는 `axis='columns'`)**:
    * **열(Column)**을 따라 연산을 수행합니다.
    * `df.sum(axis=1)`은 각 **행별로** 합계를 계산합니다.
    * `df.drop()` 메서드에서 `axis=1`은 특정 **컬럼(열)을 삭제**하라는 의미입니다.
    * 상상해보세요: 왼쪽에서 오른쪽으로(컬럼 방향으로) 스캔하며 특정 컬럼을 찾거나, 컬럼들을 합치는 작업입니다.

예시 (`drop` 메서드에서 `axis`):
-   `df.drop(rows_to_drop, axis=0)`: `rows_to_drop`에 해당하는 **행**을 삭제합니다.
-   `df.drop(columns_to_drop, axis=1)`: `columns_to_drop`에 해당하는 **컬럼**을 삭제합니다.

헷갈린다면, **"axis=1은 '원' (컬럼)을 제거한다"**라고 연상하면 좋습니다.
"""

# 2. inplace 파라미터: '원본을 바꿀까, 새 복사본을 만들까?'
"""
`inplace` 파라미터는 Pandas의 많은 메서드(특히 데이터 변경과 관련된)에서 사용되며,
연산의 결과를 **원본 DataFrame에 직접 적용할지** 아니면 **수정된 새 DataFrame을 반환할지** 결정합니다.

-   **`inplace=False` (기본값)**:
    * **원본 DataFrame은 그대로 유지**됩니다.
    * 연산 결과가 적용된 **새로운 DataFrame 복사본을 반환**합니다.
    * 이것이 **안전한 기본 동작**입니다. 원본 데이터를 보존하면서 변형된 데이터를 얻을 수 있습니다.
    * 새로운 DataFrame을 받아서 변수에 **재할당**해야 합니다.
    * 예: `df_new = df.drop('컬럼명', axis=1, inplace=False)`

-   **`inplace=True`**:
    * 연산 결과가 **원본 DataFrame에 직접 반영(수정)**됩니다.
    * 메서드는 `None`을 반환하며, 별도의 DataFrame을 반환하지 않습니다.
    * **재할당이 필요 없습니다.**
    * **주의**: 원본 데이터가 영구적으로 변경되므로, 실수로 중요한 데이터를 잃을 수 있어 **사용에 신중**해야 합니다. 복사본을 만들어두거나, 작업 전 `df.copy()`를 사용하는 것이 좋습니다.
    * 예: `df.drop('컬럼명', axis=1, inplace=True)`

언제 `inplace=True`를 사용할까?
-   메모리 효율이 중요할 때: 매우 큰 DataFrame을 다루는데, 중간 결과 DataFrame을 여러 개 생성하는 것이 부담스러울 때.
-   코드를 더 간결하게 만들고 싶을 때 (단, 원본 변경 의도를 명확히 해야 함).

대부분의 경우, `inplace=False` (기본값)를 사용하고 결과를 새로운 변수에 할당하거나, `df = df.drop(...)`과 같이 원본 변수에 재할당하는 것이 **권장**됩니다. 이는 코드의 예측 가능성을 높이고, 실수를 줄이는 데 도움이 됩니다.
"""

# 3. axis와 inplace의 조합 예시 (drop 메서드)
# 예시 실행을 위한 데이터
data = """A,B,C
1,10,100
2,20,200
3,30,300
"""
df_example_drop = pd.read_csv(StringIO(data))
print("\n--- 원본 DataFrame (drop 예시용) ---")
print(df_example_drop)

# 예시 1: 'C' 컬럼을 삭제하되, 원본은 유지하고 새로운 DataFrame 반환 (inplace=False)
print("\n--- 'C' 컬럼 삭제 (inplace=False, axis=1) ---")
df_no_c = df_example_drop.drop('C', axis=1, inplace=False) # inplace=False는 기본값이므로 생략 가능
print(df_no_c)
print("원본 df_example_drop (변화 없음):")
print(df_example_drop) # 원본 df_example_drop는 그대로 유지됨

# 예시 2: 'B' 컬럼을 삭제하고, 원본 DataFrame을 직접 수정 (inplace=True)
print("\n--- 'B' 컬럼 삭제 (inplace=True, axis=1) ---")
df_example_drop.drop('B', axis=1, inplace=True)
print(df_example_drop) # 원본 df_example_drop가 변경됨

# 예시 3: 인덱스 0번 행을 삭제하되, 원본은 유지하고 새로운 DataFrame 반환 (inplace=False, axis=0)
# 예시 2에서 df_example_drop가 이미 변경되었으므로, 새로운 원본 복사본을 생성하여 예시를 진행
df_example_drop_for_row_drop = pd.read_csv(StringIO(data))
print("\n--- 새로운 원본 DataFrame (행 삭제 예시용) ---")
print(df_example_drop_for_row_drop)

df_row_deleted = df_example_drop_for_row_drop.drop(0, axis=0, inplace=False) # inplace=False는 기본값
print("\n--- 인덱스 0번 행 삭제 (inplace=False, axis=0) ---")
print(df_row_deleted)
print("원본 df_example_drop_for_row_drop (변화 없음):")
print(df_example_drop_for_row_drop) # 원본 df_example_drop_for_row_drop는 그대로 유지됨

# 예시 4: 인덱스 1번 행을 삭제하고, 원본 DataFrame을 직접 수정 (inplace=True, axis=0)
print("\n--- 인덱스 1번 행 삭제 (inplace=True, axis=0) ---")
df_example_drop_for_row_drop.drop(1, axis=0, inplace=True)
print(df_example_drop_for_row_drop) # 원본 df_example_drop_for_row_drop가 변경됨


# --- [정리] ---
"""
-   **`axis`**: 연산을 수행할 방향 (`0`=행, `1`=열). `drop()`에서는 무엇을 삭제할지(행 또는 열) 결정합니다.
-   **`inplace`**: 연산 결과를 원본에 적용할지(True), 새 복사본을 반환할지(False). **안전한 코드 작성을 위해 `inplace=False`를 기본으로 사용하고 필요할 때만 `True`를 고려하세요.**
이 두 파라미터를 정확히 이해하는 것은 Pandas를 유연하고 안전하게 사용하는 데 필수적입니다.
"""
