#Main file where the system will run stuff
import BasicOperations

def main():
    operator = input("Please input what operator you would like to use(Example: Addition):\n")
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
        pass

    elif operator == "division":
        pass

    elif operator == "modulus":
        pass

    else:
        print("You inputed an invalid operator, please restart the program!")



if __name__ == "__main__":
    main()