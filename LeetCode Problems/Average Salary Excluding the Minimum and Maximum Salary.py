class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop()
        salary=salary[1:]
        return sum(salary)/len(salary)