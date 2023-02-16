#Loops Continued
import datetime

for j in range(1,5):
    for i in range(1,16):
        if (i%3==0 and j%2==0):
            print(i,"*",j,"=",i*j)
    print("\n")

country={
    "Kenya": 50,
    "Uganda": 12,
    "Tanzania":80
}
for index,value in country.items():
    print(index," has ",value,"Million Pop")