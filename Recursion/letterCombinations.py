class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {}
        mapping['2'] = "abc"
        mapping['3'] = "def"
        mapping['4'] = "ghi"
        mapping['5'] = "jkl"
        mapping['6'] = "mno"
        mapping['7'] = "pqrs"
        mapping['8'] = "tuv"
        mapping['9'] = "wxyz"

        ans=[]
        def helper(index, combination):
            if index == len(digits):
                #python people
                combination_str = "".join(combination)

                ans.append(combination_str)
                return
            
            #calls-loop ovetr the possible choices
            current_digit = digits[index]
            choices = mapping[current_digit]
            for char in choices:
                combination.append(char)
                helper(index+1, combination)
                combination.pop()
            
            return
        
        helper(0, [])
        return ans

        
#mapping 2->abc
#helper(digits, 0)
    #base case (on index)

    #calls
    # current digit = digits[index]
    #this current digits has some letter options, mapping[current_digit]
    #take each option, add it to your ans array, make a call to index+1
    #remove the character added before making the call
