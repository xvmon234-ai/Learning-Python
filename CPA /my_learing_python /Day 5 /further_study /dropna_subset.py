# --- 추가 학습: 파이썬 함수/메서드의 인자(Argument) 이해 및 데이터 구조 활용 ---

"""
**개요**:
`dropna` 메서드의 `subset` 매개변수 사용 시 겪는 혼란은 파이썬 함수(또는 객체의 메서드)가 입력을 받는 방식과, 그 입력으로 어떤 '형태'의 데이터를 기대하는지에 대한 이해 부족에서 비롯될 수 있습니다.
이는 파이썬 프로그래밍 전반에 걸쳐 매우 중요한 개념이므로, 이 부분을 명확히 하면 Pandas뿐만 아니라 다른 라이브러리를 사용할 때도 큰 도움이 됩니다.

**1. 파이썬 함수/메서드와 인자(Argument)**

* **함수(Function)와 메서드(Method)**: 특정 작업을 수행하는 코드 블록입니다.
    * **함수**: 독립적으로 호출됩니다. 예: `print()`, `len()`.
    * **메서드**: 특정 객체(예: DataFrame, List, String)에 속하여, 그 객체의 데이터를 가지고 작업을 수행합니다. 예: `df.dropna()`, `my_list.append()`, `my_string.upper()`.

* **인자(Argument) / 매개변수(Parameter)**: 함수/메서드에 전달하는 입력값입니다.
    * **위치 인자(Positional Argument)**: 순서가 중요합니다. 함수 정의 시 정해진 순서대로 값을 전달해야 합니다.
    * **키워드 인자(Keyword Argument)**: `이름=값` 형태로 전달합니다. 순서에 상관없이 이름을 통해 값을 지정하므로 명확합니다. `dropna(subset=...)`에서 `subset`은 키워드 인자입니다.

**2. 인자가 기대하는 '데이터 타입'과 '구조'**

함수나 메서드는 특정 작업을 수행하기 위해 특정 형태와 타입의 인자를 기대합니다.
이것이 헷갈리는 주된 이유인데, Pandas 메서드는 특히 다양한 형태의 입력을 받을 수 있기 때문입니다.

* **단일 값 (Single Value)**: 숫자, 문자열, 불리언(`True`/`False`) 등 하나의 값.
    * 예: `df.fillna(value=0)` -> `value`는 단일 숫자 0.
    * 예: `df.drop(index=0)` -> `index`는 단일 숫자 0.
* **리스트 (List `[]`)**: 여러 개의 항목을 순서대로 담는 파이썬의 핵심 데이터 구조입니다. 변경 가능합니다.
    * 예: `df.drop(columns=['col1', 'col2'])` -> `columns`는 문자열 리스트.
    * 예: `df.groupby(['colA', 'colB'])` -> `groupby`에 여러 컬럼 이름을 리스트로 전달.
    * **`dropna(subset=[컬럼1, 컬럼2, ...])`**: `subset`은 여러 컬럼 이름을 대상으로 결측치를 검사해야 하므로, 이 컬럼 이름들을 리스트 형태로 전달받습니다.
* **튜플 (Tuple `()`)**: 리스트와 유사하게 여러 개의 항목을 담지만, 한 번 생성되면 변경할 수 없습니다 (불변).
    * 예: `df.shape` (속성이지만, 결과가 튜플 형태)
    * `dropna(subset=('col1', 'col2'))`와 같이 튜플로도 전달 가능합니다.
* **딕셔너리 (Dictionary `{}`)**: `키: 값` 쌍으로 데이터를 저장하는 구조입니다.
    * 예: `df.rename(columns={'old_name': 'new_name'})` -> `columns`는 딕셔너리.

**3. `dropna(subset=...)`를 통한 이해 확장**

`dropna` 메서드는 결측치를 처리하는 '행동'을 합니다. 이때 `subset` 인자는 "어떤 컬럼들을 기준으로 이 행동을 할 것인가?"를 지정합니다.

* **`subset='컬럼명'` (문자열)**: 단일 컬럼을 기준으로만 검사하고 싶을 때 사용합니다.
    * `df.dropna(subset='A')`: 'A' 컬럼에만 NaN이 있으면 해당 행 삭제.
* **`subset=['컬럼명1', '컬럼명2', ...]` (리스트)**: 여러 컬럼을 기준으로 동시에 검사하고 싶을 때 사용합니다.
    * `df.dropna(subset=['A', 'C'])`: 'A' 또는 'C' (혹은 둘 다)에 NaN이 있으면 해당 행 삭제 (기본 `how='any'`일 경우).

여기서 `subset`이 리스트를 받는 이유는, Pandas가 특정 '여러' 컬럼에 대해 동시에 작업을 수행해야 하기 때문입니다. 마치 수학 문제에서 '집합'을 다루듯이, 관련 있는 여러 항목을 묶어서 전달하는 것이죠.

**4. 파이썬 전반적인 이해를 위한 팁**

* **도움말/문서 적극 활용 (`help()`, `?`)**:
    * `help(pd.DataFrame.dropna)` 또는 `pd.DataFrame.dropna?`를 실행하면 해당 메서드가 어떤 인자들을 받는지, 각 인자의 역할과 기대하는 데이터 타입이 무엇인지 상세히 알려줍니다. 이것이 가장 정확하고 빠른 정보 습득 방법입니다.
    * `subset : column label or sequence of labels, optional` 이와 같은 설명을 통해 `subset`이 단일 컬럼 레이블(문자열) 또는 레이블들의 시퀀스(리스트, 튜플)를 받는다는 것을 알 수 있습니다.
* **에러 메시지 읽기**: `TypeError`나 `ValueError`는 인자의 타입이나 값이 잘못되었을 때 발생합니다. 에러 메시지에 어떤 타입이 기대되었는지 힌트가 있을 때가 많습니다.
* **작은 예제로 실험**: 새로운 함수나 메서드를 배울 때는 항상 간단한 예제 데이터를 만들어 직접 실행하고 결과를 확인하는 것이 좋습니다.
* **기본 파이썬 데이터 구조 숙달**: 리스트, 튜플, 딕셔너리, 셋(set) 등 파이썬의 기본 데이터 구조들이 어떻게 사용되고 어떤 특징을 가지는지 확실히 이해하는 것이 중요합니다. 이들은 Pandas를 포함한 거의 모든 파이썬 라이브러리에서 인자로 자주 사용됩니다.

이러한 접근 방식을 통해 `subset`과 같은 특정 인자뿐만 아니라, 파이썬 코드 전반에서 함수/메서드 사용에 대한 자신감을 얻을 수 있을 것입니다.
"""

# --- 실습 예시: 함수 인자 타입과 구조 ---

def process_data(value, names_list, config_dict):
    """
    다양한 타입의 인자를 받는 예시 함수.
    Args:
        value (int): 처리할 단일 숫자 값.
        names_list (list): 처리할 이름들의 리스트.
        config_dict (dict): 설정 옵션을 담은 딕셔너리.
    """
    print(f"단일 값 (int): {value}")
    print(f"이름 리스트 (list): {names_list}")
    print(f"설정 딕셔너리 (dict): {config_dict}")
    print(f"리스트의 첫 번째 이름: {names_list[0]}")
    print(f"딕셔너리의 'mode' 설정: {config_dict.get('mode')}")

# 함수 호출 예시
print("\n--- process_data 함수 호출 예시 ---")
process_data(10, ['Alice', 'Bob'], {'mode': 'fast', 'log': True})

# Pandas dropna와 subset 인자 예시
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Col1': [1, np.nan, 3, 4, np.nan],
    'Col2': [5, 6, np.nan, 8, 9],
    'Col3': ['a', 'b', 'c', np.nan, 'e']
})

print("\n--- 원본 DataFrame ---")
print(df)

print("\n--- dropna(subset='Col1') 예시 (단일 컬럼) ---")
# 'Col1'에 NaN이 있는 행 삭제
print(df.dropna(subset='Col1'))

print("\n--- dropna(subset=['Col1', 'Col2']) 예시 (리스트로 여러 컬럼) ---")
# 'Col1' 또는 'Col2' 중 하나라도 NaN이 있는 행 삭제
print(df.dropna(subset=['Col1', 'Col2']))

print("\n--- help() 함수를 통한 인자 확인 예시 ---")
# 주석을 풀고 실행하여 dropna 메서드의 문서(docstring)를 확인해보세요.
# help(pd.DataFrame.dropna)
# print(pd.DataFrame.dropna.__doc__) # 또는 이 방법
