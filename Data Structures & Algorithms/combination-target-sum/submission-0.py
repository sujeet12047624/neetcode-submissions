class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        n=len(nums)
        res=[]
        def dfs(i,sm,path):
            if sm==target:
                res.append(path.copy())
                return
            
            if sm>target:
                return
            for j in range(i,n):
                path.append(nums[j])
                dfs(j,sm+nums[j],path)
                path.pop()
        
        nums.sort()
        dfs(0,0,[])
        return res
            
        