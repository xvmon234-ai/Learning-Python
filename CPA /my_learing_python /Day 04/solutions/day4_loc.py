# ==============================================================================
# [문제 4.3] 여러 컬럼 선택 및 행 라벨 기반 선택 (.loc[] 활용) (Day 4 학습 내용)
# ==============================================================================

# 문제 제시:
# 다음 데이터를 사용하여 DataFrame을 생성하세요. 이때 'StudentID'를 인덱스로 설정합니다.
# StudentID,Name,Math,English,Grade
# S001,Alice,90,85,A
# S002,Bob,78,80,B
# S003,Charlie,95,92,A
# S004,David,60,70,C
#
# 1. DataFrame에서 'Name'과 'Grade' 컬럼만 선택하여 출력하세요.
# 2. 인덱스 라벨을 사용하여 'S002' 학생의 모든 정보(행)를 선택하여 출력하세요.
#
# 목표: df[['컬럼1', '컬럼2']]를 사용한 다중 컬럼 선택과 df.loc['인덱스이름']을 사용한 라벨 기반 행 선택을 숙달합니다.
# 가이드:
# 1. 두 개의 대괄호를 사용하여 컬럼 이름을 리스트로 묶어 선택하세요.
# 2. DataFrame 생성 시 index_col='StudentID'를 사용하거나 set_index('StudentID')를 적용하여 'StudentID'를 인덱스로 설정한 후, .loc[]에 'S002' 라벨을 전달하세요.

# --- [최초 나의 코딩] ---
import pandas as pd
from io import StringIO

students_data = """StudentID,Name,Math,English,Grade
S001,Alice,90,85,A
S002,Bob,78,80,B
S003,Charlie,95,92,A
S004,David,60,70,C
"""

df_students = pd.read_csv(StringIO(students_data)).set_index("StudentID")

print("\n --- Student's Name and Grade --- ")
print(df_students[["Name", "Grade"]])

print("\n --- Student S002's info --- ")
print(df_students.loc["S002"]) #최초에 df 이름 뒤에 s빼고 적어서 NameError 발생했음

print("\n --- df_student (info()) --- ")
df_students.info()


# --- [코드 실행 결과] ---
"""
 --- Student's Name and Grade ---
         Name Grade
StudentID
S001    Alice     A
S002      Bob     B
S003  Charlie     A
S004    David     C

 --- Student S002's info ---
Name       Bob
Math        78
English     80
Grade        B
Name: S002, dtype: object

 --- df_student (info()) ---
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

1.  **DataFrame 생성 및 인덱스 설정**: `pd.read_csv(StringIO(students_data)).set_index("StudentID")`를 사용하여 데이터를 DataFrame으로 로드하고 동시에 'StudentID' 컬럼을 인덱스로 정확히 설정했습니다. 데이터를 효율적으로 준비하는 좋은 방법입니다.
2.  **다중 컬럼 선택**: `df_students[["Name", "Grade"]]`를 사용하여 'Name'과 'Grade' 두 컬럼을 완벽하게 선택했습니다. 두 개의 대괄호를 사용하여 여러 컬럼을 DataFrame 형태로 가져오는 방법을 정확히 이해하고 적용하셨습니다.
3.  **라벨 기반 행 선택**: `df_students.loc["S002"]`를 사용하여 인덱스 라벨 'S002'에 해당하는 행의 모든 정보를 성공적으로 추출했습니다. `.loc[]`의 라벨 기반 인덱싱 사용법을 잘 숙지하고 있음을 보여줍니다.
    * **오류 경험 기록**: `df 이름 뒤에 s빼고 적어서 NameError 발생했음`이라고 기록한 점은 아주 좋습니다! 변수 이름의 오타로 인한 `NameError`는 흔히 발생하는 실수이며, 이를 통해 변수명 정확성, 그리고 에러 메시지(`NameError`)를 통해 문제의 원인(`df` 대신 `df_students`로 사용해야 함)을 파악하는 능력을 기를 수 있습니다. 이러한 경험을 기록하는 것은 학습에 매우 중요합니다.
4.  **`info()` 활용**: 마지막으로 `df_students.info()`를 통해 DataFrame의 전반적인 구조(인덱스, 컬럼, 데이터 타입, Non-Null 개수 등)를 확인한 것은 데이터를 이해하는 데 매우 유용하며, 좋은 학습 습관입니다.

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

# 1. 'Name'과 'Grade' 컬럼만 선택하여 출력
print("\n--- 학생의 이름과 학점 ---")
selected_columns = df_students[["Name", "Grade"]]
print(selected_columns)

# 2. 인덱스 라벨 'S002' 학생의 모든 정보(행) 선택하여 출력
print("\n--- S002 학생의 모든 정보 ---")
student_s002_info = df_students.loc["S002"]
print(student_s002_info)

# (선택 사항) DataFrame 정보 확인
print("\n--- df_students DataFrame 정보 ---")
df_students.info()
"""

# --- [학습 기록] ---
"""
**학습 질문**: DataFrame에서 특정 컬럼들을 동시에 선택하고, 특정 인덱스 라벨을 기준으로 행을 선택하는 방법은 무엇일까? 변수명 오타와 같은 기본 에러 처리의 중요성은?

**문제 해결**:
1.  **DataFrame 생성 및 인덱스 설정**: `pd.read_csv` 함수를 사용하여 데이터를 로드함과 동시에 `.set_index("StudentID")` 메서드 체이닝을 통해 'StudentID' 컬럼을 DataFrame의 인덱스로 지정했습니다. 이를 통해 라벨 기반의 데이터 접근이 가능해졌다.
2.  **다중 컬럼 선택**: `df_students[["Name", "Grade"]]`와 같이 **이중 대괄호** 안에 선택하고자 하는 컬럼 이름들을 **리스트** 형태로 넣어, 'Name'과 'Grade' 컬럼으로만 구성된 새로운 DataFrame을 성공적으로 얻었다. 이는 여러 컬럼을 한 번에 선택할 때의 표준 방법임을 재확인했다.
3.  **라벨 기반 행 선택**: `df_students.loc["S002"]`를 사용하여 인덱스 라벨 'S002'에 해당하는 행의 모든 데이터를 추출했다. 이 과정에서 변수명 오타(`df` 대신 `df_students`)로 인해 `NameError`가 발생했으나, 에러 메시지를 통해 문제를 파악하고 수정할 수 있었다. 이러한 작은 실수를 통해 변수명 정확성의 중요성과 디버깅 능력을 향상시킬 수 있음을 깨달았다.
4.  **정보 확인**: 최종적으로 `df_students.info()`를 통해 DataFrame의 인덱스가 'StudentID'로 올바르게 설정되었으며, 컬럼들의 데이터 타입과 Non-Null 개수도 확인했다.

**추가 학습 (공인회계사 업무와의 관련성)**:

`df[['컬럼1', '컬럼2']]`를 사용한 **다중 컬럼 선택**과 `df.loc['인덱스이름']`을 사용한 **라벨 기반 행 선택**은 공인회계사(CPA)가 **특정 거래의 전체 내용(행) 또는 특정 정보(컬럼)만을 빠르고 정확하게 추출하여 감사 및 분석에 활용**할 때 매우 중요합니다.

* **다중 컬럼 선택**:
    * **예시**: 회사의 **전표 데이터**에서 '전표번호', '계정과목', '차변금액', '대변금액' 등 **감사 또는 재무 보고에 필요한 핵심 컬럼들만 동시에 선택**하여 분석합니다.
    * CPA는 이를 통해 특정 거래의 재무적 영향만을 집중적으로 분석하거나, 재무제표 작성에 필요한 필수 데이터를 효율적으로 추출할 수 있습니다. 예를 들어, `df_journal[['Date', 'Account', 'Debit', 'Credit']]`와 같이 사용합니다.

* **라벨 기반 행 선택 (`.loc[]`)**:
    * **예시**: '거래번호', '고객ID', '자산ID' 등이 인덱스로 설정된 데이터에서 **특정 고객ID(`'CUST005'`) 또는 특정 자산ID(`'ASSET123'`)에 해당하는 모든 거래나 자산 정보(해당 행 전체)**를 조회합니다.
    * CPA는 특정 거래의 상세 내역을 파악하거나, 특정 감사 샘플(예: 특정 고객에 대한 매출채권 확인)의 데이터를 빠르게 조회하여 증거를 확보할 수 있습니다. 이는 인덱스가 명확한 데이터(예: 고유 ID)에서 특히 강력한 효과를 발휘합니다.

* **특정 문서/보고서 생성**:
    * CPA는 다양한 내부 보고서나 외부 공시 자료를 작성할 때, 원본 데이터에서 **필요한 특정 정보(컬럼)와 관련된 특정 대상(행)**만을 정확히 추출하여 반영해야 합니다. `.loc[]`와 다중 컬럼 선택의 조합은 이러한 정밀한 데이터 추출을 가능하게 합니다.
    * 예를 들어, `df_financials.loc['2024Q1', ['Revenue', 'Net_Income']]`와 같이 특정 분기의 매출액과 순이익만 선택하여 분석하는 식입니다.

결론적으로, 다중 컬럼 선택과 라벨 기반 행 선택은 CPA가 **정확하고 효율적인 데이터 접근을 통해 재무 데이터를 심층적으로 분석하고, 감사 증거를 확보하며, 특정 목적에 맞는 보고서를 작성하는 데 필수적인 역량**을 제공합니다.
"""
