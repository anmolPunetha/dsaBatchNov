class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        curr_sum=0
        #initial k elements
        for i in range(k):
            curr_sum+=nums[i]
        
        #i have got the sum of the first subarray
        max_sum = curr_sum
        
        #sliding window loop
        for i in range(k,n): #i===>the end of the window, i-k is the start
            #expanding the end
            #shrinking from the beginning
            #update

            curr_sum+=nums[i]
            curr_sum-=nums[i-k]
            max_sum=max(max_sum, curr_sum)
        
        return max_sum/k


# TC: O(K + N-K) = O(N)
# SC: O(1)

        
