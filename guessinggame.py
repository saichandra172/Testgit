import random
randomNumber = random.randrange(0,20)
print("Random number has been generated")
guessed = False
while guessed==False:
    userInput = int(input("Your guess pleas: "))
    if userInput==randomNumber:
        guessed = True
        print("Well done!")
    elif userInput>20:
        print("Our guess range is between 0 and 20, please try a bit lower")
    elif userInput<0:
        print("Our guess range is between 0 and 20, please try a bit higher")
    elif userInput>randomNumber:
        print("Try one more time, a bit lower")
    elif userInput < randomNumber:
        print("Try one more time, a bit higher")

print("End of program")