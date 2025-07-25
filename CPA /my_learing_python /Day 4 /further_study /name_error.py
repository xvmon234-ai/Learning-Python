# --- [Further Study: NameError 이해 및 해결] ---

# 1. NameError 란?
"""
`NameError`는 Python에서 **정의되지 않은 변수나 함수를 호출하려 할 때** 발생하는 오류입니다.
'Name'은 변수, 함수, 클래스 등 코딩에 사용되는 '이름'을 의미하며,
'Error'는 그런 이름이 현재 스코프(코드 실행 범위) 내에서 찾아질 수 없다는 뜻입니다.

간단히 말해, "너 이런 이름(변수/함수) 쓴다고 했는데, 내가 아무리 찾아봐도 그런 이름은 없어!" 라고 Python 인터프리터가 알려주는 것입니다.
"""

# 2. Pandas 학습 중 NameError가 발생하는 흔한 경우
"""
Pandas를 다룰 때 NameError는 주로 다음과 같은 상황에서 발생합니다.

(1) 변수명 오타:
    DataFrame이나 Series의 변수 이름을 잘못 입력했을 때.
    예: df_students를 df_student로 오타.

(2) 변수 정의 전 사용:
    변수를 선언(할당)하기 전에 해당 변수를 사용하려고 할 때.
    예: `new_df = df_original` 코드 이전에 `df_original`을 사용하려 할 때.

(3) 모듈/함수 임포트 누락 또는 오타:
    사용하려는 함수나 클래스가 속한 모듈을 임포트하지 않았거나, 임포트할 때 오타가 났을 때.
    예: `pd.read_csv`를 사용해야 하는데 `import pandas`를 하지 않았거나 `pd`가 아닌 다른 이름으로 임포트했을 때.

(4) 스코프 문제:
    변수가 정의된 스코프(범위) 밖에서 해당 변수를 사용하려 할 때.
    (예: 함수 내에서 정의된 지역 변수를 함수 밖에서 호출)
"""

# 3. NameError 발생 예시 및 해결 방법

# 예시 1: 변수명 오타 (문제 4.3에서 경험한 경우)
"""
# 발생 상황:
# df_students = pd.read_csv(StringIO(students_data)).set_index("StudentID")
# print(df_student.loc["S002"]) # 'df_student'는 정의되지 않은 변수

# 해결 방법:
# 올바른 변수명인 `df_students`를 사용해야 합니다.
# print(df_students.loc["S002"])
"""
# 예시 코드 (실행 시 NameError 발생):
# import pandas as pd
# from io import StringIO
# students_data = "StudentID,Name,Math,English,Grade\nS001,Alice,90,85,A"
# df_students = pd.read_csv(StringIO(students_data)).set_index("StudentID")
# # print(df_student.loc["S002"]) # 이 줄의 주석을 풀면 NameError 발생

# 예시 2: 모듈 임포트 누락
"""
# 발생 상황:
# read_csv("data.csv") # 'read_csv'는 정의되지 않은 함수

# 해결 방법:
# `import pandas as pd`를 통해 pandas 모듈을 임포트하고, `pd.read_csv`와 같이 사용해야 합니다.
# import pandas as pd
# pd.read_csv("data.csv")
"""

# 예시 3: 변수 정의 전 사용
"""
# 발생 상황:
# print(my_variable) # 'my_variable'은 아직 정의되지 않음
# my_variable = 10

# 해결 방법:
# 변수를 사용하기 전에 먼저 정의(할당)해야 합니다.
# my_variable = 10
# print(my_variable)
"""

# 4. NameError 발생 시 대처법
"""
1.  **에러 메시지 읽기**: `NameError: name 'xxx' is not defined` 메시지에서 'xxx'가 어떤 이름인지 확인합니다.
2.  **변수명 확인**: 해당 이름의 변수가 코드 내에서 정확하게 철자 오류 없이 정의되었는지 확인합니다.
3.  **임포트 확인**: 사용하려는 함수나 객체가 특정 라이브러리에 속한다면, 해당 라이브러리를 올바르게 임포트했는지 확인합니다. (예: `import pandas as pd`)
4.  **실행 흐름 확인**: 변수가 사용되는 시점 이전에 해당 변수가 할당되었는지, 또는 함수가 정의되었는지 코드의 실행 순서를 따라가며 확인합니다.
5.  **스코프 확인**: 특히 함수나 클래스 내부/외부에서 변수를 사용할 때 스코프 규칙을 고려합니다.
"""

# --- [정리] ---
"""
`NameError`는 코드의 가장 기본적인 오류 중 하나이지만, 초보자가 자주 마주치며 디버깅 능력을 향상시키는 데 중요한 경험을 제공합니다.
에러 메시지를 침착하게 읽고, 위에 제시된 대처법들을 적용하여 문제를 해결하는 습관을 들이세요.
"""
