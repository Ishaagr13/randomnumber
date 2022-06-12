import random 
secret = random.randint(1,100)
guess = secret+1
while secret!=guess:
    guess = int(input("enter a no between 1 to 100: "))
    if(guess<=0):
        print("better luck ,next time !:")
        break
    if(guess>secret):
        print("number too large:")
    elif(guess<secret):
        print("number too small:")
    else:
        print("congratulation you are  right!")
