class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Scharacters , Tcharacters  = {} , {}
        if (len(s) != len(t)):
            return False
        for i in range(0, len(s)):
            Scharacters[s[i]] = 1 + Scharacters.get(s[i],0)
            Tcharacters[t[i]] = 1 + Tcharacters.get(t[i],0)
        return Scharacters == Tcharacters