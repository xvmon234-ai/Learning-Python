# ==============================================================================
# [문제 1] 인덱스 초기화 및 특정 컬럼 유지
# ==============================================================================

# --- [최초 나의 코딩] ---
import pandas as pd
from io import StringIO

sales_data = """OrderID,OrderDate,Amount,Customer
101,2023-01-05,15000,C001
102,2023-01-05,20000,C002
103,2023-01-06,12000,C001
104,2023-01-07,30000,C003
105,2023-01-07,8000,C002
"""
#""" 다음에 띄어쓰기 해서 오류 발생한 적 있음, 주의


df_sales_data = pd.read_csv(StringIO(sales_data)).set_index("OrderDate")
df_reset_sales = df_sales_data.reset_index() #이 부분에서 조금 버벅거림

print("\n --- df_reset_sales (info()) --- ")
df_reset_sales.info() #info는 출력을 포함한 매서드이기 때문에 별도로 print문을 작성할 필요 없음

print("\n --- df_reset_sales (head(3)) --- ")
print(df_reset_sales.head(3))

# --- [피드백] ---
"""
문제 해결: `reset_index()`의 기본 동작이 기존 인덱스를 컬럼으로 유지한다는 것을 정확히 활용하여 문제를 해결했습니다. `set_index`를 통한 초기 인덱스 설정도 잘 하셨습니다.
코드 품질:
- `pd.read_csv(StringIO(sales_data)).set_index("OrderDate")`와 같이 메서드 체이닝을 사용하여 간결하게 코드를 작성했습니다.
- `info()`가 자체 출력을 포함한다는 점을 인지하고 계신 것은 좋은 코딩 습관으로 이어질 것입니다.
개선점: `'reset_index()`에서 조금 버벅거렸다'고 하셨지만, 이 문제에서는 `drop=True`를 명시할 필요가 없었기 때문에 기본값으로 올바르게 동작했습니다. 만약 기존 인덱스를 *제거*해야 했다면 `drop=True`를 명시해야 했을 것입니다. 이 점을 다시 한번 상기하는 계기로 삼을 수 있겠습니다.
"""

# --- [모범 답안] ---
# import pandas as pd
# from io import StringIO

# sales_data = """OrderID,OrderDate,Amount,Customer
# 101,2023-01-05,15000,C001
# 102,2023-01-05,20000,C002
# 103,2023-01-06,12000,C001
# 104,2023-01-07,30000,C003
# 105,2023-01-07,8000,C002
# """

# # 1. 'OrderDate' 컬럼을 인덱스로 지정하여 df_sales DataFrame 생성
# # Note: read_csv의 index_col 파라미터로 직접 인덱스 지정 가능
# # df_sales = pd.read_csv(StringIO(sales_data), index_col="OrderDate")

# # 또는: (위의 나의 코드 방식도 좋은 방식입니다)
# # df_sales = pd.read_csv(StringIO(sales_data))
# # df_sales = df_sales.set_index("OrderDate")


# # 2. df_sales의 인덱스를 기본 RangeIndex로 초기화 (기존 'OrderDate' 컬럼 유지)
# # reset_index()의 drop 기본값은 False이므로, 명시하지 않아도 컬럼이 유지됩니다.
# # df_reset_sales = df_sales.reset_index()


# # print("\n --- df_reset_sales (info()) --- ")
# # df_reset_sales.info()

# # print("\n --- df_reset_sales (head(3)) --- ")
# # print(df_reset_sales.head(3))

# --- [학습 기록] ---
"""
**학습 질문**: `reset_index()` 메서드를 사용할 때, `drop` 매개변수의 기본값이 `False`라는 점을 인지하고 있었음에도, 실제로 코드를 작성할 때 이를 명시해야 할지 잠시 망설였음. 또한 `pd.read_csv()`에서 `index_col` 파라미터로 인덱스를 바로 지정하는 방법도 함께 고려하는 것이 더 효율적인지 궁금했음.

**문제 해결**: `reset_index()`의 기본 동작을 신뢰하여 `drop=False`를 생략했고, 문제 요구사항에 따라 기존 인덱스(`'OrderDate'`)가 일반 컬럼으로 잘 유지되는 것을 확인했음. `info()`와 `head()`를 사용하여 데이터 구조 변화를 검증했음.

**추가 학습 (공인회계사 업무와의 관련성 포함)**:
1. `pd.read_csv()` 호출 시 `index_col` 파라미터를 사용하여 처음부터 인덱스를 지정하는 방식이 더 효율적임을 확인했음.
2. `reset_index()`의 `drop=True` 옵션을 활용하여 인덱스를 제거하는 시나리오에 대한 추가 연습이 필요하다고 느꼈음.
3. `set_index()`와 `reset_index()`의 `inplace=True/False` 및 `drop=True/False` 매개변수 조합을 다양하게 테스트하며 DataFrame 원본 변경 여부와 컬럼 유지/삭제 동작을 명확히 이해해야 함.
   * 💡 **공인회계사 업무 연관성**: 감사 또는 재무 분석 시, 특정 보고서나 시스템이 **고유 식별자(예: 거래 ID, 계정 코드)를 일반 컬럼으로 요구**하는 경우가 많음. `reset_index()`를 통해 인덱스를 초기화하고 기존 식별자를 컬럼으로 유지하는 것은 이러한 **데이터 형식 변환 및 보고서 호환성 확보**에 필수적인 기술임. 또한, 원본 데이터의 불변성(immutability)을 유지하며 작업하는 습관은 **감사 추적성(audit trail)과 데이터 무결성(data integrity)을 보장**하는 데 중요함.
"""
