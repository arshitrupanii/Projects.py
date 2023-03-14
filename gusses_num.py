import random

num = int(input("Type number: "))

random_num = random.randint(0, num)

gusses = 0

while True:
  gusses += 1
  user = int(input("Enter number: "))
  if random_num > user:
    print("You were below the number!")
  elif random_num < user:
    print("You were above the number!")
  else:
    print("You got it!")
    print(f"You got it in {gusses} attempts")
    quit()