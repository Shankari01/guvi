player1=input()
player2=input()
if(player1=='scissor' and player2=='paper'):
    print("player 1 won")
elif(player1=='paper' and player2=='rock'):
    print("player 1 won")
elif(player1=='rock' and player2=='scissor'):
    print("player 1 won")
else:
    print("player 2 won")
