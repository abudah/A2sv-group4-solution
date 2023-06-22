n, m = list(map(int, input().split()))

nums = list(map(int, input().split()))

nums.sort()

final = nums[m-1]

if n==m:
	print(nums[m-1])
elif n > m and nums[m] > nums[m-1]:
	print(nums[m-1])
elif m== 0 and n > m and nums[0] > 1:
	print(1)
else:
	print(-1)