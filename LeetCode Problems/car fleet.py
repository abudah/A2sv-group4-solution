class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        count_fleet = 0
        zipped = sorted(zip(position, speed), reverse = True)
        current_time = (target - zipped[0][0])/zipped[0][1]
        
        for i in range(1, len(position)):
            finish_time = (target - zipped[i][0])/zipped[i][1]
            if finish_time > current_time:
                count_fleet += 1
                current_time = finish_time
                
        count_fleet += 1
        return count_fleet