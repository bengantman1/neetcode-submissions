class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+', '-', '*', '/'])
        stack = []

        if len(tokens) == 1:
            return int(tokens[0])
        stack.append(int(tokens[0]))
        stack.append(int(tokens[1]))

        for i in range(2, len(tokens)):
            
            if tokens[i] in operators:
                if tokens[i] == "+":
                    stack.append(stack.pop() + stack.pop())
                elif tokens[i] == '-':
                    r2 = stack.pop()
                    r1 = stack.pop()
                    stack.append(r1 - r2)
                elif tokens[i] == '*':
                    stack.append(stack.pop() * stack.pop())
                elif tokens[i] == '/':
                    r2 = stack.pop()
                    r1 = stack.pop()
                    stack.append(int(r1 / r2))
            else:
                stack.append(int(tokens[i]))

        return stack.pop()


