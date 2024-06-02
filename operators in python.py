#Arithmatic Operator
a=4
b=2
print(a+b) #addition
print(a*b)  # multiplication
print(a-b)  # subtraction
print(a/b)  #division
print(a % b)  #modulos
print(a ** b)  #a to the power of b
print(a//b)   # integer division

#comparision Operator  (TRUE or FALSE)
print(a>b)  #less than
print(a<b)  #greater than
print(a>=b) #greater than equal to
print(a<=b)  #less than equal to
print(a!=b)  #not equal to

#logical operator
x=True
y=False
print(x or y) #  or-->addition of 1 and 0
print(x and y)#  and--->multiplication of 1 and 0
print(not x)# this will print "y" not "x"
print(not y)# this print "x" not "y"


#bitwise operator  (do google for better understanding)
h=2
v=3
print(h&v)
print(h|v)
#010-->2
#110-->3
#010--->2 final ans

#Assingment Operator----> do google for this topic
a=6
x-=4
b+=7
print(a)
print(x)
print(b)

# membership operator
# the membership operators for strings are "in" and "not in".
# These operators allow you to check the presence or absence of a substring within a given string.
# They return a boolean value - True if the substring is present, and False otherwise.
geeks ="geeks for Geeks"
print("e" in geeks)

list1 = [1, 2, 3, 4, 5]
print(9 in list1)

#syntax-----> print(" " in " ")


#  Identity Operators:-Identity operators are used to compare the objects,
#  not if they are equal, but if they are actually the same object, with
#  the same memory location

# is:- returns true if both variable are the same object
# e.g:- x is y
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

# is not:- returns true if both variable are not the same object
# x is not y
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)
# returns False because z is the same object as x
print(x is not y)
# returns True because x is not the same object as y, even if they have the same content
print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y