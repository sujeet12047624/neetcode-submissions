class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        graph=defaultdict(list)
        for a,b in trust:
            
            graph[a].append(b)
        
        ind={}

        out={}
        for a,b in graph.items():
            for x in b:
                ind[x]=ind.get(x,0)+1
            out[a]=len(graph[a])
        print(ind)
        print(out)


        
        print(graph)
        for i in range(1,n+1):
            if ind.get(i,0)==n-1 and out.get(i,0)==0:
                return i
        
        
        

        return -1
        