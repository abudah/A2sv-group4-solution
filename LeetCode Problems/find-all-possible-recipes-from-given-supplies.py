class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for i in range(len(recipes)):
            for el,val in enumerate(ingredients[i]):
                graph[val].append(recipes[i])
                indegree[recipes[i]] += 1
        queue = deque([])
        for i in supplies:
            queue.append(i)
        recipe = set(recipes)
        res = []
        while queue:
            node = queue.popleft()
            if node in recipe:
                res.append(node)
            for neigh in graph[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        return res