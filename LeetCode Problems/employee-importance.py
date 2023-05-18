"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        res = [0]
        def find(id):
            for el in employees:
                if el.id == id:
                    return el

        def dfs(node):                    
            res[0] += node.importance
            for emp in node.subordinates:
                dfs(find(emp))

        
        dfs(find(id))
        return res[0]