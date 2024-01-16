def pretty_edit(text, max_width):
   # 텍스트를 단어의 리스트로 변환
   words = text.split()
   n = len(words)
  
   # i번째 단어부터 j번째 단어까지 한 줄에 배치할 때의 남은 여백의 제곱 : less[i - 1][j - 1]
   # 만약 줄 제한을 넘어간다면, 충분히 큰 값 (float('inf'))으로 설정
   less = [[0 for _ in range(n)] for _ in range(n)]
   # 1단계 - i 번째 단어에서 j 번째 단어까지 한 줄에 배치할 때의 길이
   for i in range(n):
       less[i][i] = len(words[i])
       for j in range(i + 1, n):
           less[i][j] = less[i][j - 1] + len(words[j]) + 1 # '1'은 단어 사이 공백
   # 2단계 - i 번째 단어에서 j 번째 단어까지 한 줄에 배치할 때의 남은 여백의 제곱
   # 줄을 넘어가는 경우 충분히 큰 값으로 초기화 한다.
   for i in range(n):
       for j in range(i, n):
           if less[i][j] >= max_width:
               less[i][j] = float('inf')
           else:
               less[i][j] = (max_width - less[i][j]) ** 2

   # i 번째 단어까지 문제의 조건에 맞게 배치했을 때 최소가 되는 여백의 제곱 합
   # min_lesss[0] 은 0으로 초기화하고, 나머지 값은 충분히 큰 값 (float('inf'))으로 초기화
   min_lesss = [0] + [float('inf')] * n
   result = [-1] * n
   for j in range(1, n + 1):
       for i in range(1, j + 1):
           # 작은 문제가 float('inf')이면 계산하지 않는다.
           # i 번째 단어부터 j 번째 단어까지 한 줄에 배치할 수 없으면 계산하지 않는다.
           if min_lesss[i - 1] != float('inf') and less[i - 1][j - 1] != float('inf'):
               # min_lesss[j - 1] + less[i - 1][j - 1] 중 최소의 값이
               # min_lesss[j]의 값이 된다.
               if min_lesss[i - 1] + less[i - 1][j - 1] < min_lesss[j]:
                   min_lesss[j] = min_lesss[i - 1] + less[i - 1][j - 1]
                   result[j - 1] = i - 1

   # 결과 추적
   lines = []
   j = n
   while j > 0:
       i = result[j - 1]
       lines.append(' '.join(words[i:j]))
       j = i
   if min_lesss[n] == float('inf'):
       return -1, None
  
   return min_lesss[n], list(reversed(lines))


def pretty_edit_space(text, max_width):
   # 텍스트를 단어의 리스트로 변환
   words = text.split()
   n = len(words)
  
   # i번째 단어부터 j번째 단어까지 한 줄에 배치할 때의 남은 여백의 제곱 : less[i - 1][j - 1]
   # 만약 줄 제한을 넘어간다면, 충분히 큰 값 (float('inf'))으로 설정
   less = [[0 for _ in range(n)] for _ in range(n)]
   # 1단계 - i 번째 단어에서 j 번째 단어까지 한 줄에 배치할 때의 길이
   for i in range(n):
       less[i][i] = len(words[i])
       for j in range(i + 1, n):
           less[i][j] = less[i][j - 1] + len(words[j]) + 1 # '1'은 단어 사이 공백
   # 2단계 - i 번째 단어에서 j 번째 단어까지 한 줄에 배치할 때의 남은 여백의 제곱
   # 줄을 넘어가는 경우 충분히 큰 값으로 초기화 한다.
   for i in range(n):
       for j in range(i, n):
           if less[i][j] >= max_width:
               less[i][j] = float('inf')
           else:
               less[i][j] = (max_width - less[i][j]) ** 2
   # i 번째 단어까지 문제의 조건에 맞게 배치했을 때 최소가 되는 여백의 제곱 합
   # min_lesss[0] 은 0으로 초기화하고, 나머지 값은 충분히 큰 값 (float('inf'))으로 초기화
   min_lesss = [0] + [float('inf')] * n

   for j in range(1, n + 1):
       for i in range(1, j + 1):
           # 작은 문제가 float('inf')이면 계산하지 않는다.
           # i 번째 단어부터 j 번째 단어까지 한 줄에 배치할 수 없으면 계산하지 않는다.
           if min_lesss[i - 1] != float('inf') and less[i - 1][j - 1] != float('inf'):
               # min_lesss[j - 1] + less[i - 1][j - 1] 중 최소의 값이
               # min_lesss[j]의 값이 된다.
               if min_lesss[i - 1] + less[i - 1][j - 1] < min_lesss[j]:
                   min_lesss[j] = min_lesss[i - 1] + less[i - 1][j - 1]
   if min_lesss[n] == float('inf'):
       return -1
   return min_lesss[n]

def main():
    testcases = [(40, "In real world, there's lots of algorithm challenges. We must solve it for every people who expect technical assist and progress."), (80, "Two roads diverged in a yellow wood, \
And sorry I could not travel both \
And be one traveler, long I stood \
And looked down one as far as I could \
To where it bent in the undergrowth; \
Then took the other, as just as fair, \
And having perhaps the better claim, \
Because it was grassy and wanted wear; \
Though as for that the passing there \
Had worn them really about the same, \
And both that morning equally lay \
In leaves no step had trodden black. \
Oh, I kept the first for another day! \
Yet knowing how way leads on to way, \
I doubted if I should ever come back. \
I shall be telling this with a sigh \
Somewhere ages and ages hence: \
Two roads diverged in a wood, and I— \
I took the one less traveled by, \
And that has made all the difference.")]

    for i, testcase in enumerate(testcases):
        min_lesss, edited_text = pretty_edit(testcase[1], testcase[0])
        print(f"TC {i + 1}:")
        print("----------")
        for line in edited_text:
            print(line)
        print("----------")

if __name__ == "__main__":
    main()