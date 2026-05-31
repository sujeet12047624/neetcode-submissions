class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        st=[]
        n=len(temperatures)
        res=[0]*n
        for d,t in enumerate(temperatures):
            while st and st[-1][1]<t:
                curr,temp=st.pop()
                res[curr]=d-curr
            st.append([d,t])
        return res
        


        