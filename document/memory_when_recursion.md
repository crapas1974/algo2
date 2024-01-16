# 재귀 함수와 메모리 사용

---

## 예제 1 코드의 분석

```python
def pre_order(node):
    if node == None:
        return
    print(node.data, end = '')
    pre_order(node.left)
    pre_order(node.right)

def pre_order_ver2(node):
    if node == None:
        return
    print(node.data, end = '')
    if node.left != None:
        pre_order_ver2(node.left)
    if node.right != None:
        pre_order_ver2(node.right)
```

- 주어진 그림의 트리를 탐색할 때, `pre_order` 함수의 호출 회수
  - `pre_order` 함수의 경우 모든 노드 당 두 번씩 재귀 호출을 실행한다. 노드가 총 10개 이므로 재귀 호출은 20번 수행되며, `root` 노드에 대한 1회의 호출까지 총 21번 호출된다.
- 주어진 그림의 트리를 탐색할 때, `pre_order_ver2` 함수의 호출 회수
  - `pre_order_ver2` 함수의 경우 `None` check를 한 후에 재귀 호출을 하기 때문에 실제로 자식 노드가 있는 경우에만 재귀 호출을 한다. 루트를 재외한 다른 모든 노드는 누군가의 자식 노드이며, 그러므로 재귀 호출은 9번 수행되며, `root` 노드에 대한 1회의 호출까지 총 10번 호출된다.

# 스택 메모리와 힙 메모리

- 스택 메모리란?
  - 함수가 호출될 때 함수에 포함된 지역 변수, 매개 변수, 반환 주소값 등이 저장된 스택 프레임이 생성된다. 이 스택 프레임이 위치하는 메모리가 스택 메모리이다.
  - 함수가 종료되면 스택 프레임은 스택 메모리에서 지워진다.
- 힙 메모리란?
  - 힙 메모리는 동적 메모리 할당을 위한 영역이다.
  - 객체가 동적으로 생성되면, 힙 메모리 영역에 객체의 공간이 만들어지고, 이 주소를 사용해 프로그램이 객체에 접근한다.
- 파이썬에서 스택 메모리와 힙 메모리에 저장되는 것
  - 파이썬에서 스택 메모리는 다음의 것들이 저장된다.
    - 함수의 지역 변수와 매개 변수
    - 함수가 종료될 때의 반환 주소
    - 기타 함수 호출과 관련된 정보
  - 파이썬에서 힙 메모리에는 다음의 것들이 저장된다.
    - 동적으로 할당되는 객체
    - 전역 변수
- 파이썬에서 함수가 호출될 때 호출 회수와 비례해 추가로 사용되는 메모리는 스택 메모리 영역이다.
- 재귀 호출을 과도하게 사용하는 경우, 스택 메모리를 이에 비례해서 과도하게 사용하는 문제가 발생한다.

## 예제 2 코드의 분석

```python
def factorial(n):
    result = 1
    for i in range(n):
        result *= (i + 1)
    return result
```

- 공간 복잡도는 $\mathcal O(1)$이다.
- 재귀 호출을 사용해 동일한 결과를 출력하는 함수는 다음과 같다.

```python
def factorial_recursive(n):
    if n < 1:
        return None
    if n == 1:
        return 1
    return n * factorial(n - 1)
```

- 재귀 호출로 구현하는 경우 알고리즘 자체의 공간 복잡도는 $\mathcal O(1)$이다.
- 하지만 재귀 호출 만큼 스택 메모리를 사용하게 되므로 실질적인 공간 복잡도는 $\mathcal O(n)$이다.
