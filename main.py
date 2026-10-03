def shunt(strExpression):
    tknExpression = list(strExpression)
    precedence = {"+" : 1, # Precedence is what decides whether operators are popped off the stack or not.
                  "-" : 1, # Operators with Precedence 3 or more are right associative, whereas 2 or less are left.
                  "*" : 2,
                  "/" : 2,
                  "^" : 3,
                  "sin" : 4,
                  "cos" : 4,
                  "tan" : 4}
    output = []
    stack = []
    for token in tknExpression:
        if token in precedence: # Operators
            if precedence[token] == 0: # Bracket logic
                if token == "(":
                    stack.append(token)
                elif token == ")":
                    while token != "(":
                        output.append(stack.pop())
                    stack.pop()
            else: # Normal operators
                if stack: # Skip precedence when empty stack
                    while (precedence[stack[-1]] >= precedence[token] and precedence[token] > 3) or (precedence[stack[-1]] > precedence[token] and precedence[token] <= 3):
                        output.append(stack.pop())
                stack.append(token)
        else: output.append(token) # Operands skip the stack
    while stack: # Purge the stack
        output.append(stack.pop())
    return "".join(output)

infix = input("Expression Here: ")
print(shunt(infix))