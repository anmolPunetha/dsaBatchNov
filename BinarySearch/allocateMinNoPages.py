class Solution:
    def check_on_mid(self,mid, arr, k):
        #sum of books to any student<=mid
        
        #m trying to make the distribution
        #allocate books to students, 
        #how many pages read by the current person
        student = 1
        pages_read = 0
        for x in arr:
            if pages_read+x<=mid:
                pages_read+=x
            else:
                student+=1 # want a new student as the previous one is close to the limit
                pages_read = x
        
        if student>k:
            return False
        
        return True
        
        
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here
        books_count = len(arr)
        if k > books_count:
            #its not possible that each student will get atleast 1 book
            return -1
        
        #max pages read by a student should be min
        #search space will be based on pages
        start = max(arr)
        end = sum(arr)
            
        ans=-1
        while start<=end:
            mid = (start+end)//2
            if self.check_on_mid(mid, arr,k):
                ans = mid
                end = mid-1
            else:
                start = mid+1
                
        return ans
