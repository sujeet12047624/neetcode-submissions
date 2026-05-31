class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph=defaultdict(list)
        cnt=0
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visit=set()
        def dfs(node):
            visit.add(node)
            for nei in graph[node]:
                if nei not in visit:
                    dfs(nei)
        
        for i in range(n):
            if i not in visit:
                cnt+=1
                dfs(i)
        return cnt

            



        