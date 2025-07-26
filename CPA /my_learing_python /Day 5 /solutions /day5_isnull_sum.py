# --- [최초 나의 코딩] ---
import pandas as pd
import numpy as np

data = {'A': [1, 2, np.nan, 4, 5],
        'B': [np.nan, 6, 7, np.nan, 9],
        'C': ['apple', 'banana', 'cherry', 'date', np.nan],
        'D': [10, 20, 30, 40, 50]}

sample_data = pd.DataFrame(data)

print("\n --- 'A'의 결측치 개수 --- ")
print(sample_data["A"].isnull().sum())

print("\n --- 'B'의 결측치 개수 --- ")
print(sample_data["B"].isnull().sum())

print("\n --- 'C'의 결측치 개수 --- ")
print(sample_data["C"].isnull().sum())

print("\n --- 'D'의 결측치 개수 --- ")
print(sample_data["D"].isnull().sum())

print("\n --- DataFrame의 총 결측치 개수 --- ")
# print(sample_data.isnull.sum().sum()) #총결측치 구하는 부분에서 AttributeError가 발생했는데 해당 부분에 대해서 알려줘


# --- [코드 실행 결과] ---
"""
 --- 'A'의 결측치 개수 ---
1

 --- 'B'의 결측치 개수 ---
2

 --- 'C'의 결측치 개수 ---
1

 --- 'D'의 결측치 개수 ---
0

 --- DataFrame의 총 결측치 개수 ---
Traceback (most recent call last):
  File "<stdin>", line 21, in <module>
    print(sample_data.isnull.sum().sum())
AttributeError: 'DataFrame' object has no attribute 'isnull'
"""

# --- [피드백] ---
"""
코드 아주 훌륭하게 작성하셨습니다! `df.isnull().sum()`을 활용하여 각 컬럼별 결측치 개수를 정확히 파악했습니다. 이는 결측치 확인의 가장 기본적이고 핵심적인 방법입니다.

발생한 `AttributeError`는 Pandas 문법의 작은 차이에서 기인합니다. `isnull`은 DataFrame의 **메서드(method)**이므로 호출할 때 뒤에 괄호 `()`를 붙여줘야 합니다. `sample_data.isnull`처럼 괄호 없이 사용하면 `isnull`을 속성(attribute)처럼 접근하려 하지만, DataFrame 객체에는 `isnull`이라는 속성이 직접 존재하지 않기 때문에 오류가 발생합니다.

즉, `sample_data.isnull()`로 `isnull` 메서드를 호출해야만 `True`/`False`로 이루어진 DataFrame이 반환되고, 그 결과에 `.sum().sum()`을 체이닝하여 전체 결측치 개수를 구할 수 있습니다.

이 점을 제외하고는 모든 것이 완벽합니다!
"""

# --- [모범 답안] ---
import pandas as pd
import numpy as np

data = {'A': [1, 2, np.nan, 4, 5],
        'B': [np.nan, 6, 7, np.nan, 9],
        'C': ['apple', 'banana', 'cherry', 'date', np.nan],
        'D': [10, 20, 30, 40, 50]}

sample_data = pd.DataFrame(data)

# 각 컬럼별 결측치 개수 출력
print("\n--- 각 컬럼별 결측치 개수 ---")
print(sample_data.isnull().sum())

# DataFrame의 총 결측치 개수 출력
print("\n--- DataFrame의 총 결측치 개수 ---")
print(sample_data.isnull().sum().sum()) # 메서드 호출을 위한 괄호 추가

# --- [학습 기록] ---
"""
**학습 질문**: Pandas DataFrame에서 각 컬럼별 결측치 개수를 확인하는 방법과 DataFrame 전체의 총 결측치 개수를 확인하는 방법은 무엇일까? 특히 `AttributeError: 'DataFrame' object has no attribute 'isnull'` 오류는 왜 발생할까?

**문제 해결**:
1.  **DataFrame 생성**: 주어진 데이터를 사용하여 `sample_data` DataFrame을 성공적으로 생성했다.
2.  **각 컬럼별 결측치 개수 확인**: `sample_data["컬럼명"].isnull().sum()` 구문을 사용하여 'A', 'B', 'C', 'D' 각 컬럼의 결측치 개수를 정확하게 출력했다. `isnull()`이 각 요소의 결측 여부를 불리언 Series로 반환하고, 여기에 `sum()`을 적용하여 `True`(결측치)의 개수를 세는 방식이 매우 효과적임을 확인했다.
3.  **총 결측치 개수 확인 오류 해결**: `sample_data.isnull.sum().sum()`에서 `AttributeError`가 발생한 원인은 `isnull`을 메서드가 아닌 속성처럼 사용했기 때문이다. Pandas에서 `isnull()`은 함수처럼 호출해야 하는 **메서드**이다. 따라서 `sample_data.isnull()`과 같이 괄호를 붙여 호출함으로써 이 오류를 해결할 수 있었다. `sample_data.isnull()`이 전체 DataFrame에 대한 불리언 DataFrame을 반환하고, 여기에 `.sum()`을 처음 적용하면 컬럼별 결측치 개수 Series가, 다시 `.sum()`을 적용하면 총 결측치 개수가 나오는 원리를 명확히 이해했다.

**추가 학습**:
* **메서드(Method)와 속성(Attribute)의 차이**:
    * **메서드**: 특정 작업을 수행하는 **함수**입니다. 호출할 때 항상 괄호 `()`를 붙여야 합니다 (예: `df.isnull()`, `df.sum()`, `df.drop()`).
    * **속성**: 객체가 가지고 있는 **값**이나 특징입니다. 괄호 없이 직접 접근합니다 (예: `df.shape`, `df.columns`, `df.index`).
    이러한 차이를 명확히 인지하는 것이 Pandas 문법 오류를 줄이는 데 중요함을 다시 한번 확인했습니다.
"""
