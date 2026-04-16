#This file will contain functions that will return the answer for the following operations: 
# Addition(+), Subtraction(-), Multiplication(*), Division(/), Exponents(** or ^)

def add(*addends: int):
    sum = 0
    if type(addends[0]) == "list":
        addends = addends[0]

    if len(addends) == 1:
        print(f"{addends[0]} = {addends[0]}")
        sum = addends[0]

        return sum
    
    else:
        sum = addends[0]
        for addend in addends:
            if addend == addends[0]:
                continue

            print(f"{sum} + {addend}", end="")
            sum += addend
            print(f" = {sum}", end="\n")

        return sum

def subtract(minuend: int, /, *subtrahends: int):
    difference = 0

    if subtrahends == (()):
        print(f"{minuend} = {minuend}")
        difference = minuend
        
        return difference
    
    else:
        difference = minuend - subtrahends[0]
        print(f"{minuend} - {subtrahends[0]} = {difference}")
        for subtrahend in subtrahends:
            print(f"{difference} - {subtrahend}", end="")
            difference -= subtrahend
            print(f" = {difference}", end="\n")

        return difference

def multipy(*factors: int):
    product = 0

    if len(factors) == 1:
        print(f"{factors[0]} = {factors[0]}")
        product = factors[0]

        return product
    
    else:
        product = factors[0]
        for factor in factors:
            if factor == factors[0]:
                continue

            print(f"{product} * {factor}", end="")
            product *= factor
            print(f" = {product}", end="\n")

        return product

def divide(dividend: int, *divisors: int):
    quotient = 0

    if divisors == (()):
        print(f"{dividend} = {dividend}")
        quotient = dividend

        return quotient
    
    else:
        quotient = dividend
        for divisor in divisors:
            print(f"{quotient} / {divisor}", end="")
            quotient /= divisor
            print(f" = {quotient}", end="\n")

        return quotient
    
def modulus(dividend: int, divisor: int, /):
    remainder = dividend % divisor

    print(f"{dividend} % {divisor} = {dividend // divisor} Remainder = {remainder}")

    return remainder