# ==============================================================================
# [문제 2] 인덱스 다중 설정
# ==============================================================================

# --- [최초 나의 코딩] ---
import pandas as pd
from io import StringIO

students_data = """StudentID,Subject,Score
S001,Math,90
S001,Science,85
S002,Math,78
S002,English,92
S003,Science,88
"""

df_grades = pd.read_csv(StringIO(students_data))
df_grades = df_grades.set_index(["StudentID", "Subject"])
#처음에 []를 안 써서 오류가 발생했음

print("\n --- df_grades (info()) ---")
df_grades.info()

print("\n --- df_grades --- ")
print(df_grades)

# --- [피드백] ---
"""
문제 해결: 여러 컬럼을 동시에 인덱스로 설정해야 하는 요구사항을 `set_index(["컬럼명1", "컬럼명2"])`와 같이 리스트 형식으로 컬럼명을 전달하여 정확하게 구현했습니다. 원본 `df_grades`를 직접 수정하라는 요구사항도 `df_grades = df_grades.set_index(...)`와 같이 재할당하여 잘 따랐습니다.
코드 품질: 데이터 로드부터 인덱스 설정, 그리고 정보 및 내용 출력까지 간결하고 명확하게 작성되었습니다. `info()` 메서드가 자체 출력을 포함한다는 점을 일관되게 적용하는 좋은 습관을 유지하고 있습니다.
학습 통찰: `'처음에 []를 안 써서 오류가 발생했음'`이라는 주석에서 알 수 있듯이, 다중 인덱스 설정 시 컬럼 이름들을 리스트로 묶어야 한다는 중요한 규칙을 직접 오류를 통해 경험하고 학습한 점이 매우 효과적입니다. 이러한 경험은 개념을 더 깊이 이해하는 데 도움이 됩니다.
"""

# --- [모범 답안] ---
# import pandas as pd
# from io import StringIO

# students_data = """StudentID,Subject,Score
# S001,Math,90
# S001,Science,85
# S002,Math,78
# S002,English,92
# S003,Science,88
# """

# df_grades = pd.read_csv(StringIO(students_data))

# # 'StudentID'와 'Subject' 컬럼을 동시에 인덱스로 설정하고 원본 df_grades를 직접 수정
# # set_index의 inplace 기본값은 False이므로, 재할당하는 방식이 명시적이고 일반적입니다.
# # df_grades.set_index(["StudentID", "Subject"], inplace=True) # 이 방식도 가능하나, 재할당이 더 흔함
# # df_grades = df_grades.set_index(["StudentID", "Subject"])


# # print("\n --- df_grades (info()) ---")
# # df_grades.info()

# # print("\n --- df_grades (인덱스) --- ")
# # print(df_grades.index) # 인덱스 자체를 출력 (문제 요구사항)

# # print("\n --- df_grades (전체 내용) --- ")
# # print(df_grades) # 전체 DataFrame 출력

# --- [학습 기록] ---
"""
**학습 질문**: `set_index()` 메서드로 여러 컬럼을 인덱스로 설정할 때, 컬럼 이름을 리스트로 묶지 않으면 오류가 발생하는 이유와 다중 인덱스(MultiIndex)가 어떻게 구성되는지 궁금했음.

**문제 해결**: `df.set_index(["컬럼1", "컬럼2"])`와 같이 컬럼 이름들을 리스트로 묶어 전달함으로써 다중 인덱스를 성공적으로 설정했음. `df.info()`를 통해 `MultiIndex` 타입으로 변경되었음을 확인했고, 기존 인덱스 컬럼들이 제거되어 인덱스 레벨로 올라간 것을 파악했음.

**추가 학습 (공인회계사 업무와의 관련성 포함)**:
1. MultiIndex의 개념과 구조(`levels`, `codes`, `names` 속성)를 더 깊이 이해해야 함.
2. MultiIndex DataFrame에서 특정 레벨의 인덱스를 기준으로 데이터를 선택하거나 정렬하는 방법을 연습해야 함.
3. `MultiIndex`를 가진 DataFrame에서 `reset_index()`를 사용했을 때의 동작 방식(모든 인덱스 레벨이 컬럼으로 복원되는지 등)을 탐구해야 함.
   * 💡 **공인회계사 업무 연관성**: 재무 데이터는 종종 **계층적 구조**를 가짐 (예: 지점-부서-팀, 연도-분기-월, 계정과목-세부항목). `MultiIndex`는 이러한 계층적 데이터를 Pandas에서 효과적으로 표현하고 분석하는 데 필수적임. 예를 들어, **연결 재무제표 작성 시 자회사별, 계정별 데이터를 동시에 관리**하거나, **세그먼트별 실적을 분석**할 때 `MultiIndex`를 활용하면 복잡한 데이터를 체계적으로 정리하고 접근할 수 있음. 이는 **정확한 보고서 작성 및 심층적인 재무 분석 능력**을 향상시킴.
"""
