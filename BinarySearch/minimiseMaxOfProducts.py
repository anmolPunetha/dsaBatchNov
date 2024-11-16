class Solution:
    def check_on_mid(self, mid, quantities, n):
        # for given mid(limit) i have to check whether in n shops i can have it or not
        total_shops = 0
        for element in quantities:
            #getting the shops needs for the current product
            no_of_shops_required = element // mid
            if element%mid!=0:
                no_of_shops_required+=1
            
            #adding it to toal req
            total_shops+=no_of_shops_required
        
        if total_shops<=n:
            return True
        return False
            
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        start = 1
        end = max(quantities)

        ans = 0
        while start<=end:
            mid = (start+end)//2
            if self.check_on_mid(mid, quantities, n):
                ans = mid
                end = mid - 1 #we want to go to left to search for smaller value
            else:
                start = mid+1
        
        return ans

#M, K
#TC: logM * K = O(KlogM), k is the size of the array, M is the max(array)
# n = 6, quantities = [11,6]
# n=17
# 1 1 1 1 1. 

# ->a shop can have atmost product type
# 11 6 0 0 0 0
# shop1=11

# 6 5 6 0 0 0
# ans=6

# 3 3 3 2 3 3
# ans=3


# get a minimum ans = (ans = max of all in a particular distribution)

#facts->>>
#more shops->reduce the ans-> they can bear/have some products
