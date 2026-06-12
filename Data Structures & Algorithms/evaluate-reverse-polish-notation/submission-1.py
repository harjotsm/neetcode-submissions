class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        # loop over tokens
        for i in tokens:
                # stack to track the operants
                # if there is an operator in tokens, pop from stack and do operation
                # push the result back to the stack  
                if i == "+":
                    stack.append(stack.pop() + stack.pop())
                elif i == "-":
                    a,b = stack.pop(), stack.pop()
                    stack.append(b - a)
                elif i == "*":
                    stack.append(stack.pop() * stack.pop())
                elif i == "/":
                    a,b = stack.pop(), stack.pop()
                    stack.append(int(float(b)/a))
                else:
                    stack.append(int(i))
        
        return stack[0]
        
