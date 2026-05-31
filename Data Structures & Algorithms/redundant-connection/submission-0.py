class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent=[i for i in range(len(edges)+1)]
        rank=[1]*(len(edges)+1)

        def find(node):
            if parent[node]!=node:
                parent[node]=find(parent[node])
            return parent[node]
        
        def union(node1,node2):
            root1=find(node1)
            root2=find(node2)
            if root1==root2:
                return True
            if root1 !=root2:
                if rank[root1]>rank[root2]:
                    parent[root2]=root1
                elif rank[root2]>rank[root1]:
                    parent[root1]=root2
                else:
                    parent[root2]=root1
                    rank[root1]+=1
            return False
        for a,b in edges:
            if union(a,b):
                return [a,b]
        


        