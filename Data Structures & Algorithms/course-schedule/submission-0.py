class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph=defaultdict(list)
        ind=defaultdict(int)
        for p in prerequisites:
            a=p[0]
            b=p[1]
            graph[b].append(a)
            ind[a]=ind.get(a,0)+1
        

        

        
        
        q=deque([c for c in range(numCourses) if ind.get(c,0)==0])
        cnt=0


        
        print(graph)
        print(ind)
        print(q)
        while q:
            node=q.popleft()
            cnt+=1
            for nei in graph[node]:
                ind[nei]=ind.get(nei)-1
                if ind[nei]==0:
                    q.append(nei)


        return cnt==numCourses
        