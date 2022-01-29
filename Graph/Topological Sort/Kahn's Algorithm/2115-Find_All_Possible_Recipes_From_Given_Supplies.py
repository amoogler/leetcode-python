class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        recipes_set = set(recipes)
        res = []

        for ingredient, recipe in zip(ingredients, recipes):
            for item in ingredient:
                graph[item].append(recipe)
                indegree[recipe] += 1

        queue = deque(supplies)

        while queue:
            item = queue.popleft()

            if item in recipes_set:
                res.append(item)

            for v in graph[item]:
                indegree[v] -= 1

                if indegree[v] == 0:
                    queue.append(v)

        return res
