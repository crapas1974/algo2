def hanoi(n):
    if n == 1:
        return 1
    return 2 * hanoi(n - 1) + 1

# src - 원판이 있는 기둥의 이름 
# dest - 원판을 옮길 기둥의 이름 
# room - 나머지 기둥의 이름 
# n - 옮기고자 하는 기둥의 개수
def move_hanoi(src, dest, room, n):
    if n == 0:
        return
    move_hanoi(src, room, dest, n - 1)
    print(f"{n}번 원반을 {src}에서 {dest}(으)로 옮깁니다.")
    move_hanoi(room, dest, src, n - 1)

def main():
    num_of_disk = 5
    print(f"{num_of_disk}개의 원판으로 구성된 하노이의 탑을 옮길 때의 최소 이동 횟수 : {hanoi(5)}")
    print(f"{num_of_disk}개의 원판으로 구성된 하노이의 탑을 옮기는 과정")
    move_hanoi('T1', 'T2', 'T3', 5)

if __name__ == '__main__':
    main()