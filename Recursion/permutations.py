class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []

        def helper(index):
            #base case-when to stop
            if index==len(nums):
                #i have got a permutation saved in the array
                ans.append(nums.copy()) # i want a separate copy
                return
            
            for j in range(index,len(nums)):
                #swap characters at index, j
                nums[index], nums[j] = nums[j], nums[index]
                helper(index+1)
                nums[index], nums[j] = nums[j], nums[index] #restoring part

        helper(0)
        return ans

