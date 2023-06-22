class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacencyList = defaultdict(list)
        dependencies = defaultdict(int)

        for pre, las in prerequisites:
            adjacencyList[las].append(pre)
            dependencies[pre] += 1
        
        queue= deque([])

        for i in range(numCourses):
            if i not in dependencies:
                queue.append(i)
        
        res = []

        while queue:
            course = queue.popleft()
            res.append(course)
            for neigh in adjacencyList[course]:
                dependencies[neigh] -= 1
                if dependencies[neigh] == 0:
                    queue.append(neigh)

        return res if len(res) == numCourses else []



