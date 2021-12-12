#exception= events detected during execution that interrupts flow of a program

try:
    numerator = int(input('Enter a number to divide: '))
    denominator = int(input('Enter a number to divide by: '))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero")
except ValueError as e:
    print(e)
    print("Enter number only plz")
except Exception as e:
    print(e)
    print("Oops! something went wrong :(")
else:
    print(result)
finally:
    print("This will always execute")