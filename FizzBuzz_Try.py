#Welcome to the Game FizzBuzz
#Hope you have fun and like playing the Game.

for x in range(1,101):
    if (x % 3 == 0 and x % 5 == 0):
        print("FizzBuzz")
    elif (x % 3 == 0):
        print("Fizz")
    elif (x % 5 == 0 ):
        print("Buzz")
    else:
        print(x)


##########Variante 2 :


def FizzBuzz(input):
    if (input % 3 == 0 and input % 5 == 0):
        return "FizzBuzz"
    elif (input % 3 == 0):
        return "Fizz"
    elif (input % 5 == 0 ):
        return "Buzz"
    else:
       return input 
print(FizzBuzz(3))

#Ende