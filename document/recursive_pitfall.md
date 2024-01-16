# 재귀 호출의 함정

---

## Case 1

```python
def mistake1(n):
    return mistake1(n - 1) + n

# 1에서 100까지의 합을 구한다.
result = mistake1(100)
```

- 문제점
  - 종료 조건이 지정되어 있지 않다.
- 해결 방법
  - `n`이 `1`에서 종료가 될 수 있도록 종료 조건을 지정한다.
  - 수정한 코드는 다음과 같다.

```python
def correct(n):
    if n == 1:
        return 1
    return correct(n - 1) + n
```

## Case 2

```python
def repeat_100_times():
    if n > 100:
        return
    n += 1
    print(n)
    repeat_100_times()

n = 0
repeat_100_times()
```

- 문제점
  - 종료 조건의 검사 대상이 되는 `n`이 파라미터로 전달되지 않는다.
  - `n`에 종료 조건이 잘못되어 함수의 이름에서 알 수 있는 의도와는 달리 101까지 출력이 된다.
- 해결 방법
  - `n`이 종료 조건으로 사용될 수 있도록 파라미터에 추가한다.
  - 종료 조건을 수정한다.
  - 수정한 코드는 다음과 같다.

```python
def correct(n):
    if n > 99:
        return
    n += 1
    print(n)
    correct(n)

n = 0
correct(n)
```

## Case 3

```python
def count_down(number):
    print(number)
    if number < 0:
        return
    count_down(number - 1)

# count_down 10, 9, ..., 0
count_down(10)
```

- 문제점
  - 종료 조건이 잘못되어 `-1`까지 출력된다.
- 해결 방법
  - 종료 조건을 수정한다.
  - 수정한 코드는 다음과 같다.

```python
def correct_count_down(number):
    print(number)
    if number < 1:
        return
    correct_count_down(number - 1)
```

## Case 4

```python
def count_down(number):
    if number < 0:
        return
    count_down(number - 1)
    print(number)

# count_down 10, 9, ..., 0
count_down(10)
```

- 문제점
  - 재귀 호출과 출력의 위치가 잘못되어서 카운트 다운이 아닌 카운트 업이 되어버린다.
- 해결 방법
  - 순서를 바로 잡는다. 순서를 바로 잡을 때 필요한 경우 재귀 호출의 종료 조건도 수정한다.
  - 수정한 코드는 케이스 3의 수정과 같다.

## Case 5

```python
# 뺄셈 만으로 나누기를 구현하는 함수
def divide(a, b, count = 0):
    if b == 0:
        raise ValueError("Connot divide by zero")
    # 나누어 떨어질 때
    if a == 0:
        return count
    # 더 이상 뺄 수 없을 때
    if a < b:
        return count, a # 몫과 나머지
    return divide(a - b, b, count + 1)
```

- 문제점
  - 이 함수는 몫과 나머지를 반환해야 하는데, 나누어 떨어질 때의 종료 조건에서 나머지를 반환하고 있지 않다. 그러므로 나누어 떨어질 때 예외가 발생한다.
- 해결 방법
  - 나누어 떨어질 때의 종료 조건에 나머지(0)를 반환하도록 수정한다.
  - 수정한 코드는 다음과 같다.

```python
# 뺄셈 만으로 나누기를 구현하는 함수
def correct_divide(a, b, count = 0):
    if b == 0:
        raise ValueError("Connot divide by zero")
    # 나누어 떨어질 때
    if a == 0:
        return count, 0
    # 더 이상 뺄 수 없을 때
    if a < b:
        return count, a # 몫과 나머지
    return correct_divide(a - b, b, count + 1)
```

## Case 6

```python
# 지수승을 계산하는 함수
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(exponent, base - 1)

```

- 문제점
  - 재귀 호출 시에 파라미터의 순서가 잘못되었다.
- 해결 방법
  - 재귀 호출의 파라미터를 바로 잡는다.
  - 수정한 코드는 다음과 같다.

```python
# 지수승을 계산하는 함수
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

```
