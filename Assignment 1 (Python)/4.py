#Reandom number guesser program
import random

n = random.randint(1,100)

chance = 3
while(chance):
    print("Guess a number")
    num = int(input())
    if(chance != 1):
        if(num == n):
            print('Hola You have guessed the right number!!!!')
        elif(num > n):
            print("You are a little high up. Try guessing a smaller number!")
        else:
            print("You are a little low down. Try guessing a larger number!")
    else:
        if(num == n):   
            print('Hola You have guessed the right number!!!!')
        else:
            print("Sorry you have run out of luck!")
            print("The correct number was {} !".format(n))
    chance -= 1