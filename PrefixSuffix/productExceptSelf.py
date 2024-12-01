class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        #prefix, suffix product array
        pre = [0]*n
        suf = [0]*n

        #populating prefix product array
        pre[0]=nums[0]
        for i in range(1,n):
            pre[i] = pre[i-1]*nums[i]


        #populating suffix product array
        suf[n-1]=nums[n-1]
        for i in range(n-2, -1, -1):
            suf[i] = suf[i+1]*nums[i]
        
        #build answer array
        ans = [0]*n
        for i in range(n):
            if i==0:
                ans[i] = suf[i+1]
            elif i==n-1:
                ans[i]=pre[i-1]
            else:
                ans[i] = pre[i-1] * suf[i+1]
        
        return ans
