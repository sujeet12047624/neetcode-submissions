class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent=[i for i in range(n)]
        rank=[1]*n
        
        def find(node):
            if parent[node]!=node:
                parent[node]=find(parent[node])
            return parent[node]
        
        def union(node1,node2):
            root1=find(node1)
            root2=find(node2)
            if root1!=root2:
                if rank[root1]>rank[root2]:
                    parent[root2]=root1
                elif rank[root2]>rank[root1]:
                    parent[root1]=root2
                else:
                    parent[root2]=root1
                    rank[root1]+=1
        
        for a,b in sorted(edges):
            union(a,b)
        cnt=0
        print(parent)
        return len(set(find(i) for i in range(n)))


        