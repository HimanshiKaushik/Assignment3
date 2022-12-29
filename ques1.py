count = 0
MyString = str(input("ENTER YOUR STRING:"))
MyChar = str(input("ENTER THE WORD YOU WANT TO COUNT:"))

for i in MyString:
    if i==MyChar:
        count +=1

print(count)