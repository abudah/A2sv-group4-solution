class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def backtrack(i, arr,  n):
            # if the index comes to the end or base case
            if i == n:
                if  sorted(arr) in subsets:
                    return
                subsets.append(sorted(arr[::]))
                return 
            # choosing to take the index 
            arr.append(nums[i])
            
            backtrack(i + 1, arr, n)
            arr.pop()
            # choosing not to take the index
            backtrack(i + 1, arr, n)

        backtrack(0, [], len(nums))

        return subsets
