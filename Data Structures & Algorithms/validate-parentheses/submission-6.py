class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        myHashMap = {']':'[' , '}':'{' , ')':'(' }

        for character in s : 
            if stack and character in myHashMap:
                if(stack[-1] == myHashMap[character] ):
                    stack.pop()
                else : 
                    return False
            else : 
                stack.append(character)
        
        return True if not stack else  False