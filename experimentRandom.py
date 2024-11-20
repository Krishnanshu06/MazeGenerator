import random
# def rand():
#     iterations = random.
n1 = 0
n2 = 0
n3 = 0
n4 = 0

for i in range(100):
    mylist = ["left","right", "down", "up"]
    lis = [1,2,3,4]
    k = random.choices(lis,weights = [7,4,4,4] , k = 1)
    k = k[0]

    choices = random.choices(mylist ,k = k)
    choicesSet = set(choices)
    l =len(list(choicesSet))

    # print(l)

    if l == 1:
        n1 += 1
    elif l == 2:
        n2 += 1
    elif l == 3:
        n3 += 1
    else:
        n4 += 1

print('No of 1 :' , n1)
print('No of 2 :' , n2)
print('No of 3 :' , n3)
print('No of 4 :' , n4)



# print(k)
# print(choices)
# print(len(list(choicesSet)) ,'   ', list(choicesSet))

