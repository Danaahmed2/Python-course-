

##4

apple = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]

x = 0

for i in apple:
    x+= i

capacity.sort(reverse=True)

sumBox = 0
numBox = 0

for i in capacity:
    sumBox +=i
    numBox += 1

    if sumBox >= x:
        print(numBox)
        break