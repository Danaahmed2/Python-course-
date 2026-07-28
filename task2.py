
##1

text = input("Enter a string: ")
count=0
for letter in text:
   if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        count = count + 1

print("Number of vowels:", count)   


##2
text = input("Enter a string: ")
for i in range(len(text)):    
        print("The letter 'i' is at index:", i)




##3
inputarray = ["dana" ,"sara","hend","ali","sh"]
max_length = 0

for word in inputarray:
    if len(word) > max_length:
        max_length = len(word)

res= []

for word in inputarray:
    if len(word) == max_length:
        res.append(word)

print(res)


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
    