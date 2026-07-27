#1
word = input("Enter a word: ")

if word == word[::-1]:
    print("True")
else:
    print("False")


#2


list1 = [1, 2, 3]
list2 = [4, 5, 6]

res = list1+list2
print(res)


#3

names = ["Ali", "Ahmed", "Eman", "Mahmoud", "Aya", "Sara", "dana"]
res = {}
for name in names:
    first = name[0]

    if first in res:
        res[first].append(name)
    else:
        res[first] = [name]

print(res)


#4
name = input("Enter your name: ")

while name == "":
    print("Invalid name")
    name = input("Enter your name: ")

email = input("Enter your email: ")

while "@" not in email or "." not in email:
    print("Invalid email")
    email = input("Enter your email: ")

print("Name:", name)
print("Email:", email)

