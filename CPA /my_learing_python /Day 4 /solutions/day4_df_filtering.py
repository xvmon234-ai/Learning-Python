# ==============================================================================
# [문제 4.4] 단일 조건 필터링 (Day 4 학습 내용)
# ==============================================================================

# 문제 제시: 위 4.3 문제에서 생성한 DataFrame(df_students)에서 'Math' 점수가 80점 이상인 학생들만 필터링하여 출력해보세요.
# 목표: 불리언 인덱싱을 사용하여 숫자 조건을 기준으로 DataFrame을 필터링하는 방법을 연습합니다.
# 가이드: df[df['컬럼명'] 조건값] 형태를 사용하여 'Math' 컬럼에 대한 조건을 적용하세요.

# --- [최초 나의 코딩] ---
import pandas as pd
from io import StringIO

students_data = """StudentID,Name,Math,English,Grade
S001,Alice,90,85,A
S002,Bob,78,80,B
S003,Charlie,95,92,A
S004,David,60,70,C
"""

# 문제 4.3에서 'StudentID'를 인덱스로 설정했었으나, 문제 4.4에서는 인덱스 설정이 필수는 아닙니다.
# 하지만 일관성을 위해 이전 문제와 동일하게 인덱스를 설정하여 사용하겠습니다.
df_students = pd.read_csv(StringIO(students_data)).set_index("StudentID")

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

**추가 학습 (공인회계사 업무와의 관련성)**:

Pandas의 **단일 조건 필터링(`df[df['컬럼명'] 조건값]`)**은 공인회계사(CPA)가 **대량의 재무 및 운영 데이터에서 특정 기준을 충족하는 정보를 신속하게 식별하고 추출**하는 데 매우 필수적인 기능입니다. 이는 감사 절차, 재무 분석, 데이터 검증 등 다양한 업무에 활용됩니다.

* **매출/비용의 유의성 검토**:
    * **예시**: 특정 금액(예: 100만 원)을 초과하는 **고액의 매출 또는 비용 거래**만 필터링하여 검토할 때 사용합니다. `df_transactions[df_transactions['Amount'] >= 1000000]`와 같이 필터링하여 잠재적 위험 거래를 집중적으로 확인합니다.
    * CPA는 이를 통해 내부 통제상의 허점이나 부정의 가능성을 탐지하고, 중요성에 기반한 감사 접근 방식을 적용할 수 있습니다.

* **특정 조건 만족하는 계약/자산 식별**:
    * **예시**: '계약 종료일'이 특정 날짜(예: 이번 분기 말) 이전에 도래하는 계약들만 필터링하거나, '자산의 장부가치'가 일정 금액 이상인 유형 자산만 추출하여 **재평가 필요성 또는 손상 징후**를 파악합니다.
    * `df_contracts[df_contracts['EndDate'] < '2025-03-31']` 또는 `df_assets[df_assets['Book_Value'] > 500000]` 와 같이 사용하여 관련 회계 처리의 적절성을 검토합니다.

* **재고 또는 채권의 건전성 평가**:
    * **예시**: '재고 평가액'이 일정 기준 이하로 떨어지는 품목이나, '미수금 회수 기한'이 지난 채권들만 필터링하여 **재고 자산의 진부화 또는 채권의 회수 불능 가능성**을 평가합니다.
    * 이는 충당금 설정 등 관련 회계 추정의 적정성을 검토하는 데 중요한 데이터를 제공합니다.

* **특정 부서/사업부의 성과 분석**:
    * **예시**: 특정 '부서 코드'에 해당하는 데이터만 필터링하여 해당 부서의 손익이나 비용 구조를 심층적으로 분석합니다.
    * `df_expenses[df_expenses['Department_Code'] == 'SALES']`와 같이 사용함으로써, CPA는 부서별 성과를 평가하고 효율성을 증대시킬 방안을 모색할 수 있습니다.

결론적으로, 단일 조건 필터링은 CPA가 **정의된 기준에 따라 대량의 데이터에서 핵심적인 정보를 선별적으로 추출하고, 이를 기반으로 재무 분석, 감사 위험 평가, 회계 처리의 적정성 검토 등 다양한 실무를 수행하는 데 필수적인 기초 데이터 핸들링 기술**입니다.
"""
