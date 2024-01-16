# 실험 사전 단계의 시간 복잡도

---

## 실험군 쥐의 무게의 평균과 표준편차를 구하는 작업에 대하여

- 알고리즘 (유사코드로 표현)

```
FUNCTION AVG_AND_STD(n mouses)
    sum <- 0
    square_sum <- 0
    FOR i FROM 1 TO n
        mouse_weight <- weigh(i)  # i번째 쥐의 무게를 측정한 값
        sum <- sum + mouse_weight
        square_sum <- square_sum + mouse_weight * mouse_weight
    average <- sum / n
    standard_dev <- root(square_sum - sum * sum)    # root : square root
    RETURN average, standard_dev
```

- 알고리즘의 분석
  - 실험군에 속한 쥐가 $n$마리일 때 저울에 올리는 횟수는 $n$번이다.
  - 알고리즘은 1개의 루프를 사용해 루프 내에서 무게를 측정하고 무게의 합, 무게의 제곱의 합을 구한다.
  - 쥐 한마리의 무게를 측정하는 시간만 고려한다면, 이 알고리즘을 수행하는데 걸리는 시간은 $t_1n$이다.
  - 쥐 한마리의 무게를 측정하는 시간과 덧샘 연산의 시간만 고려한다면, 이 알고리즘을 수행하는데 걸리는 시간은 $(t_1 + 2\,t_2)n$이다.
  - 이 알고리즘의 시간 복잡도는 $\mathcal{O}(n)$이다.

## 실험군 쥐의 무게를 정규화하는 작업에 대하여

- 알고리즘 (유사코드로 표현)

```
FUNCTION NORMALIZE(n mouses)
    normalized_array <- size n array
    average, standard_dev <- AVG_AND_STD(n mouses) # 이전 알고리즘을 그대로 사용한다.
    FOR i FROM 1 TO n
        mouse_weight <- weigh(i)        # i번째 쥐의 무게를 측정한 값
        normalized_array[i] <- (mouse_weight - average) / standard_dev
    RETURN normalized_array
```

- 알고리즘의 분석

  - 알고리즘은 2개의 루프를 나란히 사용한다.
    - 첫 번째 루프에서는 실험군 쥐의 무게의 평균과 표준편차를 계산한다.
    - 두 번째 루프에서는 실험군 쥐의 무게를 구하고, 평균과 표준편차를 계산해 각각의 쥐를 정규화한다.
  - 쥐 한마리의 무게를 측정하는 시간과 쥐 한마리의 무게를 정규화 하는데 걸리는 시간만 고려한다면, 이 알고리즘을 걸리는 시간은 다음과 같다.
    - 첫 번째 루프 : $t_1n$
    - 두 번째 루프 : $(t_1 + t_3)n$
    - 루프를 나란히 사용하므로, 알고리즘의 전체 소요 시간은 $t_1 n + (t_1 + t_3) n = (2\,t_1 + t_2) n$이다.
    - 이 알고리즘의 시간 복잡도는 $\mathcal{O}(n)$이다.

## 모든 가능한 쥐의 쌍의 무게의 차를 구하는 작업에 대하여

- 알고리즘 (유사코드로 표현)

```
FUNCTION DIFF_LIST(n mouses)
    diff_weight <- empty array
    weight_array <- size n array
    FOR i FROM 1 TO n
        weight_array[i] <- weigh(i) # i번째 쥐의 무게를 측정한 값

    FOR i FROM 1 TO n
        FOR j FROM 1 TO n
            IF i = j THEN CONTINUE  # 루프의 현재 반복을 건너뛴다.
            IF weight_array[i] > weight_array[j] THEN
                APPEND (weight_array[i] - weight_array[j]) INTO diff_weight
            ELSE
                APPEND (weight_array[j] - weight_array[i]) INTO diff_weight
    RETURN diff_weight
```

- 알고리즘의 분석
  - 알고리즘은 3개의 루프를사용한다.
    - 하나는 단일 루프로, 실험군 쥐의 무게를 측정한다.
    - 나머지 둘은 중첩된 이중 루프로 실험군 쥐 두 마리의 차이를 계산한다.
  - 쥐 한 마리의 무게를 측정하는 시간과 쥐 두 마리의 무게의 차를 구하는데 필요한 시간만 고려한다면, 이 알고리즘을 수행하는데 필요한 시간은 다음과 같다.
    - 첫 번째 루프 : $t_1 n$이다.
    - 두 번째 루프 : $n$ 번의 루프 내에서 $n - 1$번의 차이를 계산하므로 필요한 시간은 $t_4 n (n - 1)$이다.
    - 그러므로 전체 작업을 완료하는데 필요한 시간은 $t_1 n + t_4 n (n - 1) = t_4 n^2 + (t_1 - t_4) n$이다.
  - $t_1 = 100$, $t_4=1$일 때의 전체 작업에 필요한 시간
    - 10마리일 때 ($n = 10$) : 1090초
    - 100마리일 때 ($n = 100$) : 19900초
    - 1000마리일 때 ($n = 1000$) : 1099000초
  - 쥐의 무게를 측정하는데 걸리는 시간
    - 10마리일 때 ($n = 10$) : 1000초
    - 100마리일 때 ($n = 100$) : 10000초
    - 1000마리일 때 ($n = 1000$) : 100000초
  - 쥐의 무게의 차를 구하는데 걸리는 시간
    - 10마리일 때 ($n = 10$) : 90초
    - 100마리일 때 ($n = 100$) : 9900초
    - 1000마리일 때 ($n = 1000$) : 999000초
  - 쥐의 개체수가 증가할 때 실행 시간에 더 크게 영향을 미치는 값은 제곱차수 항의 계수인 $t_4$이다.
  - 이 알고리즘의 시간 복잡도는 $\mathcal{O}(n^2)$이다.
