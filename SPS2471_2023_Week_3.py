# #Data Structures and their methods
# #Lists
# import pandas
#
# mylist = [1,2,3,5]
# print(mylist)
# print(type(mylist))
# fruits = ["Banana","Apples","Orange","Mango"]
# print(fruits[0])
# #index starts from 0
#
# #Negative indexing
# print(fruits[-2])#second last item
#
# #Python Tuples
# mytuple = ("Kenya","Uganda","Tanzania")
# print(mytuple)
# print(type(mytuple))
# #accessing values in tuples
# print("The first element is ",mytuple[0])
# print("The last element is ",mytuple[-1])
#
# #output a range of values
# mytuple = ("Kenya","Uganda","Tanzania","Sudan","Somalia")
# print(mytuple[2:4])
#
# #Python Dictionary
# mydictinary = {
#     "Grade": 1,
#     "Years": 5,
#     "county":"Nakuru"
# }
# print(mydictinary)
#
# print("She is in class ",mydictinary["Grade"])
#
# #Exchanging values
# mydictinary["Grade"] = 5
#
# print(mydictinary)
#
# #Dataframes
# # importing pandas library
#
import pandas as pd
mydata ={'Reg_no':[6845,4875,9625,4562,3652],
         'Name':["Jane","John","James","Grace","Job"],
         'Age':[21,22,20,21,22],
         'Weight':[54,56,58,65,70],
         'County':["Embu","Kilifi","Meru","Kisumu","Nairobi"]}
df4 = pd.DataFrame(mydata, index=['rank1','rank2','rank3','rank4','rank5'])
print(df4)
print([df4['Age']].mean())
# print(mydata)
#
# # assign data of lists.
# data = {'Name': ['Tom', 'Joseph', 'Krish', 'John'], 'Age': [20, 21, 19, 18]}
#
# # Create DataFrame
# df = pd.DataFrame(data)
#
# # Print the output.
# print(df)
#
# data = [['Alex',10],['Bob',12],['Clarke',13]]
# df = pd.DataFrame(data,columns=['Name','Age'])
# print(df)


import pandas as pd
df = pd.DataFrame()
#print(df)
data1 = [2,5,6,5,5]
data2 = pd.DataFrame(data1)
#print(data2)

mydata = [['Jane',23],['John',20],['Kim',21]]
df2 = pd.DataFrame(mydata,columns=['Name','Age'])
#print(df2)

mydata1 = {'Name':['John','Kin','Jane'],'Age':[23,20,21]}
df3 = pd.DataFrame(mydata1)
#print(df3)
