class Token:
    def __init__(self, value, is_operator=False, is_parenthesis=False):
        self.value = value
        self.is_operator = is_operator
        self.is_parenthesis = is_parenthesis

    def __repr__(self):
        return f"Token({self.value})"

class Lexer:
    def tokenize(self, expression):
        tokens = []
        number = ''
        for char in expression:
            if char.isdigit() or char == '.':
                number += char
            else:
                if number:
                    tokens.append(Token(number))
                    number = ''
                if char in '+-*/':
                    tokens.append(Token(char, is_operator=True))
                elif char in '()':
                    tokens.append(Token(char, is_parenthesis=True))
        if number:
            tokens.append(Token(number))
        return tokens

class RPNConverter:
    def to_rpn(self, tokens):
        output = []
        stack = []
        operator_precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        for token in tokens:
            if token.is_operator:
                while stack and stack[-1].is_operator and operator_precedence[stack[-1].value] >= operator_precedence[token.value]:
                    output.append(stack.pop())
                stack.append(token)
            elif token.is_parenthesis:
                if token.value == '(':
                    stack.append(token)
                else:
                    while stack and stack[-1].value != '(':
                        output.append(stack.pop())
                    stack.pop()  # Pop the '('
            else:
                output.append(token)
        while stack:
            output.append(stack.pop())
        return output

class Calculator:
    def calculate(self, rpn_expression):
        stack = []
        for token in rpn_expression:
            if token.is_operator:
                b = stack.pop()
                a = stack.pop()
                if token.value == '+':
                    result = a + b
                elif token.value == '-':
                    result = a - b
                elif token.value == '*':
                    result = a * b
                elif token.value == '/':
                    if b == 0:
                        raise ValueError("Division by zero")
                    result = a / b
                stack.append(result)
            else:
                stack.append(float(token.value))
        return stack[0] if stack else 0
