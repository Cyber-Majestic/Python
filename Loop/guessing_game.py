from random import randint
guessNumber=int(input("Enter your guess number:"))
randomNumber=randint(1,5)
if randomNumber==guessNumber:
    print("You've won.")
else:
    print("You've lost.") 
    print("The random number was:",end=f"{randomNumber}")