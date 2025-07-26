# --- 추가 학습: 메서드(Method)와 속성(Attribute)의 차이 ---

"""
**개요**:
Pandas를 포함한 객체지향 프로그래밍에서 메서드와 속성은 객체와 상호작용하는 두 가지 주요 방법입니다.
이 둘의 차이를 명확히 이해하는 것은 코드 작성 시 오류를 줄이고,
객체가 제공하는 기능을 효과적으로 활용하는 데 필수적입니다.

**메서드(Method)**:
* **정의**: 객체가 수행할 수 있는 '행동' 또는 '기능'을 나타내는 함수입니다.
* **호출 방법**: 항상 뒤에 괄호 `()`를 붙여서 호출합니다. 괄호 안에 필요한 인자(argument)를 전달할 수 있습니다.
* **예시**:
    * `df.isnull()`: DataFrame의 각 요소가 결측치인지 여부를 확인하는 '행동'을 수행합니다.
    * `df.sum()`: DataFrame의 합계를 계산하는 '행동'을 수행합니다.
    * `df.drop()`: DataFrame에서 특정 행이나 열을 제거하는 '행동'을 수행합니다.
    * `df.head(5)`: DataFrame의 상위 5개 행을 보여주는 '행동'을 수행합니다.

**속성(Attribute)**:
* **정의**: 객체가 가지고 있는 '상태' 또는 '특징'을 나타내는 변수입니다. 객체에 저장된 값이나 데이터를 직접적으로 나타냅니다.
* **호출 방법**: 괄호 `()` 없이 직접 접근합니다.
* **예시**:
    * `df.shape`: DataFrame의 차원(행, 열의 개수)이라는 '특징'을 나타내는 튜플입니다.
    * `df.columns`: DataFrame의 열 이름 목록이라는 '값'을 나타냅니다.
    * `df.index`: DataFrame의 인덱스(행 레이블)라는 '값'을 나타냅니다.
    * `df.dtypes`: DataFrame 각 컬럼의 데이터 타입이라는 '정보'를 나타냅니다.

**왜 중요한가요?**:
Pandas에서 `AttributeError`는 메서드를 속성처럼 호출하거나 (예: `df.isnull` 대신 `df.isnull()`), 존재하지 않는 속성에 접근하려 할 때 자주 발생합니다. 이 차이를 이해하면 이러한 일반적인 오류를 쉽게 진단하고 수정할 수 있습니다.

**실습 코드 예시**:
"""

import pandas as pd
import numpy as np

# 데이터프레임 생성
df = pd.DataFrame({
    'col1': [1, 2, np.nan, 4],
    'col2': ['A', 'B', 'C', 'D']
})

print("--- DataFrame의 속성 접근 예시 ---")
# shape: (행 수, 열 수)를 나타내는 튜플 (속성)
print(f"df.shape: {df.shape}")
# columns: 열 이름 (속성)
print(f"df.columns: {df.columns}")
# index: 행 인덱스 (속성)
print(f"df.index: {df.index}")
# dtypes: 각 컬럼의 데이터 타입 (속성)
print(f"df.dtypes:\n{df.dtypes}")

print("\n--- DataFrame의 메서드 호출 예시 ---")
# isnull(): 결측치 여부를 반환 (메서드)
print(f"df.isnull():\n{df.isnull()}")
# sum(): 합계를 계산 (메서드)
print(f"df.sum():\n{df.sum()}")
# head(): 상위 n개 행 반환 (메서드)
print(f"df.head(2):\n{df.head(2)}")

# 잘못된 접근 예시 (AttributeError 발생):
# print(df.isnull) # TypeError: 'method' object is not subscriptable (혹은 AttributeError)
# print(df.shape()) # TypeError: 'tuple' object is not callable
