# ==============================================================================
# [문제 4.1] 단일 컬럼 선택 (Day 4 학습 내용)
# ==============================================================================

# 문제 제시: 다음 데이터를 사용하여 DataFrame을 생성하고, 'Product' 컬럼만 선택하여 출력해보세요.
# OrderID,Product,Quantity,Price
# 1,Laptop,1,1200
# 2,Mouse,2,25
# 3,Keyboard,1,75
# 4,Monitor,1,300
# 목표: df['컬럼명']의 기본 사용법을 익히고 Series 반환을 확인합니다.
# 가이드: pandas 라이브러리의 read_csv와 StringIO를 사용하여 DataFrame을 생성한 뒤, 단일 대괄호를 사용하여 'Product' 컬럼을 선택하세요.

# --- [최초 나의 코딩] ---
import pandas as pd
from io import StringIO

products_data = """OrderID,Product,Quantity,Price
1,Laptop,1,1200
2,Mouse,2,25
3,Keyboard,1,75
4,Monitor,1,300
"""

df_products = pd.read_csv(StringIO(products_data))

print("\n --- Product Col --- ")
print(df_products["Product"])

print("\n --- df_product (info()) --- ")
df_products["Product"].info()


# --- [코드 실행 결과] ---
"""
 --- Product Col ---
0      Laptop
1       Mouse
2    Keyboard
3     Monitor
Name: Product, dtype: object

 --- df_product (info()) ---
<class 'pandas.core.series.Series'>
RangeIndex: 4 entries, 0 to 3
Series name: Product
Non-Null Count  Dtype
--------------  -----
4 non-null      object
dtypes: object(1)
memory usage: 200.0+ bytes
"""

# --- [피드백] ---
"""
코드 아주 잘 작성하셨습니다!

1.  **DataFrame 생성**: `StringIO`를 사용하여 CSV 데이터를 성공적으로 DataFrame으로 변환했습니다.
2.  **컬럼 선택**: `df_products["Product"]`를 사용하여 **'Product' 컬럼**을 정확히 선택하고 출력했습니다. 이는 **Series 객체**로 반환되며, 문제의 목표를 완벽하게 달성했습니다.
3.  **`info()` 활용**: 선택된 컬럼에 대해 `.info()` 메서드를 사용한 것은 아주 좋은 습관입니다. 이를 통해 데이터 타입, Non-Null 개수 등을 빠르게 파악하여 데이터의 상태를 이해하는 데 큰 도움이 됩니다.

요구사항을 모두 만족하는 완벽한 코드입니다!
"""

# --- [모범 답안] ---
"""
# 아래 코드는 '최초 나의 코딩'과 동일합니다.
# 이미 완벽하게 문제를 해결하셨기 때문에 별도의 수정이 필요 없습니다.

import pandas as pd
from io import StringIO

products_data = """OrderID,Product,Quantity,Price
1,Laptop,1,1200
2,Mouse,2,25
3,Keyboard,1,75
4,Monitor,1,300
"""

df_products = pd.read_csv(StringIO(products_data))

product_series = df_products["Product"]
print("--- 'Product' 컬럼 (Series) ---")
print(product_series)

print("\n--- 'Product' 컬럼 정보 ---")
product_series.info()
"""

# --- [학습 기록] ---
"""
**학습 질문**: DataFrame에서 특정 컬럼 하나만 선택하려면 어떻게 해야 할까? Series와 DataFrame의 차이는 무엇일까?

**문제 해결**:
`pandas.read_csv`와 `io.StringIO`를 사용하여 문자열 CSV 데이터를 DataFrame `df_products`로 로드했다.
`df_products["Product"]` 문법을 사용하여 `'Product'` 컬럼을 성공적으로 선택했다. 이 결과가 **Pandas Series 객체**로 반환되는 것을 확인했다.
추가적으로 `.info()` 메서드를 사용하여 선택된 Series의 데이터 타입(dtype: object, 즉 문자열), Non-Null 개수, 메모리 사용량 등을 확인하여 컬럼의 특성을 이해하는 데 도움을 얻었다.

**추가 학습 (공인회계사 업무와의 관련성)**:

Pandas에서 **특정 컬럼을 선택하는 것은 공인회계사(CPA)의 업무에서 매우 기본적이고 핵심적인 데이터 준비 단계**입니다. 방대한 재무 데이터에서 필요한 정보만 추출하여 분석 효율성을 높이고, 특정 목적에 맞는 리포트를 생성하는 데 필수적으로 사용됩니다.

* **재무제표 항목 분석**:
    * **예시**: 회사의 **총계정원장(GL) 데이터**에서 특정 계정(예: '매출액', '현금', '미수금') 컬럼만 추출하여 해당 계정의 상세 내역이나 추이를 분석합니다.
    * CPA는 이를 통해 특정 계정의 잔액 변동을 추적하거나, 이상 징후를 파악하여 감사 절차를 계획할 수 있습니다. 예를 들어, `df_gl['Account_Balance']`와 같이 특정 계정 잔액 컬럼만 선택하여 분석하는 식입니다.

* **감사 증거 수집 및 검토**:
    * **예시**: 감사 대상 기업의 판매 데이터베이스에서 '판매금액', '판매일자', '제품코드' 등 **특정 감사 목적에 필요한 컬럼만 선택**하여 분석합니다.
    * 이를 통해 CPA는 매출의 실재성, 발생주의 적용의 적절성 등을 검토하고, 특정 기간의 총 매출을 집계하거나, 이상한 패턴(예: 기말에 집중된 매출)을 식별할 수 있습니다.

* **데이터 추출 및 보고서 작성**:
    * **예시**: 인사 급여 데이터에서 '직원명', '부서', '급여액' 컬럼만 추출하여 특정 보고서 양식에 맞게 데이터를 가공하거나, 특정 분석 도구로 내보내기 위한 기초 데이터를 만듭니다.
    * CPA는 재무 모델링을 위한 입력 데이터나 특정 공시를 위한 자료를 준비할 때, 필요한 컬럼만 정확히 선택하여 사용함으로써 데이터의 불필요한 부분을 제거하고 작업 효율성을 높일 수 있습니다.

* **데이터 구조 파악 및 검증**:
    * `.info()`와 같은 메서드를 사용하여 선택된 컬럼의 데이터 타입(dtype)과 결측치(Non-Null Count)를 확인하는 것은 CPA에게 매우 중요합니다. 예를 들어, '판매금액' 컬럼이 숫자가 아닌 문자열로 되어 있거나 결측치가 많다면, 이후 분석 과정에서 오류가 발생할 수 있기 때문에 사전에 파악하고 처리해야 합니다.

결론적으로, Pandas에서 **단일 컬럼을 선택하는 것은 CPA가 데이터를 파악하고, 필요한 정보를 추출하며, 분석 준비를 하는 데 있어 가장 기초적이면서도 핵심적인 기술**입니다.
"""
