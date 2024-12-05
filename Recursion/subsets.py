class Solution:
    def helper(self, index, ans, nums):
        if index==len(nums):
            #i have got a subset
            #print/store
            self.result.append(ans.copy()) #ans is again saved as reference
            return

        #leave call
        self.helper(index+1, ans, nums)

        #take
        ans.append(nums[index])
        self.helper(index+1, ans, nums)
        ans.pop() # backtracking step

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.helper(0, [], nums)
        return self.result


        
