total_sum = 0 # 합계를 저장할 변수 초기화

print("--- while 루프: 0을 입력하면 종료 ---")
print("숫자를 입력하세요 (0을 입력하면 합계 출력 후 종료):")

while True: # 무한 루프로 시작하여, 조건에 따라 break로 탈출
    user_input_str = input("숫자 입력: ") # 사용자로부터 문자열 입력받기
    
    # 입력받은 문자열을 정수로 변환 (예외 처리 시도)
    try:
        current_number = int(user_input_str)
    except ValueError:
        print("유효하지 않은 입력입니다. 숫자를 입력해주세요.")
        continue # 숫자가 아니면 다시 입력받도록 다음 반복으로 넘어감

    if current_number == 0:
        # 사용자가 0을 입력하면 루프 종료
        print("0이 입력되었습니다. 프로그램을 종료합니다.")
        break
    else:
        # 0이 아니면 합계에 누적
        total_sum += current_number
        print(f"현재까지의 합계: {total_sum}")

print(f"최종 합계: {total_sum}")

try-except는 이런 예상치 못한 오류(예외)를 미리 처리하여 프로그램이 안정적으로 동작하도록 돕는 중요한 문법입니다. 나중에 더 복잡한 프로그램을 만들 때는 try-except를 활용하는 것이 좋습니다.
