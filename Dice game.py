import random
import dicestruc as d

a = input("Press any key to start game : ")
print("# Dice games: ")
print(random.choice(d.list))
for i in range(20):
  que = str(input('''If you have repeat for press \"1\"  
If you have quit for \"0\" : '''))

  if(que == "0" ):
    quit()
    
  elif (que =="1" ):
    print(random.choice(d.list)) 

  else:
    print("You type wrong instrection, Please try again")