class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st=[]
        res=[]

        for ch in operations:
            if ch=='+':
                if len(st)>=2:
                    st.append(st[-1]+st[-2])
                    
            elif ch=='D':
                if st: 
                    st.append(2*st[-1])
            elif ch=='C':
                if st:
                    del st[-1]
            else:
                st.append(int(ch))
        print(st)
        return sum(st)


        