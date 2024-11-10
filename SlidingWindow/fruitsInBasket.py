class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        d = {}
        ans = 0
        start=0

        for i in range(n):
            fruit = fruits[i]
            #expand
            if fruit in d:
                d[fruit]+=1
            else:
                d[fruit]=1

            #shrink
            while len(d)>2: #len of d can be not mare than 3
                d[fruits[start]]-=1
                if d[fruits[start]]==0:
                    del d[fruits[start]]
                start+=1

            #update
            curr_size = i-start+1
            ans=max(ans,curr_size)
        
        return ans

#TC= O(N+N) ~ O(N)
        


# [1,2,3,2,2]
# 2=>3
# 3=>1
# 1=>1

# 1,2
# b0 = 1, 
# b1 = 2, 
# ans=2

# 2,3,2,2
# b0 = 2,2,2
# b2 = 3, 
# ans=4


# where to start from? == you can choose
# you have to pick all fruits till you can take

# [2 1 1 0 0 2 2]
# ans=4
