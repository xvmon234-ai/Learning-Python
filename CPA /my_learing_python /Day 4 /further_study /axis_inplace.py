# --- [Further Study: Pandas drop() 메서드의 axis와 inplace 파라미터 심층 이해] ---

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

예시 (drop 메서드에서 axis):
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
"""
import pandas as pd
from io import StringIO

data = """A,B,C
1,10,100
2,20,200
3,30,300
"""
df = pd.read_csv(StringIO(data))
print("--- 원본 DataFrame ---")
print(df)

# 예시 1: 'C' 컬럼을 삭제하되, 원본은 유지하고 새로운 DataFrame 반환 (inplace=False)
print("\n--- 'C' 컬럼 삭제 (inplace=False, axis=1) ---")
df_no_c = df.drop('C', axis=1, inplace=False) # inplace=False는 기본값이므로 생략 가능
print(df_no_c)
print("원본 df:", df) # 원본 df는 그대로 유지됨

# 예시 2: 'B' 컬럼을 삭제하고, 원본 DataFrame을 직접 수정 (inplace=True)
print("\n--- 'B' 컬럼 삭제 (inplace=True, axis=1) ---")
df.drop('B', axis=1, inplace=True)
print(df) # 원본 df가 변경됨

# 예시 3: 인덱스 0번 행을 삭제하되, 원본은 유지하고 새로운 DataFrame 반환 (inplace=False, axis=0)
df_row_deleted = df.drop(0, axis=0) # inplace=False는 기본값
print("\n--- 인덱스 0번 행 삭제 (inplace=False, axis=0) ---")
print(df_row_deleted)
print("원본 df:", df) # 원본 df는 (B컬럼이 삭제된 상태로) 그대로 유지됨

# 예시 4: 인덱스 1번 행을 삭제하고, 원본 DataFrame을 직접 수정 (inplace=True, axis=0)
print("\n--- 인덱스 1번 행 삭제 (inplace=True, axis=0) ---")
df.drop(1, axis=0, inplace=True)
print(df) # 원본 df가 변경됨 (C, B 컬럼 없고 1번 행도 없음)
"""

# --- [정리] ---
"""
-   **`axis`**: 연산을 수행할 방향 (`0`=행, `1`=열). `drop()`에서는 무엇을 삭제할지(행 또는 열) 결정합니다.
-   **`inplace`**: 연산 결과를 원본에 적용할지(True), 새 복사본을 반환할지(False). **안전한 코드 작성을 위해 `inplace=False`를 기본으로 사용하고 필요할 때만 `True`를 고려하세요.**
이 두 파라미터를 정확히 이해하는 것은 Pandas를 유연하고 안전하게 사용하는 데 필수적입니다.
"""
