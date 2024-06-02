# With the while loop we can execute a set of statements as long as a condition is true
# Note: remember to increment i, or else the loop will continue forever
number = int(input("Enter the number:"))
i=1
while i<24:
    print(number*i)
    if i==10:
        break
    i+=1
