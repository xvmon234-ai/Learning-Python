from bs4 import BeautifulSoup

# --- 데이터 준비 ---
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

# --------------------------------------------------------------------------------
# 문제 1: 정적 HTML 스크래핑 (기본)
# --------------------------------------------------------------------------------

# [내가 최초 제공한 코딩]
soup = BeautifulSoup(html_doc_static, 'html.parser')

products = []

for product_div in soup.find_all('div', class_='product'):
    name = product_div.find('h2', class_='product-name').get_text(strip=True)
    price = product_div.find('p', class_='price').get_text(strip=True)

    products.append({
        'name': name,
        'price': price
    })

print("--- 문제 1: 정적 HTML 스크래핑 결과 ---")
for product in products:
    print(product)


# [피드백 및 모범 답안]
# - 문제의 요구사항을 완벽하게 충족하는 훌륭한 코드입니다.
# - 'find_all()'로 상품 목록을 가져오고, 반복문 내에서 'find()'를 사용해 각 상품의 세부 정보를 추출하는 과정이 매우 효율적이고 정확합니다.
# - '.get_text(strip=True)'를 사용하여 불필요한 공백을 제거한 점도 좋은 습관입니다.

# [추가 학습]
# - 현재 코드는 가독성이 뛰어나고 명확하지만, 파이썬의 '리스트 컴프리헨션(List Comprehension)'을 활용하면 더 간결하게 작성할 수 있습니다.
# - 예시:
#   products_concise = [
#       {
#           'name': p.find('h2', class_='product-name').get_text(strip=True),
#           'price': p.find('p', class_='price').get_text(strip=True)
#       }
#       for p in soup.find_all('div', class_='product')
#   ]
#   print(products_concise)
