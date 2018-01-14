tictac={}
moves=("x","o")


def validmoves(tictac,pos):
    if pos in tictac.keys():
        print(" # Not a valid Move...Try Again!! ")
        return 1
    else:
        return 0
    

def play(tictac,steptype,player):
    notvalid=1
    if (len(tictac)==0):
        print(" PLAYER {} , enter the postion of move: ".format(player), end="")
        pos=int(input())
        tictac[pos]=steptype
    else:
        while(notvalid): 
            print(" PLAYER {} , enter the postion of move: ".format(player), end="")
            pos=int(input())
            notvalid=validmoves(tictac,pos)
        tictac[pos]=steptype

        

def wincheck(tictac):
    #horizontal check
    for i in range(1,8,3):
        if tictac.get(i," ")==tictac.get(i+1," ")==tictac.get(i+2," ")!=" " :
            return 1
    #vertical check
    for i in range (1,4) :
        if tictac.get(i," ")==tictac.get(i+3," ")==tictac.get(i+6," ")!=" " :
            return 1
    #Diagnol check
    if tictac.get(1," ")==tictac.get(5," ")==tictac.get(8," ")!=" " :
        return 1
    if tictac.get(3," ")==tictac.get(5," ")==tictac.get(7," ")!=" " :
        return 1
        
        
def displaytictac(tictac):
    for i in range(1,10):
        print("\t",tictac.get(i," "),end="")        
        if i%3!=0 :
            print(" | ", end="")
        else:
            print("\n")

            

def main():
    print("***** TIC TAC TOE GAME *****".center(50))
    print("Instruction:\nPlayer 1 move : x\nPlayer 2 move : o")
    player1= input("Enter player 1 name : ")
    player2= input("Enter player 2 name : ")
    players=[player1,player2]
    print(" Starting Game.........Good Luck!! ".center(75))
    count=1
    while (count<10):
        if(count%2!= 0):
            p=0
        else: p=1
        print(" {}'s turn ".format(players[p]))
        play(tictac,moves[p],p+1)
        displaytictac(tictac)
        
        if (count >=5):
            if(wincheck(tictac)):
              print("\n\n {} WON !!! ".format(players[p]),"\n GAME OVER ")
              break
            
        count=count+1
    if(count==10):
        print (" GAME DRAW !!")
    
if __name__=="__main__" :
    main()
        
    
    
        
            
    
        

