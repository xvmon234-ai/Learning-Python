numbers = [1, 2, 3, 4, 5]

print("--- for 루프: 짝수만 출력 ---")
for num in numbers:
    if num % 2 == 0: #처음 풀 때 해당 부분에 : 를 찍지 않아서 오류 발생
        print(f"{num}")
