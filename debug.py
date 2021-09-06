import random


def generateRandom(upper):
    r = random.randint(1, upper)
    return r


def main():
    run = True
    num1 = generateRandom(10)
    num2 = generateRandom(10)
    result = num1 * num2
    while run:
        ans = input("What is " + str(num1) + " x " + str(num2) + "? ")

        if ans.isdigit():
            if int(ans) == result:
                print("Correct")
            else:
                print("Incorrect")
        else:
            print("Answer must be a positive number, try again")


times = 10

for x in range(times):
    main()
