class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #kadane's algo for op1
        #min sum subarray for op2
        
        #max sum subarray
        cs,ms=0,0
        for x in nums:
            cs+=x
            if cs<0:
                cs=0
            ms = max(ms, cs)
        op1 = ms

        #min sum subarry
        cs,min_sum=0,0
        for x in nums:
            cs+=x
            if cs>0:
                cs=0
            min_sum = min(min_sum, cs)
        
        total = sum(nums)
        op2 = total-min_sum

        #all nums are negative
        # op2==0 is also correct, bcz when total==min_sum, then only it will 0
        if op2==0: #i was not able to find max sum bcz all were negative
            return max(nums)

        return max(op1,op2)



# tc: O(N+N)~O(N)


        
