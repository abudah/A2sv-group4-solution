tc = int(input())

for i in range(tc):
    f, s = list(map(int, input().split()))
    left = 0
    right = min(f, s)

    while left <= right:
        mid = (left + right)//2

        if mid <= (f+s)//4:
            left = mid + 1
        else:
            right = mid - 1
    print(right)
