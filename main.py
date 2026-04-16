#Main file where the system will run stuff

#insert BULLSHIT

import BasicOperations

def main():
    operator = input("Please input what operator you would like to use(Example: Addition):\n") #Allows selection of operator
    operator = operator.lower()
    print()

    if operator == "addition":
        quantity = int(input("How many numbers would you like to add?:\n"))
        print()
        if quantity < 1:
            print("Please restart the program!")
        
        elif quantity == 1:
            addend = int(input("Please input a number:\n"))
            print()
            BasicOperations.add(addend)
        else:
            counter = 1
            addends = []
            addend = int(input("Please input a number:\n"))
            addends.append(addend)
            while counter < quantity:
                addend = int(input("Please input another number:\n"))
                addends.append(addend)

                counter += 1

            print()
            BasicOperations.add(*addends)
        

    elif operator == "subtraction":
        quantity = int(input("How many numbers would you like to subtract:\n"))
        print()
        if quantity < 1:
            print("Please restart the program!")
        
        elif quantity == 1:
            minuend = int(input("Please input a number:\n"))
            print()
            BasicOperations.subtract(minuend)
        
        elif quantity == 2:
            minuend = int(input("Please input the minuend:\n"))
            subtrahend = int(input("Please input the subtrahend:\n"))
            print()
            BasicOperations.subtract(minuend, subtrahend)

        else:
            counter = 2
            minuend = int(input("Please input the minuend:\n"))
            subtrahends = []
            subtrahend = int(input("Please input a subtrahend:\n"))
            subtrahends.append(subtrahend)
            while counter < quantity:
                subtrahend = int(input("Please input another subtrahend:\n"))
                subtrahends.append(subtrahend)

                counter += 1

            print()
            BasicOperations.subtract(minuend, *subtrahends)
            


    elif operator == "multiplication":
        quantity = int(input("How many numbers would you like to multiply?:\n"))
        print()

        if quantity < 1:
            print("Please restart the program!")
        
        elif quantity == 1:
            factor = int(input("Please input a number:\n"))
            print()
            BasicOperations.multipy(factor)

        else:
            counter = 1
            factors = []
            factor = int(input("Please input a number:\n"))
            factors.append(factor)
            while counter < quantity:
                factor = int(input("Please input another number:\n"))
                factors.append(factor)

                counter += 1

            print()
            BasicOperations.multipy(*factors)

    elif operator == "division":
        quantity = int(input("How many numbers would you like to divide:\n"))
        print()
        if quantity < 1:
            print("Please restart the program!")
        
        elif quantity == 1:
            dividend = int(input("Please input a number:\n"))
            print()
            BasicOperations.divide(dividend)
        
        elif quantity == 2:
            dividend = int(input("Please input the dividend:\n"))
            divisor = int(input("Please input the divisor:\n"))
            print()
            BasicOperations.divide(dividend, divisor)

        else:
            counter = 2
            dividend = int(input("Please input the dividend:\n"))
            divisors = []
            divisor = int(input("Please input a divisor:\n"))
            divisors.append(divisor)

            while counter < quantity:
                divisor = int(input("Please input another divisor:\n"))
                divisors.append(divisor)

                counter += 1

            print()
            #divisors.reverse()
            print(divisors)
            BasicOperations.divide(dividend, *divisors)

    elif operator == "modulus":
        dividend = int(input("Please input the dividend:\n"))
        divisor = int(input("Please input the divisor:\n"))

        print()
        BasicOperations.modulus(dividend, divisor)

    else:
        print("You inputed an invalid operator, please restart the program!")



if __name__ == "__main__":
    main()