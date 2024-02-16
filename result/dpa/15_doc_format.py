def pretty_edit(text, max_width):
   words = text.split()
   n = len(words)
  
   less = [[0 for _ in range(n)] for _ in range(n)]
   for i in range(n):
       less[i][i] = len(words[i])
       for j in range(i + 1, n):
           less[i][j] = less[i][j - 1] + len(words[j]) + 1
   for i in range(n):
       for j in range(i, n):
           if less[i][j] >= max_width:
               less[i][j] = float('inf')
           else:
               less[i][j] = (max_width - less[i][j]) ** 2

   min_lesss = [0] + [float('inf')] * n
   result = [-1] * n
   for j in range(1, n + 1):
       for i in range(1, j + 1):
           if min_lesss[i - 1] != float('inf') and less[i - 1][j - 1] != float('inf'):
               if min_lesss[i - 1] + less[i - 1][j - 1] < min_lesss[j]:
                   min_lesss[j] = min_lesss[i - 1] + less[i - 1][j - 1]
                   result[j - 1] = i - 1

   lines = []
   j = n
   while j > 0:
       i = result[j - 1]
       lines.append(' '.join(words[i:j]))
       j = i
   if min_lesss[n] == float('inf'):
       return -1, None
  
   return min_lesss[n], list(reversed(lines))

def main():
    testcases = [
        (15, "Youths, Be Ambitious!"),
        (40, "In real world, there's lots of algorithm challenges. We must solve it for every people who expect technical assist and progress."), 
        (80, "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth; Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same, And both that morning equally lay In leaves no step had trodden black. Oh, I kept the first for another day! Yet knowing how way leads on to way, I doubted if I should ever come back. I shall be telling this with a sigh Somewhere ages and ages hence: Two roads diverged in a wood, and I— I took the one less traveled by, And that has made all the difference.")
    ]

    for i, testcase in enumerate(testcases):
        min_lesss, edited_text = pretty_edit(testcase[1], testcase[0])
        print(f"Testcase {i + 1}:")
        print(f"    최소 여백의 제곱 합 : {min_lesss}")
        print("----------")
        for line in edited_text:
            print(line)
        print("----------")
        print()

if __name__ == "__main__":
    main()