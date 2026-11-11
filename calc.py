import math

operators = {
    "+" : 1 ,
    "-" : 1 ,
    "*" : 2 ,
    "/" : 2 ,
    "%" : 2 ,
    "^" : 3 ,
}

functions = {
    "sqrt" : math.sqrt
}

def calc_banner():
    print("╔══════════════════════════════════════╗")
    print("║             AUVRION CALC             ║")
    print("║     Scientific Terminal Calculator   ║")
    print("╠══════════════════════════════════════╣")
    print("║ Type 'menu' to see all Calc-Commands ║")
    print("╚══════════════════════════════════════╝")

def menu() :
    print("╔═════════════════════════════════════════════╗")
    print("║                 Menu Section                ║")
    print("╠═════════════════════════════════════════════╣")
    print("║ do add spaces between operators and numbers ║")
    print("╚═════════════════════════════════════════════╝")

def tokenize(expression):
    tokens = expression.split()
    return tokens

def is_number(token) :
    try :
        float(token)
        return True
    except ValueError :
        return False
          

def validate_operators(tokens) :
    expecting = "number"
    bracket_count = 0

    for token in tokens :
        if is_number(token) :
            if expecting != "number" :
                print("Error! Number received when operator was expected")              
                return False
            expecting = "operator"
        elif token in operators :
            if expecting != "operator" :
                print("Error! Operator received when number was expected")
                return False
            expecting = "number"
        elif token in functions :
            if expecting != "number" :
                print("Error ! Wrong position of Expression ")
                return False
            expecting = "bracket"
        elif token == "(" :
            if expecting not in ("number" , "bracket") :
                print("Error ! Opening bracket in wrong position ")
                return False
            bracket_count += 1
            expecting = "number"
        elif token == ")" :
            if expecting != "operator":
                print("Error ! Closing bracket in wrong position")
                return False
            if bracket_count == 0 :
                print("Error ! missing opening brakets in expression ")
                return False
            bracket_count -= 1
            expecting = "operator"
        else:
            print(f"Invalid '{token}' Operator Entered")
            return False
    if expecting == "number" :
        print("Error ! Expression cannot end with an operator ")
        return False
    if bracket_count != 0:
        print("Error! Missing closing bracket")
        return False
    return True
        

def infix_to_postfix(tokens):
    output = []
    stack = []

    for token in tokens:
        # check if token is a number
        if is_number(token):
            output.append(token)

        #opening braket 
        elif token == "(" :
            stack.append(token)

        elif token in functions:
            stack.append(token)

        #closing braket
        elif token == ")" :
            while stack and stack[-1] != "(" :
                output.append(stack.pop())
            stack.pop() 

            #for functions   
            if stack and stack[-1] in functions:
                output.append(stack.pop())

        # otherwise it is an operator
        else:
            while stack and stack[-1] != "(" and operators[stack[-1]] >= operators[token]:
                last_pop = stack.pop()
                output.append(last_pop) 
    
            stack.append(token)
                                     
    while stack :
        popped = stack.pop()
        output.append(popped)

    return output

def postfix_evaluation(postfix) :
    stack = []

    for exp in postfix :
        if is_number(exp) :
            stack.append(float(exp))
        elif exp in functions :
            value = stack.pop()
            result = functions[exp](value)
            stack.append(result)
        else :
            b = stack.pop()
            a = stack.pop()
            if exp == "+" :
                stack.append(a+b)
            if exp == "-" :
                stack.append(a-b)
            if exp == "*" :
                stack.append(a*b)
            if exp == "/" :
                stack.append(a/b)
            if exp == "%" :
                stack.append(a%b)
            if exp == "^" :
                stack.append(a**b)
    return stack.pop() 

def main():
    calc_banner()

    while True:
        cmd_input = input("@ >> Calc >> ")
        if cmd_input.lower().strip() == "exit":
            print("Exiting Scientific calculator byiiii !")
            break
        if cmd_input.lower().strip() == "menu":
            menu()
        try :
            tokens = tokenize(cmd_input)

            if not validate_operators(tokens):
                continue

            postfix = infix_to_postfix(tokens)
#            print(postfix)
            postfix_eval = postfix_evaluation(postfix)

            print(">> calc >> ",postfix_eval)

        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")

        except IndexError:
            print("Error: Invalid / Incomplete expression")

        except KeyError:
            print("Error: Unknown operator") 
        
if __name__ == "__main__":
    main()