# --- [최초 나의 코딩] ---

import pandas as pd
from io import StringIO

df_high_math = df_students[df_students["Math"] >= 80]

print("\n --- Students with High Math Score --- ")
print(df_high_math)

print("\n --- df_students (info()) --- ")
df_students.info()


# --- [코드 실행 결과] ---
"""
 --- Students with High Math Score ---
          Name  Math  English Grade
StudentID
S001     Alice    90       85     A
S003   Charlie    95       92     A

 --- df_students (info()) ---
<class 'pandas.core.frame.DataFrame'>
Index: 4 entries, 'S001' to 'S004'
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   Name     4 non-null      object
 1   Math     4 non-null      int64
 2   English  4 non-null      int64
 3   Grade    4 non-null      object
dtypes: int64(2), object(2)
memory usage: 288.0+ bytes
"""

# --- [피드백] ---
"""
코드 아주 훌륭하게 작성하셨습니다!

1.  **DataFrame 생성**: 주어진 데이터를 사용하여 DataFrame을 성공적으로 생성했습니다. 문제 4.3에서 인덱스를 설정했으므로, 여기에서도 일관성 있게 `set_index("StudentID")`를 사용한 점이 좋습니다.
2.  **단일 조건 필터링**: `df_students[df_students["Math"] >= 80]` 구문을 사용하여 'Math' 컬럼의 점수가 80점 이상인 학생들만 정확히 필터링했습니다. 이는 Pandas에서 **불리언 인덱싱**을 사용하는 가장 기본적인 방법이며, 해당 방법을 정확히 적용하셨습니다.
3.  **결과 확인**: 필터링된 `df_high_math` DataFrame을 출력하여 조건에 맞는 데이터만 추출되었음을 확인했습니다.
4.  **`info()` 활용**: 마지막으로 `df_students.info()`를 통해 원본 DataFrame의 정보를 확인한 것은 데이터의 구조를 파악하는 데 유용한 습관입니다.

모든 요구사항을 정확하고 효율적으로 만족하는 완벽한 코드입니다!
"""

# --- [모범 답안] ---
"""
# 아래 코드는 최초 나의 코딩과 동일합니다.
# 이미 완벽하게 문제를 해결하셨기 때문에 별도의 수정이 필요 없습니다.

import pandas as pd
from io import StringIO

students_data = """StudentID,Name,Math,English,Grade
S001,Alice,90,85,A
S002,Bob,78,80,B
S003,Charlie,95,92,A
S004,David,60,70,C
"""

# DataFrame 생성 및 'StudentID'를 인덱스로 설정
df_students = pd.read_csv(StringIO(students_data)).set_index("StudentID")

# 'Math' 점수가 80점 이상인 학생들만 필터링
df_high_math = df_students[df_students["Math"] >= 80]

print("--- 'Math' 점수가 80점 이상인 학생들 ---")
print(df_high_math)

# (선택 사항) 원본 DataFrame 정보 확인
print("\n--- 원본 df_students DataFrame 정보 ---")
df_students.info()
"""

# --- [학습 기록] ---
"""
**학습 질문**: DataFrame에서 특정 컬럼의 값을 기준으로 조건을 만족하는 행들만 필터링하려면 어떻게 해야 할까? 불리언 인덱싱의 원리는?

**문제 해결**:
주어진 학생 데이터로 DataFrame `df_students`를 생성했다. 이전에 학습한 `.set_index("StudentID")`를 활용하여 'StudentID'를 인덱스로 설정함으로써 데이터 일관성을 유지했다.
`df_students[df_students["Math"] >= 80]`라는 구문을 사용하여 'Math' 컬럼의 점수가 80점 이상인 모든 행을 성공적으로 필터링하여 `df_high_math`라는 새로운 DataFrame에 할당했다.
이때 `df_students["Math"] >= 80` 부분이 `True` 또는 `False`로 이루어진 **불리언 Series**를 반환하며, 이 불리언 Series를 원본 DataFrame의 인덱싱에 사용하여 `True`에 해당하는 행들만 선택되는 **불리언 인덱싱** 원리를 명확히 이해했다.

**추가 학습**:
불리언 인덱싱은 Pandas에서 데이터를 조건에 따라 추출하는 가장 강력하고 기본적인 방법이다. 이 과정에서 `df["컬럼명"]`은 Series를 반환하고, 이 Series에 조건 연산자(`>=`, `<=`, `==`, `!=`, `>`, `<`)를 적용하면 각 요소에 대한 불리언 값을 갖는 새로운 Series가 생성된다. 이 불리언 Series를 다시 원본 DataFrame의 `[]` 안에 넣어 필터링하는 방식이 핵심이다. 필터링 결과는 원본 DataFrame을 변경하는 것이 아니라 **새로운 DataFrame을 반환**하므로, 이 결과를 재사용하려면 반드시 새로운 변수에 할당해야 한다. 이 점을 숙지하여 원본 데이터의 불필요한 변경을 방지해야 한다.
"""
