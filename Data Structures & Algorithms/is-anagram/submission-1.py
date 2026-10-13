class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ##two lists for each that updates
        ##find count for each and compare
        ## if same. then anagram
        ## else reject

        seens = {}
        seent = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char in seens:
                seens[char] += 1
            else:
                seens[char] = 1
        for char in t:
            if char in seent:
                seent[char] += 1
            else:
                seent[char] = 1
        
        if seens != seent:
            return False

        return True