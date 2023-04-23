n , m = list(map(int, input().split()))


nElements = list(map(int, input().split()))
mElements = list(map(int, input().split()))


n_point = 0
m_point = 0

less_elements = []

for i, val in enumerate(mElements):
	while n_point < n and nElements[n_point] < val :
		n_point += 1
	less_elements.append(n_point)

print(' '.join(map(str,less_elements)))