# --- [Further Study: Pandas 불리언 인덱싱 (Boolean Indexing) 심층 이해] ---

# 1. Pandas 불리언 인덱싱이란?
"""
Pandas에서 **불리언 인덱싱(Boolean Indexing)**은 DataFrame이나 Series의 특정 조건에 맞는 행이나 열을 선택하는 매우 강력하고 유연한 방법입니다.
기본 아이디어는 다음과 같습니다:

1.  **조건을 만족하는 불리언 Series 생성**: 특정 조건을 Pandas Series(예: `df['컬럼명'] > 10`)에 적용하면,
    각 요소가 해당 조건을 만족하는지 여부를 나타내는 `True` 또는 `False` 값으로 구성된 새로운 **불리언(Boolean) Series**가 반환됩니다.
    * `True`: 해당 조건에 부합하는 데이터
    * `False`: 해당 조건에 부합하지 않는 데이터

2.  **불리언 Series를 필터로 사용**: 이 불리언 Series를 DataFrame의 대괄호 `[]` 안에 넣으면,
    `True` 값에 해당하는 행들만 선택되어 새로운 DataFrame으로 반환됩니다.
    `False` 값에 해당하는 행들은 결과에서 제외됩니다.
"""

# 2. 왜 isin(), str.contains() 등의 결과를 바로 사용하지 않고 불리언 인덱싱에 활용할까?
"""
`df_employees["Name"].str.contains("a", case=False)`나
`df_employees["Department"].isin(["HR", "Finance"])`와 같은 Pandas 메서드들은
그 자체가 필터링된 DataFrame을 반환하는 것이 아니라,
**필터링을 위한 기준 역할을 하는 불리언 Series를 반환**합니다.

이 불리언 Series는 각 행이 특정 조건을 만족하는지(`True`) 아닌지(`False`)를 알려주는 '체크리스트'와 같습니다.

예시를 들어볼까요?
원본 DataFrame:
   Name  Math
0  Alice    90
1    Bob    78
2  David    60

조건: `df['Math'] >= 80`
이 조건은 다음과 같은 불리언 Series를 반환합니다:
0     True  (90 >= 80)
1    False  (78 >= 80)
2    False  (60 >= 80)
Name: Math, dtype: bool

이제 이 불리언 Series를 DataFrame의 `[]` 안에 넣으면, Pandas는 이 `True`/`False` 값을 보고
`True`인 행(인덱스 0)만 선택하고 `False`인 행(인덱스 1, 2)은 버립니다.

최종 결과 (필터링된 DataFrame):
   Name  Math
0  Alice    90

따라서, `isin()`이나 `str.contains()` 등은 필터링 로직을 만드는 도구이지,
그 자체가 최종 필터링 결과를 담는 DataFrame이 아닙니다.
이러한 메서드들이 반환하는 불리언 Series를 `df[불리언_시리즈]` 형태로
원본 DataFrame에 다시 적용해야 원하는 필터링된 DataFrame을 얻을 수 있습니다.
"""

# 3. 불리언 인덱싱의 기본 구조 및 동작 원리
"""
기본 구조: `dataframe[조건_을_만족하는_불리언_시리즈]`

단계별 동작 원리:

1.  **조건 생성**: 먼저, 필터링하려는 조건(예: `df["컬럼"] > 값`, `df["문자열컬럼"].str.contains("패턴")`, `df["숫자컬럼"].isin([값1, 값2])`)을 작성합니다.
2.  **불리언 Series 반환**: 이 조건은 각 행에 대해 `True` 또는 `False` 값을 가지는 Pandas Series를 반환합니다. 이 Series의 인덱스는 원본 DataFrame의 인덱스와 동일해야 합니다.
3.  **DataFrame 필터링**: Pandas는 이 불리언 Series를 사용하여 원본 DataFrame에서 `True`에 해당하는 행들만 추출하여 새로운 DataFrame을 생성합니다.

예시 코드:
import pandas as pd
from io import StringIO

data = """Name,Age,City
Alice,25,Seoul
Bob,30,Busan
Charlie,35,Seoul
David,28,Jeju
"""
df = pd.read_csv(StringIO(data))

# 1단계: 조건 생성 -> 불리언 Series 반환
is_seoul_resident = df['City'] == 'Seoul'
print("--- 'City' == 'Seoul' 불리언 Series ---")
print(is_seoul_resident)
# 결과:
# 0     True
# 1    False
# 2     True
# 3    False
# Name: City, dtype: bool

# 2단계: 불리언 Series를 사용하여 DataFrame 필터링
seoul_residents_df = df[is_seoul_resident]
print("\n--- 'Seoul' 거주자 DataFrame ---")
print(seoul_residents_df)
# 결과:
#     Name  Age   City
# 0  Alice   25  Seoul
# 2  Charlie   35  Seoul

# 이를 한 줄로 줄여서 사용한 것이 우리가 흔히 보는 형태입니다:
# df_seoul = df[df['City'] == 'Seoul']
"""

# 4. 불리언 인덱싱의 장점
"""
-   **직관적**: 조건문을 바로 데이터프레임의 인덱싱에 적용하는 방식이 매우 직관적입니다.
-   **강력함**: 단일 조건, 다중 조건(`&`, `|` 사용), 문자열/숫자/날짜 등 다양한 데이터 타입에 유연하게 적용할 수 있습니다.
-   **성능**: Pandas 내부적으로 최적화되어 있어 대량의 데이터를 효율적으로 필터링할 수 있습니다.
"""

# --- [정리] ---
"""
`isin()`이나 `str.contains()`와 같은 Pandas 메서드들은 **필터링을 위한 불리언 Series를 생성**하는 역할을 합니다.
이 생성된 불리언 Series를 원본 DataFrame의 대괄호 `[]` 안에 넣어주어야만,
실제로 **조건에 맞는 행들만 추출된 새로운 DataFrame**을 얻을 수 있습니다.
이러한 불리언 인덱싱의 원리를 정확히 이해하는 것이 Pandas 데이터 조작의 핵심입니다.
"""
