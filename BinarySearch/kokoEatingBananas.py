class Solution:
    def check_on_mid(self, mid, piles, h):
        #mid is speed
        needed_hours = 0
        for pile in piles:
            #for each pile
            #calculate how many hours you need
            curr_pile_need = pile//mid
            if (pile%mid)!=0:
                curr_pile_need+=1

            needed_hours+=curr_pile_need

        if needed_hours<=h:
            return True
        return False
# 11//5=2
# 13%5->1 more hr

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # it will be from 1 to max(piles)
        start = 1
        end = max(piles)

        ans = 0 #i will update the answer in this

        while start<=end:
            
            mid = (start+end)//2
            #mid is expected k value for which we need to check

            if self.check_on_mid(mid, piles, h)==True:
                ans=mid
                #try for lesser value=>left
                end = mid-1
            else:
                # move towards higher value=>right
                start=mid+1
            
        return ans

#binary search on ans
