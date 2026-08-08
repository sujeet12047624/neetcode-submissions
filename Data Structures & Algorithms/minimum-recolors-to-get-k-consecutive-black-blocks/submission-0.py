class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        n=len(blocks)
        l=0
        res=[]
        mn=float('inf')
        mp={}
        
        for r in range(n):
            mp[blocks[r]]=mp.get(blocks[r],0)+1
            if r-l+1==k:
                cnt=mp.get('W',0)
                mn=min(mn,cnt)
                mp[blocks[l]]=mp.get(blocks[l])-1
                if mp[blocks[l]]==0:
                    del mp[blocks[l]]
                l+=1
            print(mp)
            
        return mn
                
            
            

            

        