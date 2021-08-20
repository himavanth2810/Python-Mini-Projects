import random 

def dice(): 
    total = 120 
    game = "Y" 
 
    while (game == "Y"or game =="y"):
        print (" You have = ", total, "Gold")
        bbet = input("How much do you bet ? : ") 
        bet = int(bbet)  

        while bet > total:
            print("You don't have enough money, Please bet again")
            bbet = input("how much do you bet ?") 
            bet = int(bbet)

        print ("""   \_1_/    \_2_/    \_3_/  """)

        guess= input("Which pot is the stone in ? : ")
        guess=int(guess)

        while guess >3:
            print("It is out of 3 !!")
            guess= input("Which pot is the stone in ? : ")
            guess=int(guess)
        die = random.randint(1,3) 
        print ("It is under pot ", die) 

        if die !=guess: 
            print ("You lose") 
            total-=bet 
        else: 
           print ( "You win") 
           total+=bet*2 

        if total<=0:
            input("Go home you have no more gold left, press enter to escape")
            break       
        game = input("Play again? (Y/N)")   
        game= game.upper()

        if game== "N":                              
            print (" final amount = ", total, "Gold")
            input("Good bye, press enter to escape")

dice()
