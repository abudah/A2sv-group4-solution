from math import isqrt
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        def sieve_of_eratosthenes(left, right):
            if right <= 2:
                return []
            is_prime = [True] * (right+1)
            is_prime[0]=is_prime[1] = False
            for i in range(2, isqrt(right)+1):
                if is_prime[i]:
                    for c in range(i*i, right+1, i):
                        is_prime[c] = False
            return [i for i in range(left, right+1) if is_prime[i]]

        n =  len(sieve_of_eratosthenes(left, right))
        result = sieve_of_eratosthenes(left, right)
        
        if  n < 2: return [-1,-1]
        arr = []
        for x in range(n-1):
            arr.append([result[x],result[x+1]])
        return sorted(arr, key = lambda x: x[1]-x[0])[0]