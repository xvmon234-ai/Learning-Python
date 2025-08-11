# Day 12: 웹 스크래핑 기초 (Beautiful Soup & Requests)

## 🎯 학습 목표

  - **문제 1**: 정적인 HTML 구조에서 데이터를 추출하는 기본 원리를 이해합니다.
  - **문제 2**: 실제 웹사이트의 복잡한 구조(`<iframe>` 포함)를 파악하고, 데이터를 수집하는 실전 경험을 확보합니다.

### ✔️ 오늘 할 일

  - **웹페이지 구조 이해 및 Requests & Beautiful Soup 이론 (1.5시간)**
  - **실전 웹 스크래핑 (2.5시간)**: 두 개의 실습 문제를 해결하며 웹 스크래핑 실력 다지기.

-----

### 💻 이론 학습: 웹 스크래핑 핵심 개념

#### 1\. 웹페이지 구조 이해

웹 스크래핑을 하려면 웹페이지가 어떻게 구성되어 있는지 알아야 합니다. 대부분의 웹페이지는 \*\*HTML(HyperText Markup Language)\*\*로 만들어져 있으며, 다음과 같은 요소로 구성됩니다.

  - **태그 (Tag)**: `<p>`, `<h1>`, `<a>`, `<div>`와 같이 꺾쇠 괄호로 둘러싸인 요소입니다.
  - **속성 (Attribute)**: 태그에 대한 추가 정보를 제공합니다. `<a href="url">`에서 `href`가 속성입니다.
  - **클래스 (Class)**: `.product-item`, `.post-title`과 같이 여러 태그에 동일하게 적용되는 스타일이나 기능을 묶어주는 역할을 합니다.
  - **ID**: `id="mainFrame"`과 같이 특정 태그를 고유하게 식별하는 데 사용됩니다.

#### 2\. Requests 라이브러리: 웹페이지 요청 및 응답 받기

`requests`는 웹페이지의 데이터를 가져오는 가장 기본적인 도구입니다.

  - **`requests.get(URL)`**: 특정 URL에 GET 요청을 보내 웹페이지의 HTML 데이터를 가져옵니다.
  - **응답 객체**: 요청이 성공하면 응답 객체(Response Object)를 반환하며, `response.text`를 통해 HTML 내용을 문자열로 얻을 수 있습니다.

#### 3\. Beautiful Soup 라이브러리: HTML 파싱 및 데이터 추출

`Beautiful Soup`는 `requests`로 가져온 HTML을 파싱(parsing)하여 원하는 데이터를 쉽게 추출할 수 있게 도와주는 라이브러리입니다.

  - **`BeautifulSoup(html_doc, 'html.parser')`**: HTML 문자열을 파싱하여 탐색 가능한 객체로 만듭니다.
  - **`find()`, `find_all()`**: 특정 태그를 찾을 때 사용합니다. `find()`는 첫 번째 일치하는 요소를, `find_all()`은 모든 일치하는 요소를 리스트로 반환합니다.
  - **`.select()`**: CSS 선택자를 이용해 여러 요소를 한 번에 찾아올 수 있습니다. (예: `soup.select('.product-name')`은 클래스가 'product-name'인 모든 요소를 찾아줍니다.)

-----

### 📝 실습 문제 및 요구사항

#### **문제 1: 정적 HTML 스크래핑 (기본)**

아래 HTML 코드는 가상의 상품 목록을 나타냅니다. 이 문자열을 사용하여 상품 이름과 가격을 스크래핑하세요.

```python
# 파이썬 코드에서 사용할 HTML 문자열
html_doc_static = """
<html>
<body>
    <h1>오늘의 특가 상품</h1>
    <div class="product-list">
        <div class="product">
            <h2 class="product-name">노트북 거치대</h2>
            <p class="price">35,000원</p>
        </div>
        <div class="product">
            <h2 class="product-name">무선 키보드</h2>
            <p class="price">89,000원</p>
        </div>
        <div class="product">
            <h2 class="product-name">마우스 패드</h2>
            <p class="price">12,500원</p>
        </div>
    </div>
</body>
</html>
"""
```

**요구사항:**

  - `BeautifulSoup`을 사용해 `html_doc_static`에서 모든 상품의 **이름**과 **가격**을 추출하세요.
  - 추출한 데이터를 리스트 안에 딕셔너리 형태로 저장하고 출력하세요.

[**정답 코드 보러가기**](https://github.com/xvmon234-ai/Learning-Python/blob/main/CPA%20/my_learing_python%20/Day%2012/solutions/coding_1.py)

#### **문제 2: 네이버 블로그 스크래핑 (심화)**

운영 중인 블로그 `https://blog.naver.com/xvmon2`의 첫 페이지에서 모든 글의 **제목**과 **URL**을 스크래핑하세요.

**요구사항:**

  - **Requests**로 블로그 메인 주소의 HTML을 가져온 후, `iframe` 태그의 `src` 속성을 추출하세요.
  - 추출한 `src` 주소로 다시 `Requests`를 보내 실제 블로그 글 목록을 담은 HTML을 가져오세요.
  - `BeautifulSoup`으로 글 목록 HTML을 파싱하고, 모든 글의 **제목**과 **URL**을 추출하세요.
  - 결과를 리스트 안에 딕셔너리 형태로 저장하고 출력하세요.

[**정답 코드 보러가기**](https://github.com/xvmon234-ai/Learning-Python/blob/main/CPA%20/my_learing_python%20/Day%2012/solutions/coding_2.py)
