import random
import os


def gameStart(rounds):
    Userpoints=0
    Comppoints=0
    r=1

    while rounds-r>=0:
        user = input("whats your choice? r for rock,s for scissors,p for paper:")
        comp = random.choice(['r','s','p'])

        if comp == user:
            print('it is a tie')
        #rules:rock>scissor scissor>paper paper>rock

        elif iswin(user,comp):
            Userpoints+=1
            print(f'you won this round\ncurrent scores user:{Userpoints},computer:{Comppoints}')
        
        else:
            Comppoints+=1
            print(f'you lost this round\ncurrent scores user:{Userpoints},computer:{Comppoints}')
        r=r+1
    
    if(Userpoints>Comppoints):
        print("congrats user is the winner")
        regame = int(input('Would You like to play again \n [0] for yes , [1] for no'))
        if regame== 0:
            os.system('cls||clear')

            print("every round winner get one point\nincase of tie no points")
            rounds = int(input("enter max rounds number to held:"))  

            gameStart(rounds)
        else:
            exit(0)
   
    elif(Userpoints<Comppoints):
        print("User lost the game")
        regame = int(input('Would You like to play again \n [0] for yes , [1] for no'))
        if regame== 0:
            os.system('cls||clear')

            print("every round winner get one points\nincase of tie no points")
            rounds = int(input("enter max rounds number to held:"))

            gameStart(rounds)
        else:
            exit(0)
    
    else:
        print("It is a tie")
        regame = int(input('Would You like to play again \n [0] for yes , [1] for no'))
        if regame== 0:
            os.system('cls||clear')

            print("every round winner get one points\nincase of tie no points")
            rounds = int(input("enter max rounds number to held:"))

            gameStart(rounds)
        else:
            exit(0)

def iswin(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    else:
        return False

print("every round winner get one points\nincase of tie no points")

rounds = int(input("enter max rounds number to held:"))

gameStart(rounds)