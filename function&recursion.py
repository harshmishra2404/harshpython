def fun():
    print("hello world")

fun()


def add(num1, num2):
    num3 = num1+num2
    return num3
num1, num2 = 5, 23
ans=add(num1,num2)
print(f"the sum of {num1} and {num2} is {ans}")


# def num(num1,num2,num3):
#     sum=num1+num2+num3
#     avg=sum/3
#     return avg
# ans=int(num(2,5,8))
# print("the avg value of three num is ",ans)

# WAP to print the list using function
# marks=[1,2,3,4,5,6,7,8,9,0]
# letter=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"]
#
# def print_len(list):
#     print(len(list))
#
# print_len(marks)
# print_len(letter)

# fruits =["mango","apple","cherry","banana","papaya"]
# vehicals=["ford","toyota","BMW","Ferari","mercedis","Royal royces","porshe"]
# def print_len(list):
#     print(len(list))
#     return print
# print_len(fruits)
# print_len(vehicals)

# WAP to print the elements of a list in a single line(list is the parameter)
# fruits =["mango","apple","cherry","banana","papaya"]
# vehicals=["ford","toyota","BMW","Ferari","mercedis","Royal royces","porshe"]
# def print_len(list):
#     print(len(list))
# def print_list(list):
#     for item in list:
#         print(item, end=" ")
#
# print_list(fruits)
# print()
# print_len(fruits)


# WAF to find the factorial of n
# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact*i
#     print(fact)
#
# cal_fact(7)

# WAF to convert USD to INR
# def cal_currency(USD):
#     INR = USD * 83
#     print("USD=",USD,"INR=",INR)
#
# cal_currency(100)


# WAF to state whether the number is ODD or EVEN in string
# def cal_evenodd(n):
#     if (n%2==0):
#         print("this id EVEN")
#     else:
#         print("this is ODD")
#
# cal_evenodd(7)
# ---------------------------------------------------------------------------->
# RECURSION:
# print n to 1 (backwards)
# ---->
# def show(n):
#     if (n==0):
#         return
#     print(n)
#     show(n-1)
#     return show
# show(12)


# Q.return n!
# def fac(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * fac(n-1)
#
# print(fac(34))

# write a recursive function to calculate the sum of first n natural number
# def sumofnumber(n):
#     if (n==0):
#         return 0
#     return sumofnumber (n-1) + n
#
# sum = sumofnumber(12)
# print(sum)

# write a recursive function to print all element in a list.
# (hint: use list & index as parameter.)

# def print_list(list,idx=0):
#     if(idx==len(list)):
#         return
#     print(list[idx])
#     print_list(list,idx+1)
#
# fruits=["apple","mango","banana","pineapple","litchi"]
# print_list(fruits)





