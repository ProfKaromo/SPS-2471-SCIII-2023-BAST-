#Break and Continue Stattements
mylist = range(1,15)
print(list(mylist))
#Continue Statement
for i in mylist:
    if (i==4 or i==7):
        continue
    print(i,end=" ")

#Break Statement
for i in mylist:
    if i==9:
        break
    print(i,end=" ")

#Break and Continue Statements
for i in mylist:
    if (i==4 or i==7):
        continue
    elif i==9:
        break
    print(i,end=" ")
