def shunt(strExpression):
    tknExpression = tokenise(strExpression)
    output = []
    stack = []
    for token in tknExpression:
        if token[1] != -1: # Operators
            if token[1] == 0: # Bracket logic
                if token == "(":
                    stack.append(token)
                elif token == ")":
                    while stack[-1] != "(":
                        output.append(stack.pop())
                    stack.pop()
            else: # Normal operators
                while stack: # Skip precedence when empty stack
                    try:
                        if (stack[-1][1] >= token[1] and token[1] > 3) or (stack[-1][1] > token[1] and token[1] <= 3):
                            output.append(stack.pop())
                        else: break
                    except IndexError:
                        break
                stack.append(token)
        else: output.append(token) # Operands skip the stack
    while stack: # Purge the stack
        output.append(stack.pop())
    return "".join(output[0] for output in output)

def tokenise(strExpression): # Token Format: [Value, precedence]
    # Precedence is what decides whether operators are popped off the stack or not.
    # Operators with Precedence 3 or more are right associative, whereas 2 or less are left.
    tokens = list(strExpression)
    for i in range(len(tokens)): # Makes trig functions work
        maxIndex = len(tokens) - 1
        if i > maxIndex:
            break
        if tokens[i].isalpha():
            try: 
                flag = False
                if tokens[i] == "s" and tokens[i+1] == "i" and tokens[i+2] == "n":
                    tokens[i] = "sin"
                    del tokens[i+1:i+3]
                    maxIndex -= 2
                    flag = True


                elif tokens[i] == "c" and tokens[i+1] == "o" and tokens[i+2] == "s":
                    tokens[i] = "cos"
                    del tokens[i+1:i+3]
                    maxIndex -= 2
                    flag = True


                elif tokens[i] == "t" and tokens[i+1] == "a" and tokens[i+2] == "n":
                    tokens[i] = "tan"
                    del tokens[i+1:i+3]
                    maxIndex -= 2
                    flag = True

                if flag: # Function
                    newShunt = []
                    for j in range(i+2, len(tokens)):
                        if tokens[j] == ")":
                            break
                        newShunt.append(tokens[j])
                    maxIndex = len(tokens) - len(newShunt) - 2
                    newShunt = shunt("".join(newShunt))
                    newShunt = "".join([tokens[i], "(", newShunt, ")"])
                    del tokens[i:i+len(newShunt)-2]
                    tokens.insert(i, ["".join(newShunt), -1])
                else: # Variable or function not recognised, so treat as a variable.
                    tokens[i] = [tokens[i], -1]
            except IndexError: # Variable
                tokens[i] = [tokens[i], -1]
            if i >= maxIndex:
                break
        else:
            if tokens[i].isdigit(): # All values (incl. functions) are given a precedence of -1 to skip the stack.
                tokens[i] = [tokens[i], -1]
            else:
                match tokens[i]: # Precedences
                    case "(":
                        tokens[i] = [tokens[i], 0]
                    case ")":
                        tokens[i] = [tokens[i], 0]
                    case "+":
                        tokens[i] = [tokens[i], 1]
                    case "-":
                        tokens[i] = [tokens[i], 1]
                    case "*":
                        tokens[i] = [tokens[i], 2]
                    case "/":
                        tokens[i] = [tokens[i], 2]
                    case "^":
                        tokens[i] = [tokens[i], 3]
    return tokens

infix = input("Expression Here: ")
print(shunt(infix))