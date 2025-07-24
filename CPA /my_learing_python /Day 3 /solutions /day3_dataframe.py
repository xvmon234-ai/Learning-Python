# ==============================================================================
# [문제 3] 불완전한 데이터로 DataFrame 생성
# ==============================================================================

# [최초 나의 코딩]
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

"""
[피드백]
문제 해결: 행 기준 딕셔너리 리스트(`data_list`)를 사용하여 `DataFrame`을 생성하는 방법을 정확히 이해하고 적용했습니다. 특히, 각 딕셔너리에 컬럼 구성이 달라도 `Pandas`가 누락된 값을 `NaN`으로 채워 유연하게 `DataFrame`을 생성하는 특성을 잘 확인했습니다. `df.info()`와 `print(df)`를 통해 데이터 타입을 확인하고 모든 행을 출력하는 요구사항도 잘 따랐습니다.
코드 품질: 간결하고 명확하게 `DataFrame`을 생성하고 탐색하는 코드를 작성했습니다.
학습 통찰: 컬럼 길이가 다른 데이터를 `DataFrame`으로 만들 때 `ValueError`가 발생하는 딕셔너리-리스트(컬럼 기준) 방식과 달리, `NaN`으로 자동으로 채워지는 리스트-딕셔너리(행 기준) 방식의 유연성을 직접 경험하며 그 장점을 명확히 파악한 점이 중요합니다. 중구난방의 데이터를 처리할 때 매우 유용한 방식임을 이해했을 것입니다.
"""

# [모범 답안]
# import pandas as pd

# data_list = [
#     {'Product': 'Laptop', 'Price': 1200, 'Weight_kg': 2.5},
#     {'Product': 'Mouse', 'Price': 25, 'Manufacturer': 'Logitech'}, # Weight_kg 누락, Manufacturer 추가
#     {'Product': 'Keyboard', 'Weight_kg': 1.0, 'Layout': 'US'}, # Price 누락, Layout 추가
#     {'Product': 'Monitor'} # Price, Weight_kg, Manufacturer, Layout 모두 누락
# ]

# # 리스트-딕셔너리 조합 (행 기준)으로 DataFrame 생성
# df_flexible = pd.DataFrame(data_list)

# print("\n --- df_flexible (info()) --- ")
# df_flexible.info()

# print("\n --- df_flexible (모든 행) --- ")
# print(df_flexible)
