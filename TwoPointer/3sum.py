class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = [] # overall ans, contains all the tripltes
        nums.sort()
        n = len(nums)

        for idx in range(0, n): # this is for A
            if idx > 0 and nums[idx] == nums[idx-1]: # to handle duplicate start value
                continue

            # 2sum comes here
            i = idx + 1
            j = n -1
            new_target = -nums[idx]  #a+b+c=0, b+c=-a(target for the two), b+c=target-A

            while i < j:
                curr_sum = nums[i]+nums[j]
                if curr_sum < new_target:
                    i += 1
                elif curr_sum > new_target:
                    j -= 1
                else:
                    # got a triplet
                    ans.append([nums[idx], nums[i], nums[j]]) #A,B,C

                    #handle the duplicate i,j values for that corresponding idx
                    #until that i-th number is same, keep incrementing i to reach new element
                    #_ 1 1 1 1 2 3 3 3
                    #  i             j
                    ele = nums[i]
                    while i<j and nums[i]==ele:
                        i+=1
        return ans
