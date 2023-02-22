#SPS 2471: STATISTICAL COMPUTING III (PA 105)
#CAT I Python SOLUTIONS
#Q1
import math

mylist = range(3,45,3)
for i in mylist:
    if (i==6 or i==15):
        continue
    elif i==21:
        break
    print(i,end=" ")

#3 9 12 18

#Q2
Myvals = {
    'Ten':10,
    'Twenty':20,
    'Thirty':30
}
print(Myvals)

#{'Ten': 10, 'Twenty': 20, 'Thirty': 30}

#Q3
#i
for i in 'Python':
    print(i,end='')
#Python
#ii
x = 'Python'
for i in range(len(x)):
    print(x[i],end='')
#Python
#Q4
def quad(a,b,c):
    dis = b**2 - 4*a*c
    if dis < 0:
        print('\nThe the discriminant is',dis,' hence the roots are complex.')
    elif dis==0:
        ans = -b/(2*a)
        print('\nThe discriminant is zero hence the roots are equal.')
        print('\nThe roots are x1 = x2 = ',ans)
    else:
        ans1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        ans2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
        print('\nRoots are: x1 =',ans1,' and x2 = ',ans2,'\n')
quad(1,-3,2)

#Q5
#Lists are mutable (can add elements)
#Tuples are immutable (cant add elements)
mylist = [25,30,24,26]
mytuple = (25,30,24,26)

#Q6
def tax():
    salary = int(input('Enter your salary in KSh.: '))
    if salary > 20000:
        tax_amt = salary * 0.15
        net_sal = salary - tax_amt
        print('Your Gross Salary: ksh.',salary)
        print('Taxed at 15% to have tax amount of Ksh.',tax_amt)
        print('Hence your Net salary is ksh.',net_sal)
    elif salary >= 10000 and salary <= 20000:
        tax_amt = salary * 0.10
        net_sal = salary - tax_amt
        print('Your Gross Salary: ksh.',salary)
        print('Taxed at 10% to have tax amount of Ksh.',tax_amt)
        print('Hence your Net salary is ksh.',net_sal)
    else:
        tax_amt = salary * 0
        net_sal = salary - tax_amt
        print('Your Gross Salary: ksh.',salary)
        print('Taxed at 0% to have tax amount of Ksh.',tax_amt)
        print('Hence your Net salary is ksh.',net_sal)
tax()
# Enter your salary in KSh.: 25000
# Your Gross Salary: ksh. 25000
# Taxed at 15% to have tax amount of Ksh. 3750.0
# Hence your Net salary is ksh. 21250.0
#Q7
for i in range(2,10):
    for j in range(2,14,4):
        if i%3==0 and j%2==0:
            print(i,"*",j,"=",i*j)
    print('\n')

# 3 * 2 = 6
# 3 * 6 = 18
# 3 * 10 = 30
#
# 6 * 2 = 12
# 6 * 6 = 36
# 6 * 10 = 60
#
# 9 * 2 = 18
# 9 * 6 = 54
# 9 * 10 = 90

#Q8
import pandas as pd
mydata ={'Name':["James","Peter","John","Mercy","Jane"],
         'University':["Nairobi","Kirinyaga","Chuka","Moi","JKUAT"],
         'Class_Awarded':["First","Pass","Second Lower","Pass","Second Upper"],
         'Year_Awarded':[2017,2019,2018,2021,2018]}
mydata = pd.DataFrame(mydata)
print(mydata)

#     Name University Class_Awarded  Year_Awarded
# 0  James    Nairobi         First          2017
# 1  Peter  Kirinyaga          Pass          2019
# 2   John      Chuka  Second Lower          2018
# 3  Mercy        Moi          Pass          2021
# 4   Jane      JKUAT  Second Upper          2018