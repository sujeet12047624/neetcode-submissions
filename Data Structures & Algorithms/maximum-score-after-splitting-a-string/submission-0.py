class Solution:
    def maxScore(self, s: str) -> int:

        ans=0
        n=len(s)
        l=0
        r=n-1
        for i in range(1,n):
            ls=s[:i]
            rs=s[i:]

            sm=ls.count('0')+rs.count('1')
            ans=max(ans,sm)
        return ans
        