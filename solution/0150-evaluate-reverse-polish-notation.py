class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                operand_b = stack.pop()
                operand_a = stack.pop()

                calced = 0

                if token == "+":
                    calced = operand_a + operand_b
                elif token == "-":
                    calced = operand_a - operand_b
                elif token == "*":
                    calced = operand_a * operand_b
                elif token == "/":
                    calced = int(operand_a / operand_b)

                stack.append(calced)

        return stack[0]
