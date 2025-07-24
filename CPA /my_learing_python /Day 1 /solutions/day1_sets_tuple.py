data = (100, 200, 300)

a, b, c = data #언패킹 추가 정리하기
print("--- 튜플 언패킹 결과 ---")
print(f"변수 a: {a}")
print(f"변수 b: {b}")
print(f"변수 c: {c}") #f-string 사용 습관화하기


numbers = [1, 2, 3, 2, 1]
print(f"\n원본 리스트: {numbers}")

print("--- Set으로 중복값 제거 결과 ---")
print(set(numbers)) #set은 매서드가 아님, 최초에 numbers.set()으로 했다가 AttributeError 발생
