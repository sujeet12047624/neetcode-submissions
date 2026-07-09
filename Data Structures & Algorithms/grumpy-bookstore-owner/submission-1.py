class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        cnt=0
        m=len(customers)
        for i in range(m):
            if grumpy[i]==0:
                cnt+=customers[i]
                customers[i]=0
        
        
        print(customers)
        mx=0
        l=0
        windowsum=0

        for i in range(m):
            windowsum+=customers[i]
            if i-l+1>minutes:
                windowsum-=customers[l]
                l+=1
            mx = max(mx, windowsum)

            
        print(mx)
        print(cnt)
        return cnt+mx
        