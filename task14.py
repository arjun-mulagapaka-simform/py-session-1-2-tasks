'''
    Exercise 14: Stack & Queue - Expression Evaluator
'''

from collections import deque

# 1. Balanced parentheses checker using stack
def is_balanced_parentheses(expr):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}
    for char in expr:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != matching[char]:
                return False
    return not stack

# 2. Infix to postfix converter
def infix_to_postfix(expr):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    stack = []
    output = []
    
    for char in expr:
        if char.isalnum():  # operand
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # pop '('
        else:  # operator
            while stack and stack[-1] != '(' and precedence.get(char, 0) <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(char)
    
    while stack:
        output.append(stack.pop())
    
    return ''.join(output)

# 3. Postfix expression evaluator
def evaluate_postfix(expr):
    stack = []
    for char in expr:
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+': stack.append(a + b)
            elif char == '-': stack.append(a - b)
            elif char == '*': stack.append(a * b)
            elif char == '/': stack.append(a / b)
            elif char == '^': stack.append(a ** b)
    return stack[0]

# 4. Queue-based level-order traversal of a binary tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def level_order_traversal(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

# Function to detect type of expression
def detect_expression(expr):
    expr = expr.replace(" ", "")
    
    # If it contains only parentheses/brackets
    if all(c in '(){}[]' for c in expr):
        return 'parentheses'
    
    # If it contains operators or digits/letters, check for infix or postfix
    operators = set('+-*/^')
    operands = set('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    # If any invalid characters are present, return unknown
    if any(c not in operators and c not in operands and c not in '()' for c in expr):
        return 'unknown'
    
    # Check if it could be postfix
    stack_counter = 0
    is_postfix_possible = True
    for c in expr:
        if c in operands:
            stack_counter += 1
        elif c in operators:
            if stack_counter < 2:
                is_postfix_possible = False
                break
            stack_counter -= 1  # two operands popped, one result pushed
        else:  # parentheses in postfix -> not valid
            is_postfix_possible = False
            break
    if is_postfix_possible and stack_counter == 1:
        return 'postfix'
    
    # If not postfix, assume infix
    return 'infix'

# Main to test all features
def main():
    # Test cases
    expressions = [
        "((a+b)*c)",       # balanced parentheses + infix
        "a+b*c",           # infix without parentheses
        "23+5*",           # postfix
        "((()))",          # parentheses only
        "3+4*2/(1-5)^2",    # more complex infix
        "34+2*7/"     
    ]
    
    print("==== Expression Tests ====")
    for expr in expressions:
        print(f"\nExpression: {expr}")
        expr_type = detect_expression(expr)
        print(f"Detected type: {expr_type}")
        
        if expr_type == 'parentheses':
            print("Balanced:" , is_balanced_parentheses(expr))
        elif expr_type == 'infix':
            postfix = infix_to_postfix(expr.replace(" ", ""))
            print(f"Postfix: {postfix}")
            # Evaluate if purely numeric
            if all(c.isdigit() or c in '+-*/^' for c in postfix):
                print(f"Evaluation: {evaluate_postfix(postfix)}")
        elif expr_type == 'postfix':
            print(f"Evaluation: {evaluate_postfix(expr)}")
        else:
            print("Cannot process this expression")
    
    # Test binary tree level-order traversal
    print("\n==== Binary Tree Level-order Traversal Test ====")
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Level-order traversal:", level_order_traversal(root))

if __name__ == "__main__":
    main()