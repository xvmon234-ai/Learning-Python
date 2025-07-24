-----

## **Day 3: Pandas DataFrame 기초 및 인덱스 다루기**

### **🎯 학습 목표**

  * **Pandas DataFrame의 기본적인 구조와 생성 방법**을 이해하고 활용할 수 있습니다.
  * 다양한 데이터 소스(Python 객체, CSV 파일)로부터 **DataFrame을 효율적으로 생성**할 수 있습니다.
  * **DataFrame의 인덱스(Index) 개념**을 명확히 이해하고, 인덱스를 **설정, 변경, 초기화**하는 방법을 숙달합니다.
  * `inplace` 및 `drop`과 같은 핵심 매개변수의 동작 방식을 파악하여 **DataFrame 조작 시 원본 데이터의 변경 여부를 제어**할 수 있습니다.
  * 데이터 탐색을 위한 **기본적인 DataFrame 속성 및 메서드**를 활용할 수 있습니다.

-----

### **📝 Day 3 학습 요약 정리: Pandas 기초 다지기**

오늘 우리는 Pandas의 핵심인 DataFrame 생성, 파일 입출력, 그리고 데이터 탐색 및 요약 통계를 깊이 있게 학습했습니다.

-----

### **💡 주요 주제별 정리**

#### **1. DataFrame 및 Series 생성과 인덱스 설정**

  * **설명**: Pandas의 기본 데이터 구조인 DataFrame(2차원 테이블)과 Series(1차원 배열)를 파이썬 딕셔너리나 딕셔너리 리스트를 활용해 직접 만드는 방법을 배웠습니다. 또한, 특정 컬럼을 DataFrame의 행 인덱스로 지정하는 방법을 익혔습니다.
  * **이론**:
      * **🌟🌟🌟 `pd.DataFrame()` / `pd.Series()`**: Pandas의 기본 데이터 구조를 생성하는 함수입니다. 데이터를 분석하기 위한 첫 단계가 됩니다.
      * **🌟🌟 `df.set_index('컬럼명')`**: 특정 컬럼을 DataFrame의 행 인덱스로 설정합니다. 이 메서드는 새로운 DataFrame을 반환하므로, 변경사항을 적용하려면 반드시 `df = df.set_index(...)` 형태로 **재할당**해야 합니다.
  * **암기할 사항**:
      * `pd.DataFrame(데이터)`: DataFrame 생성 기본 구문.
      * `df = df.set_index("컬럼명")`: 인덱스 설정 후 재할당 필수\!
  * **오답이나 주의사항**:
      * `pd.DataFrame()` 함수 호출 시 괄호 `()` 사용: `pd.DataFrame[데이터]`처럼 `[]` 대괄호를 사용하면 `TypeError`가 발생합니다. 함수/클래스 호출은 반드시 `()` 소괄호를 사용해야 합니다.
      * `set_index()`의 `inplace=False` 기본값: `df.set_index("id")`만으로는 원본 DataFrame이 변경되지 않습니다. 대부분의 Pandas 메서드는 새로운 DataFrame을 반환하므로, 변경사항을 반영하려면 **재할당(`df = df.set_index(...)`)해야 함**을 잊지 마세요.

#### **2. 파일 입출력 (`pd.read_csv()` 활용)**

  * **설명**: CSV, TSV 등 외부 텍스트 파일을 Pandas DataFrame으로 불러오는 방법을 익혔습니다. 특히 파일의 인코딩, 구분자, 헤더 유무 등 다양한 `pd.read_csv()` 옵션의 중요성을 파악했습니다. `StringIO`를 활용하여 메모리에서 가상 파일을 다루는 방법도 배웠습니다.
  * **이론**:
      * **🌟🌟🌟 `pd.read_csv()`**: 외부 텍스트 파일(CSV, TSV 등)을 DataFrame으로 불러오는 가장 핵심적인 함수입니다. 데이터 분석의 시작은 대부분 이 함수로부터 이루어집니다.
          * `sep`: 데이터 **구분자** 지정 (기본값 `,`). 탭으로 구분된 파일(`\t`) 처리 시 필수.
          * `encoding`: 파일 **문자 인코딩** 지정. 한글 깨짐(`UnicodeDecodeError`) 발생 시 필수 (`'cp949'`, `'euc-kr'`, `'utf-8'` 등).
          * `header`: **컬럼명으로 사용할 행** 지정. `header=None`은 헤더가 없음을 의미.
          * `names`: `header=None`일 때 **컬럼명을 직접 지정**.
          * `index_col`: 특정 컬럼을 DataFrame의 **행 인덱스**로 지정.
          * `dtype`: 특정 컬럼의 **데이터 타입을 강제 지정**.
      * **🌟🌟 `from io import StringIO`**: 파이썬 문자열을 마치 파일처럼 `pd.read_csv()`에 전달할 수 있게 해주는 도구. 문제 풀이 테스트 시 유용합니다.
  * **암기할 사항**:
      * `df = pd.read_csv('파일경로', 옵션들)`: 파일 불러오기 기본 구문.
      * `pd.read_csv()`의 주요 옵션: `sep`, `encoding`, `header`, `names`, `index_col`, `dtype`.
      * `encoding='cp949'` (Windows 한글), `encoding='euc-kr'` (리눅스/구형 한글), `encoding='utf-8'` (글로벌 표준)
  * **오답이나 주의사항**:
      * `pd.read_csv()` 매개변수 전달 방식 및 이름 오타: `index_col`이나 `dtype`을 `pd.read_csv(...).index_col = ...`처럼 잘못된 메서드 체이닝으로 사용하거나, `header`를 `head`, `names`를 `name` 등으로 오타를 내서 `AttributeError`가 발생했던 경험이 있습니다. 매개변수는 `()` 괄호 안에 `매개변수명=값` 형태로 정확히 전달해야 합니다.
      * 데이터 원본의 미세한 공백: `csv_data = """ TransactionID,..."""`처럼 문자열 시작 부분에 공백이 있어 컬럼명이 `" TransactionID"` (공백 포함)으로 읽혀 `ValueError`가 발생했습니다. 파일(또는 문자열)의 헤더(컬럼명)에 불필요한 공백이 없는지 항상 확인하는 습관을 들이세요.

#### **3. DataFrame 기본 탐색 및 요약 통계**

  * **설명**: 데이터를 불러온 후 DataFrame의 크기, 구조, 결측치 여부, 그리고 핵심적인 통계 정보를 빠르게 파악하는 방법을 배웠습니다. 이는 데이터의 '건강 상태'를 확인하고 분석 방향을 설정하는 데 매우 중요합니다.
  * **이론**:
      * **🌟🌟🌟 `df.info()`**: DataFrame의 전반적인 요약 정보를 출력합니다. (컬럼명, Non-Null 값 개수, 데이터 타입, 메모리 사용량). 데이터 초기 탐색 시 가장 먼저 확인해야 할 **필수 메서드**입니다.
      * **🌟🌟🌟 `df.describe()`**: 숫자형 컬럼들의 기술 통계량 (평균, 표준편차, 사분위수 등)을 보여줍니다. 데이터 분포 파악에 유용합니다.
      * **🌟🌟🌟 `df['컬럼명'].value_counts()`**: 특정 컬럼(Series) 내 각 고유 값의 빈도수를 계산합니다. 범주형 데이터의 분포를 파악하는 데 필수적입니다.
      * **🌟🌟🌟 `df.isnull().sum()`**: 각 컬럼별 결측치(`NaN`)의 총 개수를 효율적으로 계산합니다. 데이터 전처리 전 결측치 현황 파악에 필수입니다.
      * **🌟🌟 `df.shape`**: DataFrame의 \*\*크기 (행, 열 개수)\*\*를 튜플 형태로 반환하는 **속성**입니다. (괄호 `()` 없음\!)
  * **암기할 사항**:
      * 크기: `df.shape`
      * 전반 정보: `df.info()`
      * 기술 통계: `df.describe()`
      * 빈도수: `df['컬럼'].value_counts()`
      * 결측치 개수: `df.isnull().sum()`
  * **오답이나 주의사항**:
      * `df['컬럼명'].value_counts()` vs `df.count()`:
          * `value_counts()`는 고유 값들의 빈도수를 세는 반면,
          * `count()`는 결측치를 제외한 유효한 값의 개수를 셉니다.
          * 두 메서드의 목적과 반환하는 값이 다르니 혼동하지 않도록 주의하세요. 오타(`count` vs `counts`)로 인해 `AttributeError`가 발생할 수 있습니다.
      * `df.isnull().sum()`에서 `sum()`의 의미: `isnull()`의 결과인 `True`/`False` 불리언 값을 `sum()` 메서드가 1/0으로 간주하여 합계를 계산한다는 점을 이해하는 것이 중요합니다. 메서드 체이닝을 통해 간결하고 효율적으로 결측치를 집계할 수 있습니다.

-----

### **➕ 추가 질문 사항 정리**

#### **언더스코어(`_`)의 의미 및 활용:**

  * **단일 언더스코어 (`_`)**: 임시 변수, 무시하는 변수(예: `x, _, z`), 파이썬 인터프리터에서 직전 결과 값.
  * **선행 언더스코어 (`_변수명`)**: 내부 사용을 위한 약속(convention). 외부에서 직접 접근하지 않도록 권장.
  * **후행 언더스코어 (`변수명_`)**: 파이썬 예약어(keyword)와 변수명 충돌을 피하기 위해 사용.
  * **이중 선행 언더스코어 (`__변수명`)**: 이름 맹글링(Name Mangling)을 통한 강제적인 이름 충돌 방지 (주로 클래스 상속 시).
  * `index_col`, `read_csv`에서의 언더스코어: `index_col`, `read_csv` 등 Pandas 함수 및 매개변수 이름에서 언더스코어를 사용하는 것은 파이썬의 표준 명명 규칙인 **snake\_case**를 따라 단어들을 연결하여 가독성을 높인 것입니다. 특별한 문법적 의미는 없습니다.

-----

### **💡 코딩 문제 (solution.py 파일에 저장)**

각 문제에 대한 코딩 모범 답안은 `solution.py` 파일에 별도로 작성해 주세요.

#### **문제 1: 인덱스 초기화 및 특정 컬럼 유지 (난이도: 중)**

  * **목표**: `reset_index()` 사용 시 기존 인덱스를 일반 컬럼으로 유지하는 방법을 연습합니다.
  * **가이드**:
    1.  아래 `data` 문자열을 `StringIO`와 `pd.read_csv()`를 활용하여 `df_sales` DataFrame을 생성하세요. 이때, `'OrderDate'` 컬럼을 인덱스로 지정하세요.
    2.  `df_sales`의 인덱스를 **기본 `RangeIndex`로 초기화**하세요. 이때, 기존 인덱스였던 `'OrderDate'` 컬럼은 일반 컬럼으로 **유지**되어야 합니다.
    3.  변경 후의 DataFrame을 `df_reset_sales`에 저장하고, `df_reset_sales`의 **정보(info)를 출력**하여 `'OrderDate'` 컬럼이 일반 컬럼으로 잘 유지되었는지 확인하세요.
    4.  `df_reset_sales`의 **상위 3개 행을 출력**하세요.




-----

#### **문제 2: 인덱스 다중 설정 (난이도: 상)**

  * **목표**: 여러 컬럼을 동시에 인덱스로 설정하는 방법을 연습하고, 이때 컬럼들이 DataFrame에서 제거되는지 확인합니다.
  * **가이드**:
    1.  아래 `data` 문자열을 `StringIO`와 `pd.read_csv()`를 활용하여 `df_grades` DataFrame을 생성하세요.
    2.  `'StudentID'`와 `'Subject'` 컬럼을 **동시에 인덱스로 설정**하세요. 이때, 원본 `df_grades`를 직접 수정하세요.
    3.  `df_grades`의 **정보(info)를 출력**하여 인덱스가 올바르게 설정되었고, 원본 컬럼들이 제거되었는지 확인하세요.
    4.  `df_grades`의 **인덱스 자체를 출력**하세요.

<!-- end list -->

```csv
StudentID,Subject,Score
S001,Math,90
S001,Science,85
S002,Math,78
S002,English,92
S003,Science,88
```

-----

#### **문제 3: 불완전한 데이터로 DataFrame 생성 (난이도: 중)**

  * **목표**: 행 기준 딕셔너리 리스트 방식의 유연성과 `NaN` 처리 특성을 이해합니다.
  * **가이드**:
    1.  아래 `data_list`를 사용하여 `df_flexible` DataFrame을 생성하세요.
    2.  `df_flexible`의 **정보(info)를 출력**하여 각 컬럼의 `Non-Null Count`와 `Dtype`을 확인하세요. 특히 누락된 데이터가 어떻게 처리되는지 주목하세요.
    3.  `df_flexible`의 **모든 행을 출력**하세요.

<!-- end list -->

```python
data_list = [
    {'Product': 'Laptop', 'Price': 1200, 'Weight_kg': 2.5},
    {'Product': 'Mouse', 'Price': 25, 'Manufacturer': 'Logitech'}, # Weight_kg 누락, Manufacturer 추가
    {'Product': 'Keyboard', 'Weight_kg': 1.0, 'Layout': 'US'}, # Price 누락, Layout 추가
    {'Product': 'Monitor'} # Price, Weight_kg, Manufacturer, Layout 모두 누락
]
```

-----

### **➕ 추가 학습 (further\_study.py 파일에 저장)**

이 섹션은 더 깊은 이해를 위해 스스로 탐구하고 코드를 작성해 볼 수 있는 주제들입니다.

```python
# further_study.py

# --- 인덱스와 컬럼 조작의 다양한 조합 탐구 ---
# 1. set_index()와 reset_index()의 모든 파라미터 조합 (inplace=True/False, drop=True/False)을 직접 코딩하여
#    DataFrame의 원본 변경 여부와 컬럼 유지/삭제 여부를 명확히 이해하기.
#    각 조합별로 df.info()와 df.index, df.columns를 출력하여 변화를 관찰할 것.

# 2. pd.read_csv()의 추가적인 중요 파라미터 탐구:
#    - header: 헤더가 없는 CSV 파일 처리
#    - names: 컬럼 이름 직접 지정
#    - usecols: 특정 컬럼만 불러오기
#    - na_values: 특정 문자열을 NaN으로 인식하게 하기

# --- DataFrame의 인덱스 객체 (Index, MultiIndex) 심층 이해 ---
# 1. 단일 인덱스와 MultiIndex(다중 인덱스)의 구조 비교.
# 2. df.index 속성의 다양한 활용: name, dtype, values 속성 접근.
# 3. 인덱스 기반으로 DataFrame의 특정 행을 선택하는 방법 (예: loc, iloc 사용 예시)

# --- Pandas 데이터 타입(Dtype) 심화 ---
# 1. object, int64, float64 외에 자주 사용되는 Dtype (예: datetime64, bool, category) 알아보기.
# 2. DataFrame 생성 시와 불러올 때 Dtype을 명시적으로 지정하는 방법 (dtype 파라미터) 복습.
# 3. df.astype() 메서드를 사용하여 컬럼의 Dtype을 변경하는 방법 학습.
```

-----

이제 이 종합적인 `README.md` 구조를 바탕으로 GitHub에 Day 3 학습 내용을 체계적으로 기록해 나갈 수 있습니다.

**문제 1**부터 코드를 작성해 볼 준비가 되셨을까요?
