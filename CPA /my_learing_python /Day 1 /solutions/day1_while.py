total_sum = 0 # 합계를 저장할 변수 초기화

print("숫자를 입력하세요 (0을 입력하면 합계 출력 후 종료):")

while True: 
    current_number = int(input("숫자 입력: "))

    if current_number == 0:
        print("0이 입력되었습니다. 프로그램을 종료합니다.")
        break
    else:
        total_sum += current_number
        print(f"현재까지의 합계: {total_sum}")

print(f"최종 합계: {total_sum}")

#자주 무한루프 발생, 연습 더 많이 해야할 거 같음
