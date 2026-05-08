class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:                      
            return ""

        prefix = ""
        reference = strs[0]               

        for i in range(len(reference)):   
            char = reference[i]

            for word in strs[1:]:         
                if i >= len(word) or word[i] != char:
                    return prefix         

            prefix += char                

        return prefix
            


        
