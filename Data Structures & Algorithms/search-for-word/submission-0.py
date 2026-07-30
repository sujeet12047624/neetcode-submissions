class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n=len(board)
        m=len(board[0])
        def dfs(r,c,i,visit):
            if i==len(word):
                return True
            if r in range(n) and  c in range(m) and (r,c) not in visit and word[i]==board[r][c]:
                visit.add((r,c))
                top=dfs(r+1,c,i+1,visit)
                bottom=dfs(r-1,c,i+1,visit)
                left=dfs(r,c-1,i+1,visit)
                right=dfs(r,c+1,i+1,visit)
                visit.remove((r,c))
                return top or right or left or bottom
            
            return False
        
        for r in range(n):
            for c in range(m):
                if dfs(r,c,0,set()):
                    return True
        return False





            


        