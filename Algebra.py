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

def function(expression: str, plugInNumber: int):          
    # operators = []
    yValue = 0
    terms = expression.split("+")
    positives = []
    negatives = []
    # expressionSplit = expression.split("+")

    # for term in range(len(expressionSplit)):
    #     expressionSplit[term] = expressionSplit[term].strip()
    #     if expressionSplit[term].find("-") > -1:
    #         negatives = expressionSplit[term].split("-")
    #         for i in range(len(negatives)):
    #             if i == 0:
    #                 negativeValue = negatives[i].strip()
    #             else:
    #                 negativeValue = "-" + negatives[i].strip()
    #             positives.append(negativeValue)
    #         expressionSplit.pop(term)
    #         expressionSplit = expressionSplit[:term] + positives + expressionSplit[term:]

    new_terms = []
    for term in terms:
        sub_terms = term.strip().split("-")
        for idx in range(1, len(sub_terms)):
            sub_terms[idx] = "-" + sub_terms[idx].strip()
        new_terms += sub_terms

    

    print(new_terms)
    # for operator in expressionSplit:
    #     if operator == "+":
            
    #         # operators.append(operator)
    #         break

    #     else:
    #         print()
    #         pass




# A + Bx^C + Dx^E ...

def polynomial(expression: str):                #Expression example: x^2 + 4x + 4
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
                difference = factorsOfC[i] - factorsOfC[j]
                product = factorsOfC[i] * factorsOfC[j]
                if difference == int(terms[1].replace("x", "")) and product == C:
                    factoredForm = f"(x-{factorsOfC[i]})(x+{factorsOfC[j]})"
                    break
                
        print(factoredForm)

    else:                                       # operators[0] == "+" and operators[1] == "-"
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
                difference = factorsOfC[i] - factorsOfC[j]
                product = factorsOfC[i] * factorsOfC[j]
                if difference == int(terms[1].replace("x", "")) and product == C:
                    factoredForm = f"(x-{factorsOfC[i]})(x+{factorsOfC[j]})"
                    break
                
        print(factoredForm)

def quadratic(expression = str):                #Expression (-b +- sqrt(b^2 - 4ac)) / (2a)
    a = 0
    b = 0
    c = 0
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

    if terms[0] == "x^2":
        a = 1

    else:
        a = int(terms[0].replace("x^2", ""))

    if operators[0] == "-":
        b = -int(terms[1].replace("x", ""))
    
    if operators[1] == "-":
        c = -int(terms[2])
    
    numeratorAddition = -b + math.sqrt(exponent(b, 2) - 4 * a * c)

    numeratorSubtraction = -b - math.sqrt(exponent(b, 2) - 4 * a * c)

    denominator = 2 * a

    quotientAddition = numeratorAddition / denominator

    quotientSubtraction = numeratorSubtraction / denominator

    return quotientAddition, quotientSubtraction


    
# polynomial("x^2 + 16x + 60")
# polynomial("x^2 - 4x + 4")
# polynomial("x^2 - 3x - 4")
# polynomial("x^2 - 3x - 10")
# polynomial("x^2 + 13x - 30")
# quadratic("4x^2 - 15x - 90")

function("12x^4 + 4x^3 - 7x^2 - 10x^1 + 12", 3)
# function("56x^6 - 3x^5 + 12x^4 + 4x^3 - 7x^2 - 10x^1 + 12", 3)

