class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        seens = {}
        seent = {}
        if len(t) != len(s):
            return False
        for char in s:
            if char not in seens:
                seens[char] = 1
            else:
                seens[char] += 1
    
        
        for char in t:
            if char not in seent:
                seent[char] = 1
            else:
                seent[char] += 1
  
        
        if seent != seens:
            return False
        else:
            return True

    ## count number of letters in each string, compare each letter between the two
        