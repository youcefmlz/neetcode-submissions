class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        maths = []
        for token in tokens:
            if token in ['-','+', '*', '/']:
                number1= int(maths.pop())
                number2 = int(maths.pop())

                if token == '+':
                    newNum = number1 + number2
                elif token == '-':
                    newNum = number2 - number1
                elif token == '*':
                    newNum = number1 * number2
                elif token == '/':
                    newNum = float(number2) / number1
                maths.append(newNum)
            else:
                maths.append(token)

        return int(maths.pop())