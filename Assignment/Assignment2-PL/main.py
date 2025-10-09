# Programming Assignment 2
# Building a Parse Tree Based Arithmetic Expression Evaluator
# Build tokenizer, parsing & validation, and calculate

# Tokenizer
# Tokenizes the input expression string into a list of tokens
def tokenizer(expr):
    # tokens: a list of tokens from the input expression string
    tokens = []
    # number: to build multi-digit numbers
    number = ''
    
    # iterate through each character in the expression
    for char in expr:
        # if the character is a digit, build the number
        if char in '0123456789':
            number += char
        # not digit
        else:
            # append integer value of number to token
            if number:
                tokens.append(number)
                number = ''
            
            # append operators and parentheses to token
            if char in '^+-*/()':
                tokens.append(char)
            # ignore whitespace
            elif char in ' \t\n':
                continue
            #invalid character
            else:
                tokens.append(char)
                
    # if number still not empty, add it to token
    if number:
            tokens.append(number)
            number = ''
    
    # return the token list
    return tokens   

# Parsing
# Recursive descent parser based on operator precedence

# parse factor: highest precedence: (), numbers, unary -
# factor -> - factor | ( expr ) | integer
def parse_factor(tokens, index):
    # check if index is within bounds
    if index >= len(tokens):
        raise ValueError("Unexpected end of expression")
    
    # get the current token
    token = tokens[index]

    # handle unary minus
    if token == '-':
        # right associative
        # recursively parse the next factor
        subtree, next = parse_factor(tokens, index + 1)

        # add unary minus node to the parse tree and return
        return ('neg', subtree), next
    # handle numbers
    elif token.isdigit():
        # return the number as an integer
        return int(token), index + 1
    # handle parentheses
    elif token == '(':
        # recursively call expr to parse the expression inside parentheses
        subtree, next = parse_expr(tokens, index + 1)
        # check for closing parenthesis
        # check for length as well to avoid index error
        if next >= len(tokens) or tokens[next] != ')':
            raise ValueError("Mismatched parentheses")
        
        # return the subtree
        return subtree, next + 1
    # unexpected token
    else:
        raise ValueError(f"Unexpected token: {token}")

# parse power: 2nd highest precedence: ^
# right associative
# power -> <factor> ( ^ <power> )
def parse_power(tokens, index):
    # parse the left factor
    left, next = parse_factor(tokens, index)

    # if the next token is ^, parse the right power
    if next < len(tokens) and tokens[next] == '^':
        # get the operator
        op = tokens[next]
        # parse the right power (right associative)
        right, next = parse_power(tokens, next + 1)
        # build the subtree
        left = (op, left, right)
    
    # return subtree
    return left, next

# parse term: 3rd highest precedence: *, /
# left associative
# term -> power ( (*|/) power )
def parse_term(tokens, index):
    # parse the left power
    left, next = parse_power(tokens, index)

    # while the next token is */, parse the right power
    while next < len(tokens) and tokens[next] in '*/':
        # get the operator
        op = tokens[next]
        # parse the right power
        right, next = parse_power(tokens, next + 1)
        # build the subtree
        left = (op, left, right)
    
    # return subtree
    return left, next

# parse expr: lowest precedence: +, -
# left associative
# expr -> term ( (+|-) term )
def parse_expr(tokens, index):
    # parse the left term
    left, next = parse_term(tokens, index)

    # while the next token is +-, parse the right term
    while next < len(tokens) and tokens[next] in '+-':
        # get the operator
        op = tokens[next]
        # parse the right term
        right, next = parse_term(tokens, next + 1)
        # build the subtree
        left = (op, left, right)
    
    # return subtree
    return left, next 

# Parser
# Parses and detects invalid expressions
def parser(tokens):
    # parse tree: tuple (operator, left subtree, right subtree)
    parse_tree = ()
    parse_tree, num_of_tokens = parse_expr(tokens, 0)
    if num_of_tokens != len(tokens):
        raise ValueError("Invalid expression")
    return parse_tree

# calculate
def calculator(parse_tree):
    # if the parse tree is an integer, return it
    if isinstance(parse_tree, int):
        return parse_tree

    # get the operator
    op = parse_tree[0]

    # handle unary minus
    if op == 'neg':
        return -calculator(parse_tree[1])
    
    # recursively evaluate left and right subtrees
    left = calculator(parse_tree[1])
    right = calculator(parse_tree[2])

    # perform the operation based on the operator
    if op == '+':
        return left + right
    elif op == '-':
        return left - right
    elif op == '*':
        return left * right
    elif op == '/':
        return left / right
    elif op == '^':
        return left ** right

# access and run files
def run_from_file(input_file, result_file):
    # read expressions from input file
    with open(input_file, 'r') as read:
        expressions = read.readlines()
    
    # write results to output file
    with open(result_file, 'w') as write:
        # process each expression
        for expr in expressions:
            # strip whitespace
            expr = expr.strip()
            write.write(f"Expression: {expr}\n")

            # tokenizer and write to file
            tokens = tokenizer(expr)
            write.write(f"Tokens: {tokens}\n")

            # parser with validation
            try:
                # parser and write to file
                parse_tree = parser(tokens)
                write.write(f"Parse Tree: {parse_tree}\n")
            # catch parsing errors
            except ValueError as e:
                # write error message to file
                write.write(f"Error\n\n")
                continue

            # calculate and write to file
            result = calculator(parse_tree)
            write.write(f"Result: {result}\n\n")
        
# run the program
run_from_file('expressions.txt', 'result.txt')