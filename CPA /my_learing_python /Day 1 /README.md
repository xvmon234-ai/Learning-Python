# **Day 1: 파이썬 기본기 학습 기록 (변수, 자료형, 반복문)**

### **✅ 학습 목표**

  * 파이썬의 핵심 자료형인 \*\*리스트(List)\*\*와 \*\*딕셔너리(Dictionary)\*\*의 주요 메서드 및 특징을 완벽히 이해합니다.
  * 데이터 처리의 기본인 **`for`와 `while` 반복문**을 능숙하게 활용하여 기본적인 제어 흐름을 구현합니다.
  * 튜플과 집합의 개념을 이해하고, 각 자료형이 필요한 상황을 식별합니다.

-----

### **1. 변수와 기본 자료형**

#### **핵심 이론**

파이썬의 기본 데이터 타입인 정수(`int`), 실수(`float`), 문자열(`str`), 불린(`bool`)의 개념을 복습하고, `변수명 = 값` 형태로 변수를 선언하는 방법을 익힙니다.

#### **예제 코딩**

```python
# 변수 선언 및 기본 자료형 예제
my_integer = 100
my_float = 3.14
my_string = "Hello, Python!"
my_boolean = True

print(f"정수: {my_integer}, 타입: {type(my_integer)}")
print(f"실수: {my_float}, 타입: {type(my_float)}")
print(f"문자열: {my_string}, 타입: {type(my_string)}")
print(f"불린: {my_boolean}, 타입: {type(my_boolean)}")
```

#### **연습 문제**

  * **문제:** 두 개의 정수 변수를 선언하고, 합을 계산하여 출력하세요.

문제 요구사항
1. num1이라는 변수에 10을, num2라는 변수에 20을 할당하세요.
2. result라는 변수에 num1과 num2의 합을 할당하세요.
3. f"10 + 20 = 30" 형식으로 결과를 출력하세요.

[정답](./solutions/variables)
-----

### **2. 핵심 자료형 1 - 리스트 (List)**

#### **핵심 이론**

리스트는 여러 값을 **순서대로** 저장하는 \*\*변경 가능(mutable)\*\*한 컬렉션입니다. 데이터의 추가, 삭제, 수정이 자유롭습니다.

#### **예제 코딩**

```python
# 리스트 생성 및 조작 예제
fruits = ["사과", "바나나", "체리"]

# 1) 접근 및 슬라이싱
print(f"두 번째 요소: {fruits[1]}")
print(f"1번 인덱스부터 끝까지: {fruits[1:]}")

# 2) 요소 추가 및 삭제
fruits.append("딸기") # 리스트 끝에 추가
fruits.remove("사과") # 값으로 삭제
del fruits[0]        # 인덱스로 삭제

print(f"변경된 리스트: {fruits}")

# 3) 길이 및 정렬
numbers = [3, 1, 4, 2]
numbers.sort() # 원본 리스트를 정렬
print(f"정렬된 숫자 리스트: {numbers}")
```

#### **체득을 위한 연습 문제**

  * **문제:** `scores = [85, 92, 78, 90]` 리스트에 `65`를 추가하고, 92점은 삭제한 후, 리스트를 오름차순으로 정렬하세요.

-----

### **3. 핵심 자료형 2 - 딕셔너리 (Dictionary)**

#### **핵심 이론**

딕셔너리는 \*\*키(key)\*\*와 \*\*값(value)\*\*의 쌍으로 데이터를 저장하는 컬렉션입니다. 데이터를 고유한 키를 통해 빠르게 찾아 접근할 수 있습니다.

#### **예제 코딩**

```python
# 딕셔너리 생성 및 조작 예제
student = {
    "name": "김민준",
    "student_id": "2023-1234",
    "major": "경영학",
    "gpa": 4.15
}

# 1) 값 접근
print(f"학생 이름: {student['name']}")
print(f"GPA: {student.get('gpa')}") # .get()은 키가 없을 때 오류 방지

# 2) 값 추가 및 수정
student["major"] = "회계학"
student["email"] = "minjun.kim@example.com"
print(f"수정 및 추가 후: {student}")

# 3) 키, 값, 아이템 얻기
print(f"모든 키: {student.keys()}")
print(f"모든 값: {student.values()}")
```

#### **체득을 위한 연습 문제**

  * **문제:** `product = {'name': '컴퓨터', 'price': 1200000}` 딕셔너리에 `'재고': 100` 키-값 쌍을 추가하고, 가격을 `1150000`으로 수정한 후, `for` 루프를 사용해 모든 키와 값을 출력하세요.

-----

### **4. 튜플(Tuple)과 집합(Set)**

#### **핵심 이론**

  * **튜플:** 리스트와 유사하지만, 한 번 생성되면 변경할 수 없는 **불변(immutable)** 자료형입니다. 주로 `()`를 사용합니다.
  * **집합:** **중복을 허용하지 않는** 컬렉션입니다. 데이터의 중복을 제거하거나, 합집합/교집합 등 집합 연산에 유용합니다.

#### **예제 코딩**

```python
# 튜플 언패킹 예제
coordinates = (10, 20)
x, y = coordinates # 언패킹
print(f"x 좌표: {x}, y 좌표: {y}")

# 집합으로 중복 제거 및 연산 예제
numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers_with_duplicates)
print(f"중복 제거된 숫자들: {unique_numbers}")

set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(f"합집합: {set_a.union(set_b)}") # 또는 set_a | set_b
```

#### **체득을 위한 연습 문제**

  * **문제:** `data = (100, 200, 300)` 튜플을 `a, b, c` 변수에 언패킹하고, `[1, 2, 3, 2, 1]` 리스트의 중복을 제거한 결과를 출력하세요.

-----

### **5. 제어문 - `for` & `while` 반복문**

#### **핵심 이론**

  * **`for` 루프:** 리스트와 같은 컬렉션의 모든 요소를 순회하며 코드를 실행합니다.
  * **`while` 루프:** 조건이 `True`인 동안 반복하며, 무한 루프에 빠지지 않도록 루프 내에서 조건을 변경해야 합니다.

#### **예제 코딩**

```python
# for 반복문 예제 (리스트 순회)
scores = [85, 92, 78]
total_score = 0
for score in scores:
    total_score += score
print(f"총점: {total_score}")

# while 반복문 예제 (조건 기반 반복)
count = 3
while count > 0:
    print(f"{count}...")
    count -= 1
print("발사!")
```

#### **체득을 위한 연습 문제**

  * **문제:** `numbers = [1, 2, 3, 4, 5]` 리스트를 `for` 루프로 순회하며 짝수일 때만 해당 숫자를 출력하세요.
  * **문제:** 사용자로부터 숫자를 계속 입력받아 합계를 구하다가 `0`을 입력하면 종료하는 `while` 루프를 작성하세요.

-----
