class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        newNums=[]
        evens=[j for j in nums if j%2==0]
        evenNums=sum(evens)
        for i in queries:
            if nums[i[1]]%2==0:
                evenNums-=nums[i[1]]
            nums[i[1]]=nums[i[1]]+i[0]
            if nums[i[1]]%2==0:
                evenNums+=nums[i[1]]
            newNums.append(evenNums)
        return newNums