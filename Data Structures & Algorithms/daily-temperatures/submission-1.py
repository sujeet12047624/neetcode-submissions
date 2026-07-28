class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n=len(temperatures)
        st=[]
        res=[0]*n

        for d,t in enumerate(temperatures):
            while st and st[-1][1]<t:
                x,y=st.pop()
                res[x]=d-x
            st.append((d,t))
        return res



        