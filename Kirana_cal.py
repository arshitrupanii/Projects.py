sum = 0
nums = []
print("For Quit Press q :")

while True:
  num = input("Enter shopping Price ₹ :\n₹ ")
  if num != "q":
    sum = sum + float(num)
    nums.append(num)
  else:
    print(f"\nYour total shopping price is ₹ {sum} ")
    break

nums = " ₹\n".join(nums)
print("Transaction :")
for i in range(1):
  print(f"{nums} ₹")