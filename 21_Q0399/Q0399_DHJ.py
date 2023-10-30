from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for i in range(len(equations)):
            A, B = equations[i]
            value = values[i]
            graph[A][B] = value
            graph[B][A] = 1.0 / value

        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0

            queue = deque([(start, 1.0)])
            visited = set()

            while queue:
                node, result = queue.popleft()
                if node == end:
                    return result
                visited.add(node)
                for neighbor, value in graph[node].items():
                    if neighbor not in visited:
                        queue.append((neighbor, result * value))
            
            return -1.0
        
        results = []
        for query in queries:
            start, end = query
            result = bfs(start, end)
            results.append(result)
        
        return results