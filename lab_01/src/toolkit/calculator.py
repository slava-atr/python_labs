import re

from constants import TOKEN_PATTERN, Stack


def tokenize(expression):
    tokens = [match.group() for match in re.finditer(TOKEN_PATTERN, expression)]
    return tokens


def shunting_yard(tokens):
    output_queue = []
    operators = Stack()

    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}

    for token in tokens:
        if token.isdigit():
            output_queue.append(token)
        elif token == "(":
            operators.push(token)
        elif token == ")":
            while not operators.is_empty() and operators.items[-1] != "(":
                output_queue.append(operators.pop())
            if not operators.is_empty() and operators.items[-1] == "(":
                operators.pop()
        elif token in precedence:
            while (not operators.is_empty() and operators.items[-1] in precedence and \
                   precedence[operators.items[-1]] >= precedence[token]):
                output_queue.append(operators.pop())
            operators.push(token)

    while not operators.is_empty():
        output_queue.append(operators.pop())

    return output_queue


def calculate_rpn(tokens):
    numbers = Stack()

    for token in tokens:
        if token.isdigit():
            numbers.push(float(token))
        else:
            second_number = numbers.pop()
            first_number = numbers.pop()
            
            if token == "+":
                result = first_number + second_number
            elif token == "-":
                result = first_number - second_number
            elif token == "*":
                result = first_number * second_number
            elif token == "/":
                result = first_number / second_number

            numbers.push(result)

    return numbers.pop()
