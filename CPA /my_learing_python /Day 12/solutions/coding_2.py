import requests
from bs4 import BeautifulSoup

# --------------------------------------------------------------------------------
# 문제 2: 네이버 블로그 스크래핑 (심화)
# --------------------------------------------------------------------------------

# [내가 최초 제공한 코딩]
blog_url = 'https://blog.naver.com/xvmon2'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

try:
    response = requests.get(blog_url, headers=headers)
    response.raise_for_status() 
except requests.exceptions.RequestException as e:
    print(f"Error accessing the main blog page: {e}")
    exit()

main_soup = BeautifulSoup(response.text, 'html.parser')

iframe_tag = main_soup.find('iframe', id='mainFrame')
if not iframe_tag:
    print("Error: Could not find the iframe tag with id='mainFrame'")
    exit()

iframe_src = 'https://blog.naver.com' + iframe_tag.get('src')
print(f"iframe URL: {iframe_src}")

try:
    iframe_response = requests.get(iframe_src, headers=headers)
    iframe_response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error accessing the iframe page: {e}")
    exit()

iframe_soup = BeautifulSoup(iframe_response.text, 'html.parser')

posts = []
post_titles = iframe_soup.find_all('a', class_='pcol2')

for post_title_tag in post_titles:
    title = post_title_tag.get_text(strip=True)
    url = 'https://blog.naver.com' + post_title_tag.get('href')
    
    posts.append({
        'title': title,
        'url': url
    })

print("\n--- 문제 2: 네이버 블로그 스크래핑 결과 ---")
if posts:
    for post in posts:
        print(post)
else:
    print("스크래핑할 글을 찾지 못했습니다.")


# [피드백 및 모범 답안]
# - **매우 훌륭한 코드입니다!** 네이버 블로그의 iframe 구조를 정확히 파악하고, 두 번의 'requests.get()' 요청을 통해 데이터를 성공적으로 가져왔습니다.
# - **오류 처리:** 'try-except'와 'raise_for_status()'를 사용하여 네트워크 오류를 견고하게 처리한 점이 특히 인상적입니다. 실전 스크래핑에서 매우 중요한 기술입니다.
# - **HTTP 헤더:** 'User-Agent' 헤더를 추가하여 서버로부터 차단당할 가능성을 낮춘 점도 모범적입니다.
# - **데이터 추출:** 'find_all()'과 `.get()`을 사용하여 제목과 URL을 정확하게 추출하고, 딕셔너리 리스트로 깔끔하게 정리했습니다.

# [추가 학습]
# - **CSS 선택자 활용:** 'find'와 'find_all' 대신 '.select()' 메서드를 사용하면 CSS 선택자로 데이터를 더 유연하게 추출할 수 있습니다.
#   - 예: 'post_titles = iframe_soup.select('a.pcol2')'
# - **URL 완성:** 'requests.get()'을 호출할 때 'urljoin' 함수를 사용하면 URL을 더 안전하게 합칠 수 있습니다.
#   - 예: 'from urllib.parse import urljoin', 'full_url = urljoin(iframe_src, post_title_tag.get('href'))'
