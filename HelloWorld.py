# x=1
# y=10.0
# z=1111j

# print(type(x))
# print(type(y))
# print(type(z))


# print("hello")
# print('hello')
# print("hello"=='hello')
# a="""hi this is ashu
# ok this is  working"""
# print(a)

# #####################################

# a = "hello my name is ashu ,how are you"
#    01234567890123456789012345678901234

# for i in a:
#     print(i,end='')
# print()

# hello my n
# print(len(a))

# myLife="""yo bye"""
# print("hi" not in myLife)

# boolean
# can be either true or false
# a=100
# b=100
# print(a==b)


# operators

# a=10
# b=6
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b)
# print(a//b)

# w1='program'
# w2='program'

# print(w1 is w2)

# a=257
# b=2555
# print(a is b)
# print(id(a))
# print(id(b))

# starting out with functions
# def welcome():
#     print("welcome to my code ,hope you learning some great stuff")

# welcome()


##########################

# a=10

# # print(a)
# def function1():
#     a=100
#     def function2():
#         a=1001
#         print("here")
#         print(a)
#     function2()
#     print(a)
# function1()
# # print(a)

#lambda function

# x = lambda a:a*a

# print(x(2))


#############################

#learned sets,tuples and lists
#lists: []
#sets:  {}
#tuples:()

#lists are mutable
#tuples are immutable so fast to traverse
#sets do not retain order and repition is not allowed

########input is a string , so i type converted it######
# y=int(input("hello , enter your age"))
# if(y==1):
#     print("wow")




#####################################
#string formatting
#####################################

# string = {"name":"ashu","age":21}
# # print("hi this is " + string["name"] + " I am " + str(string["age"]))
# sentence ="hi my name is {} and I am {} years old".format(string["name"],string["age"])
# print(sentence)

#####################################
#classes and objects#
#####################################

# class Person:
#     x=7
# obj1 = Person()
# obj1.x=5
# print(obj1.x)
# print(Person.x)

# class Student:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
# stud1 = Student ("adi","ashu")
# print(stud1.fname , stud1.lname)

####inheritance ####
# class Parent:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def print_name(self):
#         print(self.fname,self.lname) #we are using it for printing 


# class Children(Parent): #we are passing the class as parameter
#     pass
# x= Children ("hello" , "bunny") 
# x.print_name()

##########################################################
#json#
##########################################################


# import json
# x = '{"name":"ashu","age":"21","city":"noida"}'
# y=json.loads(x) #converts json to python
# print(y["city"])



