# ==============================================================================
# [문제 3] 불완전한 데이터로 DataFrame 생성
# ==============================================================================

# --- [최초 나의 코딩] ---
import pandas as pd

data_list = [
    {'Product': 'Laptop', 'Price': 1200, 'Weight_kg': 2.5},
    {'Product': 'Mouse', 'Price': 25, 'Manufacturer': 'Logitech'},
    {'Product': 'Keyboard', 'Weight_kg': 1.0, 'Layout': 'US'},
    {'Product': 'Monitor'}
]

df_flexible = pd.DataFrame(data_list)

print("\n --- df_flexible (info()) --- ")
df_flexible.info()

print("\n --- df_flexible 모든 행 --- ")
print(df_flexible)

# --- [피드백] ---
"""
문제 해결: 행 기준 딕셔너리 리스트(`data_list`)를 사용하여 `DataFrame`을 생성하는 방법을 정확히 이해하고 적용했습니다. 특히, 각 딕셔너리에 컬럼 구성이 달라도 `Pandas`가 누락된 값을 `NaN`으로 채워 유연하게 `DataFrame`을 생성하는 특성을 잘 확인했습니다. `df.info()`와 `print(df)`를 통해 데이터 타입을 확인하고 모든 행을 출력하는 요구사항도 잘 따랐습니다.
코드 품질: 간결하고 명확하게 `DataFrame`을 생성하고 탐색하는 코드를 작성했습니다.
학습 통찰: 컬럼 길이가 다른 데이터를 `DataFrame`으로 만들 때 `ValueError`가 발생하는 딕셔너리-리스트(컬럼 기준) 방식과 달리, `NaN`으로 자동으로 채워지는 리스트-딕셔너리(행 기준) 방식의 유연성을 직접 경험하며 그 장점을 명확히 파악한 점이 중요합니다. 중구난방의 데이터를 처리할 때 매우 유용한 방식임을 이해했을 것입니다.
"""

# --- [모범 답안] ---
# import pandas as pd

# data_list = [
#     {'Product': 'Laptop', 'Price': 1200, 'Weight_kg': 2.5},
#     {'Product': 'Mouse', 'Price': 25, 'Manufacturer': 'Logitech'}, # Weight_kg 누락, Manufacturer 추가
#     {'Product': 'Keyboard', 'Weight_kg': 1.0, 'Layout': 'US'}, # Price 누락, Layout 추가
#     {'Product': 'Monitor'} # Price, Weight_kg, Manufacturer, Layout 모두 누락
# ]

# # 리스트-딕셔너리 조합 (행 기준)으로 DataFrame 생성
# # df_flexible = pd.DataFrame(data_list)

# # print("\n --- df_flexible (info()) --- ")
# # df_flexible.info()

# # print("\n --- df_flexible (모든 행) --- ")
# # print(df_flexible)

# --- [학습 기록] ---
"""
**학습 질문**: 딕셔너리-리스트(컬럼 기준) 방식으로 DataFrame을 생성할 때와 달리, 리스트-딕셔너리(행 기준) 방식에서는 컬럼 길이가 달라도 `ValueError`가 발생하지 않고 `NaN`으로 채워지는 이유와 그 유용성이 궁금했음.

**문제 해결**: 제공된 `data_list`를 `pd.DataFrame()`으로 직접 생성하여, 컬럼 구성이 다른 행들이 누락된 컬럼에 `NaN`이 채워진 채로 DataFrame이 만들어지는 것을 확인했음. `df.info()`를 통해 각 컬럼의 `Non-Null Count`가 달라진 것을 파악했고, 이는 행 기준 DataFrame 생성이 데이터의 유연한 처리에 강점이 있다는 것을 시사했음.

**추가 학습 (공인회계사 업무와의 관련성 포함)**:
1. `DataFrame` 생성 방식(컬럼 기준 vs 행 기준)의 장단점을 다시 한번 명확히 정리하고, 각 방식이 어떤 유형의 데이터나 상황에 더 적합한지 예시와 함께 정리해야 함.
2. `NaN` (Not a Number) 값의 의미와 Pandas에서 `NaN`을 다루는 기본적인 방법(예: `df.isnull()`, `df.fillna()`, `df.dropna()`)을 학습해야 함.
3. DataFrame의 각 컬럼별 데이터 타입(`Dtype`)이 `NaN` 값 존재 여부에 따라 어떻게 변화할 수 있는지(예: 정수형 컬럼이 `float`으로 변환되는 경우) 이해해야 함.
   * 💡 **공인회계사 업무 연관성**: 실제 회계 데이터는 종종 **불완전하거나 형식이 일관되지 않은 경우**가 많음 (예: 여러 시스템에서 추출된 데이터 통합, 수기 입력 오류). `NaN` 값을 유연하게 처리하고 식별하는 능력은 **데이터 클렌징(data cleansing) 및 전처리 단계**에서 매우 중요함. `NaN`이 재무 분석 결과에 미칠 수 있는 영향을 이해하고, 이를 적절히 채우거나 제거하는 방법을 아는 것은 **데이터의 정확성과 신뢰성을 확보**하는 데 필수적임. 이는 **감사 절차 수행 시 데이터 유효성 검증**이나 **재무 모델링 시 데이터 누락 처리**에 직접적으로 연결됨.
"""
