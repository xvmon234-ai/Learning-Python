# --- 나의 첫 시도 ---
# my_numbers = [10, 20, 30, 40, 50]
# def calculate_average(x, y):
#     x = sum(my_numbers)
#     y = len(my_numbers)
#     return x / y
# print(f"평균: {calculate_average}")

# --- 모범 답안 (수정된 코드) ---
def calculate_average(numbers):
    """
    숫자 리스트의 평균을 계산하고 반환하는 함수입니다.
    리스트가 비어있을 경우 0을 반환합니다.
    """
    if not numbers:
        return 0

    total = sum(numbers)
    average = total / len(numbers)
    return average

my_scores = [10, 20, 30, 40, 50]
avg1 = calculate_average(my_scores)
print(f"평균: {avg1}")

empty_list = []
avg2 = calculate_average(empty_list)
print(f"빈 리스트의 평균: {avg2}")
# 함수 호출 예시:
my_scores = [10, 20, 30, 40, 50] # 함수에 전달할 실제 '인수' 리스트
avg1 = calculate_average(my_scores) # 함수를 호출하고 반환값을 변수에 저장
print(f"평균: {avg1}")

empty_list = []
avg2 = calculate_average(empty_list) # 비어있는 리스트로 함수 호출
print(f"빈 리스트의 평균: {avg2}")


"""
[학습 기록 - 나의 첫 시도 피드백]

- 학습 질문:
  - 함수를 정의할 때 매개변수 `(x, y)`를 선언했는데, 함수 내부에서 이 매개변수를 사용하지 않고 외부 변수 `my_numbers`에 직접 의존하는 것이 올바른 방법인지 헷갈렸음.
  - `print(f"평균: {calculate_average}")`처럼 함수 이름을 직접 출력했을 때 왜 평균 값이 나오지 않고 함수 객체 정보가 출력되는지 이해하기 어려웠음.
  - 빈 리스트가 들어왔을 때 발생할 수 있는 오류(ZeroDivisionError)에 대한 고려를 하지 못했음.

- 문제 해결:
  - **매개변수 사용의 중요성**: 함수는 외부의 특정 변수에 직접 의존하기보다, **매개변수를 통해 필요한 데이터를 전달받아 처리**하는 것이 재사용성과 독립성을 높이는 좋은 설계 원칙임을 이해했음. 따라서 `def calculate_average(numbers):`처럼 하나의 리스트 매개변수를 사용하는 것이 적절했음.
  - **함수 호출 및 반환값**: 함수를 실행하고 그 결과를 얻으려면 반드시 `calculate_average(인수)`와 같이 **괄호를 붙여 호출**해야 함을 깨달았음. 또한, 함수가 반환하는 값은 변수에 저장하여 활용해야 함. `print(f"평균: {calculate_average(my_numbers)}")` 와 같이 호출해야 함.
  - **빈 리스트 예외 처리**: `len()`으로 나눌 때 분모가 0이 되는 상황(`ZeroDivisionError`)을 방지하기 위해, `if not numbers: return 0`과 같은 **조건문을 추가하여 예외 처리**해야 함을 학습했음.

- 추가 학습:
  - **함수의 독립성과 재사용성 (Further Study 필요)**:
    함수가 외부 변수에 의존하지 않고 매개변수를 통해 데이터를 받는 것이 왜 중요한지 심화 학습이 필요함.
  - **함수 호출 방법 및 반환값 활용 (Further Study 필요)**:
    `함수이름()`으로 호출하고, `return`된 값을 변수에 저장하거나 다른 연산에 사용하는 방식에 대한 명확한 이해가 필요함.
"""
