class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for el, pre in prerequisites:
            graph[pre].append(el)
            indegree[el] += 1
        queue = deque([])

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        res = 0
        while queue:
            course = queue.popleft()
            res += 1
            for neigh in graph[course]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        return numCourses == res     