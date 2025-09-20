class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operand_stack = []
        for token in tokens:
            try:
                token = int(token)
                operand_stack.append(token)
            except ValueError:
                op2, op1 = operand_stack.pop(), operand_stack.pop()
                if token == '+':
                    operand_stack.append(op1 + op2)
                elif token == '-':
                    operand_stack.append(op1 - op2)
                elif token == '*':
                    operand_stack.append(op1 * op2)
                elif token == '/':
                    operand_stack.append(int(op1 / op2))
        return operand_stack.pop()