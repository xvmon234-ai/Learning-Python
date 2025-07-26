# ==============================================================================
# [문제 6.1.3] Pandas 그룹화 및 집계 (Day 6 학습 내용)
# ==============================================================================

# --- [최초 나의 코딩] ---
import pandas as pd
data = {'City': ['Seoul', 'Busan', 'Seoul', 'Jeju', 'Busan', 'Seoul'],
        'Date': ['2023-07-01', '2023-07-01', '2023-07-02', '2023-07-02', '2023-07-03', '2023-07-03'],
        'Temperature': [28, 26, 30, 25, 27, 29]}
weather_df = pd.DataFrame(data)

max_temperature = weather_df.groupby("City")["Temperature"].max()

print("\n--- City with the Highest Temperature ---")
print(max_temperature)

# --- [코드 실행 결과] ---
"""
--- City with the Highest Temperature ---
City
Busan    27
Jeju     25
Seoul    30
Name: Temperature, dtype: int64
"""

# --- [피드백] ---
"""
문제 6.1.3을 완벽하게 해결하셨습니다! `groupby()`와 `max()` 집계 함수를 활용하여 각 도시별 최고 기온을 정확하게 찾아냈습니다.

1.  **정확한 그룹화**: `weather_df.groupby("City")`를 사용하여 데이터를 도시별로 올바르게 그룹화했습니다.
2.  **적절한 컬럼 선택 및 집계**: 그룹화된 데이터에서 `'Temperature'` 컬럼을 선택하고 `.max()` 메서드를 적용하여 각 그룹의 최고값을 도출한 것은 매우 적절합니다.
3.  **명확한 변수명**: `max_temperature`와 같이 변수명을 직관적으로 사용하여 코드의 가독성을 높였습니다.

이 코드는 Pandas의 `groupby()`와 단일 집계 함수를 이용한 데이터 요약의 기본적인 패턴을 정확히 따르고 있으며, 매우 효율적이고 깔끔한 풀이입니다.
"""

# --- [모범 답안] ---
# 이미 '최초 나의 코딩'에서 모범적으로 해결되었으므로, 추가적인 모범 답안은 생략합니다.
# 다만, 메서드 체이닝을 활용하여 한 줄로 작성하는 것도 일반적인 모범 사례입니다.
# city_max_temp_chained = weather_df.groupby("City")["Temperature"].max()
# print("\n--- City with the Highest Temperature (모범 답안 예시 - 체이닝) ---")
# print(city_max_temp_chained)


# --- [학습 기록] ---
"""
**학습 질문**: 각 도시별로 가장 높은 기온을 찾아내려면 Pandas의 어떤 기능을 사용해야 할까?

**문제 해결**:
1.  **데이터프레임 준비**: 문제에서 주어진 기온 데이터를 포함하는 `weather_df`를 생성했습니다.
2.  **`groupby()`로 그룹화**: `weather_df.groupby("City")`를 사용하여 데이터를 `'City'` 컬럼을 기준으로 그룹화했습니다. 이렇게 하면 'Seoul', 'Busan', 'Jeju' 각각에 대한 독립적인 그룹이 생성됩니다.
3.  **`max()`로 최고값 찾기**: 그룹화된 객체에서 `'Temperature'` 컬럼을 선택한 후, `.max()` 집계 함수를 호출하여 각 도시 그룹 내에서 'Temperature'의 최고값을 추출했습니다. 이 결과는 각 도시를 인덱스로 하고 최고 기온을 값으로 하는 `Series` 형태로 반환됩니다.
4.  **결과 확인**: 출력된 결과에서 각 도시별로 기록된 가장 높은 기온이 정확하게 계산되었음을 확인했습니다.

**추가 학습**:
* **`max()` 외 다른 집계 함수**: `min()`, `mean()`, `sum()`, `count()`, `std()` 등 다양한 집계 함수를 `groupby()`와 함께 사용하여 그룹별 통계량을 손쉽게 계산할 수 있습니다.
* **`Series` vs `DataFrame`**: `groupby()` 후 단일 컬럼을 선택하고 단일 집계를 수행하면 결과는 기본적으로 `Series` 객체가 됩니다. 만약 결과를 DataFrame 형태로 받고 싶다면 `.reset_index()`를 추가로 사용할 수 있습니다. 이 문제의 경우 `Series` 형태로도 정보 파악에 충분합니다.
* **데이터 요약의 중요성**: `groupby()`와 집계 함수는 대규모 데이터셋에서 특정 기준에 따른 핵심 요약 정보를 빠르게 얻을 수 있게 해주므로, 데이터 분석에서 매우 중요한 기법입니다.
"""
