class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = (right - left) * min(height[left],height[right])
        while left <= right:
            if height[left] < height[right]:
                left +=1
                val = (right - left) * min(height[left],height[right])
                area = max(val, area)
            else:
                right -=1
                val = (right - left) * min(height[left],height[right])
                area = max(val, area)                
        return area