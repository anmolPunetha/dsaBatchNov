class Solution:
    def compare(self, s1_map,s2_map):
        # arrays of size 26
        for i in range(26):
            if s1_map[i]!=s2_map[i]:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        #first save characters of s1
        #first saving the 1st window explicitly
        #i will start sliding window loop
            #expand
            #shrink
            #compare and update
        if len(s1) > len(s2):
            return False

        s1_map = [0]*26
        s2_map = [0]*26
        
        for ch in s1:
            index = ord(ch)-ord('a')
            s1_map[index]+=1
        
        # doing for 1st window
        k = len(s1)
        for i in range(k):
            index = ord(s2[i])-ord('a')
            print(index)
            s2_map[index]+=1
        
        if self.compare(s1_map,s2_map):
            return True

        #window translation
        for i in range(k, len(s2)):
            #expand
            index = ord(s2[i])-ord('a')
            s2_map[index]+=1

            #shrink
            index = ord(s2[i-k])-ord('a')
            s2_map[index]-=1

            #update ans if possible
            if self.compare(s1_map,s2_map):
                return True
        
        return False

        

        
