import random

def round(user, comp):
  print("You moves",new[user])
  print("Computer moves",nw[comp],'\n')
  if(user == comp):
    print("The Draw")
  print("You win 😊 ") if user == 1 and comp == 2 else 0
  print("You win 😊 ") if user == 2 and comp == 3 else 0
  print("You win 😊 ") if user == 3 and comp == 1 else 0
  print("You Lose 😔") if user == 3 and comp == 2 else 0
  print("You Lose 😔") if user == 1 and comp == 3 else 0

# Start this 
nw = ["","Snake","water","gun"]
new = ["","Snake","water","gun"]
print("Welcome to play Snake Water Gun :~")
name = input("Enter your name >> ")
print("\nHello,", name.capitalize(), "Let's play")

for i in range(4):
  user = int(input(f"\n{i+1}.Choose Snake, Water, Gun / 1,2,3 >> "))
  comp = random.randint(1,3)
  round(user, comp)

