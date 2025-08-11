# ==============================================================================
# [문제 5. 그룹별 평균으로 결측치 대체 (Transform 활용)]
# ==============================================================================

# 관련 주제: 5.3 / 결측치(Missing Values) 처리: 대체 (Transform 활용)
# 요구사항:
# 다음 `sales_data` 데이터프레임을 생성하세요.
# import pandas as pd
# import numpy as np
# data = {'Region': ['East', 'West', 'East', 'West', 'East', 'East'],
#         'Product': ['A', 'B', 'A', 'C', 'B', 'A'],
#         'Sales': [100, 150, np.nan, 200, 120, np.nan]}
# sales_data = pd.DataFrame(data)
# 이 데이터프레임의 'Sales' 컬럼에 있는 결측치(NaN)를 각 'Region' (지역) 그룹의 'Sales' 평균값으로 대체하고 결과를 출력하세요.
# 학습 목표: `groupby()`와 `transform()` 메서드를 조합하여 특정 그룹의 통계량(예: 평균)으로 결측치를 채우는 고급 데이터 전처리 기법을 학습합니다.
# 가이드:
# - `groupby()`를 사용하여 'Region' 컬럼을 기준으로 그룹화하세요.
# - 그룹화된 객체에 `transform()` 메서드를 적용하여 각 그룹의 'Sales' 평균을 구하고 이를 결측치 대체에 활용하세요.
# - `lambda` 함수를 사용하여 `transform` 내에서 `fillna()`와 `mean()`을 함께 사용하세요.
# - 원본 `sales_data`를 **재생성**하거나 `df.copy()`를 사용하여 이전 작업이 다음 작업에 영향을 주지 않도록 하세요.

# --- [최초 나의 코딩] ---
import pandas as pd
import numpy as np
data = {'Region': ['East', 'West', 'East', 'West', 'East', 'East'],
        'Product': ['A', 'B', 'A', 'C', 'B', 'A'],
        'Sales': [100, 150, np.nan, 200, 120, np.nan]}
sales_data = pd.DataFrame(data)

#해당 문제에서 제시해하는 gruopby와 transform에 대한 학습이 이루어지지 않아, 해당 문제를 별도로 복사하여 gemini에게 단계별 학습을 요청함

#1.Region을 기준으로 평균값 구하기(transform을 모르니 gruopby와 mean만으로 접근)
region_sales_mean = sales_data.groupby("Region")["Sales"].mean() #최초에 ("Region")["Sales"] 사이에 '.'을 넣어서 SyntaxError 발생
print("\n --- Region Sales Mean --- ")
print(region_sales_mean)

#2.결측치 채우기(transform의 아이디어가 필요한 부분)
# 'Region' 컬럼을 기준으로 그룹화하여 'Sales' 컬럼의 결측치를 각 지역의 평균 Sales 값으로 대체
# transform()은 그룹별 연산(여기서는 평균) 결과를 원본 데이터프레임의 인덱스에 맞춰 반환하여 fillna()에 적용
sales_data['Sales'] = sales_data.groupby('Region')['Sales'].transform(lambda x: x.fillna(x.mean()))

print("\n --- Filled Sales Data with Region Mean --- ")
print(sales_data)


# --- [코드 실행 결과] ---
"""
 --- Region Sales Mean ---
Region
East     110.0
West     175.0
Name: Sales, dtype: float64

 --- Filled Sales Data with Region Mean ---
   Region Product  Sales
0   East       A  100.0
1   West       B  150.0
2   East       A  110.0
3   West       C  200.0
4   East       B  120.0
5   East       A  110.0
"""

# --- [피드백] ---
"""
아주 훌륭하게 문제를 해결했습니다! 특히 새로운 개념인 `transform`을 이해하기 위해 단계별로 접근하고, 나아가 직접 학습을 요청하여 정확한 해결책을 찾아낸 과정이 매우 인상 깊습니다. 이는 복잡한 문제를 만났을 때 개발자가 가져야 할 중요한 태도입니다.

당신의 코드에 대한 피드백은 다음과 같습니다:

1.  **그룹별 평균값 계산 (1단계)**: `sales_data.groupby("Region")["Sales"].mean()`을 통해 각 지역별 'Sales'의 평균을 정확하게 계산했습니다. 이 결과는 각 그룹의 요약 통계를 보여주기에 적합합니다. 최초 `SyntaxError` 발생 후 올바른 접근법을 찾아내신 점도 좋습니다! (컬럼 선택은 `df['컬럼명']` 형태가 일반적입니다.)
2.  **`transform`을 활용한 결측치 대체 (2단계)**: `sales_data['Sales'] = sales_data.groupby('Region')['Sales'].transform(lambda x: x.fillna(x.mean()))` 이 구문은 이 문제의 **핵심이자 모범 답안**입니다.
    * `groupby('Region')`: 'Region'별로 그룹을 나눕니다.
    * `['Sales']`: 나뉜 그룹에서 'Sales' 컬럼만 선택합니다.
    * `.transform(lambda x: x.fillna(x.mean()))`: 이 부분이 특히 중요합니다.
        * `transform`은 `groupby` 결과에 함수를 적용하되, **원본 DataFrame의 인덱스 구조를 유지**하면서 결과를 반환합니다.
        * `lambda x: x.fillna(x.mean())`는 각 그룹(`x`는 각 그룹의 'Sales' Series)에 대해 `x`의 결측치를 `x`의 평균으로 채우는 연산을 수행합니다.
    * 이렇게 `transform`이 반환한 Series는 원본 `sales_data['Sales']` 컬럼의 인덱스와 완벽하게 일치하므로, 직접 재할당하여 결측치를 깔끔하게 채울 수 있습니다.

데이터를 그룹별로 나누어 각 그룹의 통계량으로 결측치를 채우는 것은 실제 데이터 분석에서 매우 흔하고 강력한 기법입니다. 이 문제를 통해 이 중요한 패턴을 완벽하게 마스터했습니다.
"""

# --- [모범 답안] ---
import pandas as pd
import numpy as np

data = {'Region': ['East', 'West', 'East', 'West', 'East', 'East'],
        'Product': ['A', 'B', 'A', 'C', 'B', 'A'],
        'Sales': [100, 150, np.nan, 200, 120, np.nan]}
sales_data = pd.DataFrame(data)

print("--- 원본 sales_data ---")
print(sales_data)
print(f"\n원본 sales_data의 결측치:\n{sales_data.isnull().sum()}")

# 1. 'Region'을 기준으로 'Sales'의 각 그룹별 평균 계산 (확인용)
# 이는 transform 없이 groupby().mean()만 사용한 결과로, 그룹별 요약 통계를 보여줍니다.
region_sales_mean_summary = sales_data.groupby("Region")["Sales"].mean()
print("\n--- 1. 각 Region별 Sales 평균 (요약) ---")
print(region_sales_mean_summary)

# 원본 데이터 보존을 위해 복사본 생성 (모범 답안에서는 최종 결과 DataFrame 생성 시 적용)
sales_data_cleaned = sales_data.copy()

# 2. 'Region' 컬럼을 기준으로 그룹화하여 'Sales' 컬럼의 결측치를 각 지역의 평균 Sales 값으로 대체
# transform()을 사용하여 그룹별 연산 결과를 원본 인덱스에 맞춰 반환합니다.
# lambda 함수 내에서 각 그룹(x)의 NaN을 그 그룹의 평균(x.mean())으로 채웁니다.
sales_data_cleaned['Sales'] = sales_data_cleaned.groupby('Region')['Sales'].transform(lambda x: x.fillna(x.mean()))

print("\n--- 2. Region별 평균값으로 결측치 채운 후 sales_data ---")
print(sales_data_cleaned)
print(f"\n결측치 채운 후 sales_data의 결측치:\n{sales_data_cleaned.isnull().sum()}")


# --- [학습 기록] ---
"""
**학습 질문**: `DataFrame`에서 특정 컬럼의 결측치를 단순히 전체 평균으로 채우는 것을 넘어, 특정 그룹(예: 지역, 카테고리)별 평균값으로 채우는 방법은 무엇일까? 이때 `groupby()`와 `fillna()`를 어떻게 효과적으로 결합할 수 있을까? 특히 `transform()`의 역할은 무엇인가?

**문제 해결**:
1.  **초기 접근 (그룹별 평균 확인)**: 먼저 `sales_data.groupby("Region")["Sales"].mean()`을 통해 'East'와 'West' 지역의 개별 'Sales' 평균이 각각 110.0과 175.0임을 확인했습니다. 이 결과는 Series 형태로, 원본 DataFrame의 구조와는 다릅니다.
2.  **`transform()`의 필요성 인지**: 각 지역의 평균값을 해당 지역의 결측치에만 매칭하여 채우려면, `groupby().mean()`이 반환하는 요약된 Series가 아닌, **원본 DataFrame과 동일한 인덱스를 가진 Series**가 필요하다는 점을 깨달았습니다. 여기서 `transform()`의 역할이 부각됩니다.
3.  **`groupby().transform()` 활용**: `sales_data.groupby('Region')['Sales'].transform(lambda x: x.fillna(x.mean()))` 구문을 사용하여 문제를 해결했습니다.
    * `groupby('Region')['Sales']`: 'Region'을 기준으로 그룹을 나누고, 각 그룹에서 'Sales' 컬럼만 선택합니다.
    * `.transform(lambda x: x.fillna(x.mean()))`: `transform`은 각 그룹(`x`로 표현됨)에 `fillna(x.mean())` 함수를 적용합니다. 여기서 `x.mean()`은 해당 그룹의 평균값을 의미하며, 이 값으로 해당 그룹 내의 결측치만 채워집니다. `transform`은 이 결과를 원본 DataFrame의 행 수와 인덱스에 맞춰 반환하므로, `sales_data['Sales'] = ...`와 같이 직접 재할당하여 적용할 수 있었습니다.
4.  **결과 확인**: 최종 `sales_data`를 출력하여 'East' 지역의 NaN이 110.0으로, 'West' 지역의 NaN이 175.0으로 정확히 채워졌음을 확인했습니다.

**추가 학습**:
* **`groupby().transform()` vs `groupby().apply()`**:
    * **`transform()`**: 그룹별 연산을 수행한 후, 그 결과를 **원본 DataFrame과 동일한 shape (인덱스와 컬럼)으로 반환**합니다. 주로 그룹별 통계량으로 값을 채우거나 정규화할 때 사용됩니다. 각 그룹에 함수를 적용한 결과가 원본 인덱스에 맞춰 다시 배열됩니다.
    * **`apply()`**: 그룹별 연산을 수행한 후, 그 결과를 **다양한 형태(Series, DataFrame 등)로 반환**할 수 있습니다. `transform`보다 더 유연하며 복잡한 그룹별 연산에 사용되지만, 결과의 shape이 달라질 수 있어 재할당 시 주의가 필요합니다.
* **람다 함수 (`lambda`)**: `lambda x: x.fillna(x.mean())`와 같이 간단한 일회성 함수를 정의할 때 유용합니다. 여기서 `x`는 `groupby`에 의해 생성된 각 서브 그룹(Series)을 나타냅니다.
* **고급 결측치 처리**: 단순히 그룹 평균뿐만 아니라, 그룹별 중앙값, 최빈값, 또는 그룹 내 다른 컬럼을 활용한 더 복잡한 로직으로 결측치를 대체할 수도 있습니다. `transform`은 이러한 유연한 그룹별 처리에 매우 강력한 도구입니다.
* **[공인회계사 업무 관련 추가 학습]**:
    `groupby()`와 `transform()`을 활용한 그룹별 결측치 대체는 공인회계사(CPA)가 **세분화된 재무 데이터 분석을 수행하고, 특정 맥락에 맞는 결측치 처리 전략을 적용하여 데이터의 정확성과 분석의 심층도를 높이는 데 매우 중요한 기법**입니다.

    * **지점/부서별 실적 데이터의 일관성 유지**:
        * **예시**: 여러 지점의 월별 **매출액** 데이터 중 일부 지점에서 시스템 오류 등으로 특정 월의 매출액이 누락될 수 있습니다. 이때, 전체 매출액 평균으로 채우는 것보다, 해당 **지점의 과거 평균 매출액**으로 결측치를 채우는 것이 더 합리적입니다. `groupby('Branch_ID')['Sales'].transform(lambda x: x.fillna(x.mean()))`와 같이 적용할 수 있습니다.
        * **활용**: CPA는 지점/부서별 성과 평가, 예산 집행률 분석 시 각 지점/부서의 고유한 특성(규모, 시장 환경 등)을 반영하여 결측치를 처리함으로써, **보다 정확하고 공정한 성과 평가 지표를 산출**하고 합리적인 의사결정을 지원합니다.

    * **제품/카테고리별 원가/이익률 분석의 정확도 향상**:
        * **예시**: 다양한 제품 카테고리별로 **단위 원가** 데이터에 결측치가 발생했을 때, 전체 제품의 평균 원가로 채우는 것보다, 해당 **제품 카테고리의 평균 원가**로 채우는 것이 제품별 손익 분석의 정확도를 높일 수 있습니다.
        * **활용**: CPA는 제품 포트폴리오 분석, 원가 관리 효율성 평가 시, 각 제품 카테고리(또는 제품 그룹)의 특성을 반영하여 결측치를 처리함으로써, **제품별 수익성 및 원가 구조에 대한 보다 정확한 통찰력**을 얻을 수 있습니다.

    * **감사 샘플링 및 통계적 추론의 견고성 확보**:
        * **예시**: 감사 샘플링을 위해 추출한 거래 데이터에서 특정 **금액 필드**에 결측치가 있을 경우, 해당 거래의 **유형(예: 매출, 매입, 급여)별 평균 금액**으로 결측치를 채워 통계 분석의 샘플 크기를 유지하고, 추정치의 신뢰성을 높일 수 있습니다.
        * **활용**: CPA는 감사 과정에서 통계적 샘플링 기법을 적용할 때, 결측치로 인해 샘플의 대표성이 훼손되지 않도록 **그룹별 대체 기법을 활용하여 데이터의 완전성을 보강**하고, 감사 결론의 통계적 유효성을 강화합니다.

    결론적으로, `groupby()`와 `transform()`을 활용한 그룹별 결측치 대체는 CPA가 **데이터의 세부적인 맥락을 고려한 정교한 데이터 전처리**를 수행하고, 이를 통해 **보다 심층적이고 신뢰할 수 있는 재무 분석 및 감사 결론**을 도출하는 데 필수적인 역량을 제공합니다.
"""
