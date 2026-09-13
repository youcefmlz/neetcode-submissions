class Solution:

    
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings into a single string."""
        res = ""
        for word in strs:
            hashword= str(len(word))+'#'+word
            res+=hashword
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string back into a list of strings."""
        res , i = [], 0
        while i < len(s):
            j =i
            while s[j] !='#':
                j+=1
            length = int(s[i:j]) #dont forget to change its type to int
            res.append(s[j+1 :j+1+length])
            #update i so it starts at the next new word
            i = j+length+1
        return res
            



