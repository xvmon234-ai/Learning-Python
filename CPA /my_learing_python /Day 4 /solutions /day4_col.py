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



# --- [피드백] ---
"""
코드 아주 잘 작성하셨습니다!

1.  **DataFrame 생성**: StringIO를 사용하여 CSV 데이터를 성공적으로 DataFrame으로 변환했습니다.
2.  **컬럼 선택**: df_products["Product"]를 사용하여 'Product' 컬럼을 정확히 선택하고 출력했습니다. 이는 Series 객체로 반환되며, 문제의 목표를 완벽하게 달성했습니다.
3.  **info() 활용**: 선택된 컬럼에 대해 .info() 메서드를 사용한 것은 아주 좋은 습관입니다. 이를 통해 데이터 타입, Non-Null 개수 등을 빠르게 파악하여 데이터의 상태를 이해하는 데 큰 도움이 됩니다.

요구사항을 모두 만족하는 완벽한 코드입니다!
"""

# --- [모범 답안] ---
"""
# 아래 코드는 최초 나의 코딩과 동일합니다.
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
`df_products["Product"]` 문법을 사용하여 `'Product'` 컬럼을 성공적으로 선택했다. 이 결과가 **Pandas Series** 객체로 반환되는 것을 확인했다.
추가적으로 `.info()` 메서드를 사용하여 선택된 Series의 데이터 타입(dtype: object, 즉 문자열), Non-Null 개수, 메모리 사용량 등을 확인하여 컬럼의 특성을 이해하는 데 도움을 얻었다.

**추가 학습**:
Pandas Series와 DataFrame의 기본적인 구조와 차이점을 명확히 인지하는 것이 중요하다. Series는 1차원 배열과 유사한 단일 데이터 컬럼이며, DataFrame은 여러 Series가 모여 행과 열을 가진 2차원 테이블 구조를 이룬다. 단일 대괄호로 컬럼을 선택하면 Series가 반환되고, 이중 대괄호로 선택하면 (단일 컬럼을 선택하더라도) DataFrame이 반환된다. 이는 Pandas에서 데이터를 다룰 때 중요한 차이점이므로 기억해야 한다.
"""
