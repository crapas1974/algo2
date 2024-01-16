def moving_count(n):
    if n == 1:
        return 1
    return 2 * moving_count(n - 1) + 1

def moving_guide(src, dest, room, n):
    if n == 0:
        return
    moving_guide(src, room, dest, n - 1)
    print(f"    {src} -> {dest}")
    moving_guide(room, dest, src, n - 1)

import random 

def main():
    testcases = [3, 4, 5, 10, 100]
    for tc in testcases:
        print(f"{tc}개의 바이오 필터를 다른 실험판으로 옮길 때의 최소 이동 회수 : {moving_count(tc)}")

    testcases = [3, 4, 5]
    for tc in testcases:
        print(f"{tc}개의 바이오 필터를 p1 실험판에서 p2 실험판으로 옮기는 과정")
        moving_guide('p1', 'p2', 'p3', tc)
        print()

if __name__ == '__main__':
    main()