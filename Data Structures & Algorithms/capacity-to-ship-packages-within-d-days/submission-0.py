class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canship(c):
            s=1
            cl=0

            for w in weights:
                if cl+w>c:
                    s+=1
                    cl=w
                else:
                    cl+=w
            return s<=days
        
        l=max(weights)
        r=sum(weights)
        while l<r:
            mid=l+(r-l)//2
            if canship(mid):
                r=mid
            else:
                l=mid+1
        
        return l

        