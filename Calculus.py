import math
import BasicOperations
import Algebra

def limits(expression: str):          
    operators = []
    terms = []
    expressionSplit = expression.split()
    
    for operator in expressionSplit:
        if operator == "+" or operator == "-":
            operators.append(operator)
    for term in expressionSplit:
        if not (term == "+" or term == "-"):
            terms.append(term)

def derivatives():
    pass

