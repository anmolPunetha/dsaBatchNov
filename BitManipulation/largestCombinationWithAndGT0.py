class Solution:
    #greedy approaches
    def largestCombination(self, candidates: List[int]) -> int:
        ans = 0
        for i in range(32):
            #i am iterating over ith position bit for all numbers
            mask = 1<<i
            count = 0
            for x in candidates:
                # check about the ith bit of this no. x
                if (x&mask)!=0:
                    count+=1
            
            #i have the nonzero bitwise and ans based on that bit
            ans = max(ans, count)

        return ans
