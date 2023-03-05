import random

option = int(input("Coding for 1 or decoding for 2 >> "))
word = str(input("Enter the word >> "))

words = word.split()
# print(words)

if option == '1':
    new_res = []
    for i in words:
        if len(i) >= 3:
            first = ['cgd','dth','edb','fky']
            second = ['wdh','r;t','gse','ugh']
            res = random.choice(first) + i[1:] + i[0] + random.choice(second)
            new_res.append(res)
        else:
            new_res.append(i[::-1])
    
    print(" ".join(new_res))

else:
    new_res = []
    for i in words:
        if(len(i)>=3): 
            res = i[3:-3]
            res = res[-1] + res[:-1]
            new_res.append(res)
        else:
            new_res.append(i[::-1])
    print(" ".join(new_res) + '.')

    
        