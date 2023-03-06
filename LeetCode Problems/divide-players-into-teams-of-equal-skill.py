class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left=0
        right=len(skill)-1
        chem=0
        teamChem=sum([skill[0],skill[-1]])
        while left<right:
            if sum((skill[left],skill[right]))!=teamChem:
                return -1
            chem+=skill[left]*skill[right]
            left+=1
            right-=1
        return chem
        