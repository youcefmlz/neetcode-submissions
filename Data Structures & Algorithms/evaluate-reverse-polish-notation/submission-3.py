class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        maths = []
        for token in tokens:
            


            if token == '+':
                maths.append(maths.pop() + maths.pop())
            elif token == '-':
                number1= int(maths.pop())
                number2 = int(maths.pop())
                maths.append(number2 - number1)
            elif token == '*':
                maths.append(maths.pop()*maths.pop())
            elif token == '/':
                number1= int(maths.pop())
                number2 = int(maths.pop())
                maths.append(int(number2 / number1))
            else:
                maths.append(int(token))

        return int(maths.pop())