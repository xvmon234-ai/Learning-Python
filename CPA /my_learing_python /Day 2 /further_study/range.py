# --- Day 2: 반복문 - range() 함수의 정확한 범위 이해 ---
"""
[주제]
range() 함수의 'stop' 값은 항상 미만(exclusive)이다.

[개념 설명]
파이썬의 내장 함수 `range()`는 숫자의 시퀀스를 생성할 때 사용됩니다.
이 함수는 세 가지 형태로 사용될 수 있으며, 각 형태에서 'stop' 값은 생성되는 시퀀스에 **포함되지 않습니다.**

1.  `range(stop)`:
    0부터 `stop-1`까지의 정수를 생성합니다.
    예: `range(5)` -> 0, 1, 2, 3, 4

2.  `range(start, stop)`:
    `start`부터 `stop-1`까지의 정수를 생성합니다.
    예: `range(1, 5)` -> 1, 2, 3, 4

3.  `range(start, stop, step)`:
    `start`부터 `stop-1`까지 `step` 간격으로 정수를 생성합니다.
    예: `range(1, 10, 2)` -> 1, 3, 5, 7, 9

[활용 팁]
반복문을 통해 특정 범위의 숫자를 다룰 때, 'stop' 값을 항상 **'원하는 마지막 숫자 + 1'**로 설정해야 원하는 모든 숫자를 포함할 수 있습니다.
예: 1부터 10까지 포함하려면 `range(1, 11)` 사용.
"""
# # 예시 코드 (실제로 실행해 보며 이해)
# print("range(5):", list(range(5)))
# print("range(1, 5):", list(range(1, 5)))
# print("range(1, 11):", list(range(1, 11))) # 1부터 10까지 포함
# print("range(1, 10, 2):", list(range(1, 10, 2)))
