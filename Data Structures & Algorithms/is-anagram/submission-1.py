class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Scharacters = {}
        Tcharacters = {}
        if (len(s) != len(t)):
            return False
        for i in range(0, len(s)):
            numS =1
            numT =1
            if s[i] in Scharacters:
                numS = Scharacters[s[i]] + 1
            Scharacters.update({s[i]:numS})   
            if t[i] in Tcharacters:
                numT = Tcharacters[t[i]] + 1
            Tcharacters.update({t[i]:numT}) 
        if (Scharacters == Tcharacters):
            return True
        else:
            return False