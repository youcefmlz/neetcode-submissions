class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lengthOfS = len(s)
        if(lengthOfS % 2 !=0):
            print("inside first ")
            return False
        else:
            for i in range(lengthOfS):
                if (s[i]=='[' or s[i]=='{' or s[i]=='('):
                    stack.append(s[i])
                else:
                    if len(stack )==0:
                        return False
                    pop = stack.pop() 
                    match s[i]:
                        case ']':
                            if pop !='[': return False
                        case ')':
                            if pop !='(': return False
                        case '}':
                            if pop !='{': return False



        if len(stack )!=0:
            return False
         
        return True
