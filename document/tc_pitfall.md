# 파이썬 시간 복잡도의 함정
---
## Q1) 리스트 컴프리헨션의 함정
- 리스트 컴프리헨션은 비록 한 줄로 작성되었다고는 하나 `for` 루프를 구성한다. 그러므로, 시간 복잡도는 $\mathcal{O}(nm)$이다.
## Q2) 리스트 슬라이싱의 함정
- 리스트 슬라이싱은 내부적으로 새로운 리스트를 만들고 모든 값을 복사하는 방식으로 동작한다.
- 모든 값을 복사하는 `[:]` 슬라이싱은 $\mathcal{O}(n)$의 시간 복잡도를 가진다.
- 절반만 복사하는 경우에도 시간은 $n$에 비례해서 증가하므로 $\mathcal{O}(n)$의 시간 복잡도를 가진다.
- 아무리 큰 값이라도 10000이라는 상수값으로 정한 이상 시간 복잡도는 $\mathcal{O}(1)$이다. 물론 $n$이 10000보다 항상 작은 경우는 실질적으로는 $\mathcal O(n)$으로 동작한다. 이건 시간 복잡도를 정의하는 이론과 현실의 차이에서 기인하는 갭으로, 어쩔 수 없는 부분이 있다.
## Q3) 배열의 함정
- 배열의 합을 구하기 위해서는 $n$에 비례한 만큼 더해야 하며, 그러므로 별도의 루프는 없지만 `sum()` 함수 자체가 1번의 루프처럼 동작한다.
- 그러므로 이 코드의 시간복잡도는 $\mathcal O(nm)$이다.
## Q4) 배열에서 함정이 아닌 것
- `sum()` 함수와 달리 `len()` 함수는 $\mathcal O(1)$ 시간 복잡도를 가진다. 이는 파이썬이 리스트의 길이를 별도로 관리하기 때문에 길이와 무관하게 길이값을 바로 사용할 수 있다.
## Q5) 문자열의 함정
- 이 파이썬 코드는 리스트 내의 각 튜플로 구성된 문자열 또는 리스트를 이어 붙인다.
- 문자열을 이어붙일 때는, 이어 붙이기 위해서는 새로운 메모리 공간을 생성하고, 해당 메모리 공간에 데이터를 모두 복사해 넣는다. 그러므로 이어 붙이는 과정에서 $\mathcal O(m)$만큼의 시간 복잡도가 필요하다. 그러므로 전체 시간복잡도는 $\mathcal O(nm)$이다.
- 리스트는 mutable 자료형이지만, 그럼에도 이어붙일 때는 문자열과 마찬가지로 동작한다. 그러므로 필요한 시간복잡도는 $\mathcal O(nm)$이다.
- 이어붙이는 것과 달리 `extend` 함수는 호출하는 리스트(`list1`)은 그대로 놔 두고 `list2`의 내용만 복사해서 붙이는 방식으로 동작한다. 그러므로 이 과정에서 리스트의 메모리를 추가로 할당하지 않으면 `list2`의 길이 만큼의 시간 복잡도로 실행된다.
## Q6) 출력의 함정
- 데이터의 출력 역시 출력하는 길이에 비례해서 실행 시간이 필요하다. 그러므로 코드의 시간 복잡도는 $\mathcal O(nm)$이다.
