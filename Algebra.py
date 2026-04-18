import math
import BasicOperations

def exponent(base, power):              # For sqrt, use 0.5 or (1/2) in power
    product = math.pow(base, power)
    return product

def log(base, product):                 # For ln, use math.e in base
    power = math.log(product, base)
    return power

# def ln(product):
#     power = math.log(product)
#     return power

def factorial(integer):
    counter = integer
    product = math.factorial(integer)
    print(f"!{integer} = ", end="")

    while counter > 0:
        if counter == 1:
            print(f"{counter} = {product}")
            break 
        print(f"{counter} * ", end="")
        counter -= 1

    return product

def polynomial(expression = str):                #Expression example: x^2 + 4x + 4
    factoredForm = ""            
    operators = []
    terms = []
    expressionSplit = expression.split()
    
    for operator in expressionSplit:
        if operator == "+" or operator == "-":
            operators.append(operator)
    for term in expressionSplit:
        if not (term == "+" or term == "-"):
            terms.append(term)

    print(operators, terms)
    
    if operators[0] == "+" and operators[1] == "+":
        C = int(terms[2])
        counter = 1
        factorsOfC = []
        while counter < C + 1:
            if BasicOperations.modulus(C, counter, False) == 0:
                answer = BasicOperations.divide(C, counter, showProcess=False)
                factorsOfC.append(int(answer))
            counter += 1


        print(factorsOfC)
        n = len(factorsOfC)

        for i in range(n):
            for j in range(i, n):
                sum = factorsOfC[i] + factorsOfC[j]
                product = factorsOfC[i] * factorsOfC[j]
                if sum == int(terms[1].replace("x", "")) and product == C:
                    factoredForm = f"(x+{factorsOfC[i]})(x+{factorsOfC[j]})"
                    break
                
        print(factoredForm)

    elif operators[0] == "-" and operators[1] == "+":
        C = int(terms[2])
        counter = 1
        factorsOfC = []
        while counter < C + 1:
            if BasicOperations.modulus(C, counter, False) == 0:
                answer = BasicOperations.divide(C, counter, showProcess=False)
                factorsOfC.append(int(answer))
            counter += 1


        print(factorsOfC)
        n = len(factorsOfC)

        for i in range(n):
            for j in range(i, n):
                difference = -factorsOfC[i] - factorsOfC[j]
                product = factorsOfC[i] * factorsOfC[j]
                if difference == -int(terms[1].replace("x", "")) and product == C:
                    factoredForm = f"(x-{factorsOfC[i]})(x-{factorsOfC[j]})"
                    break
                
        print(factoredForm)


    elif operators[0] == "-" and operators[1] == "-":
        pass
    else:                                       # operators[0] == "+" and operators[1] == "-"
        pass


    
polynomial("x^2 + 16x + 60")
polynomial("x^2 - 4x + 4")

