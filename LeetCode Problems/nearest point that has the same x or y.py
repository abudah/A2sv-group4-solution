class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        validPoints=[]
        for i in points:
            if i[0]==x or i[1]==y:
                validPoints.append(i)
        if len(validPoints)==0:
            return -1
        smallest=10000
        element=-1
        for i,data in enumerate(validPoints):
            distance=abs(x-data[0])+abs(y-data[1])
            if distance<smallest:
                smallest=distance
                element=points.index(data)
        return element