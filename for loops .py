# Range Function:-The range() function returns a sequence of numbers,
# starting from 0 by default, and increments by 1 (by default), and ends
# at a specified number.

i1 = list(range(1, 11))  # in this when "i" print then 1 will include but 11 not
# e.g [1,2,3,4,5,6,7,8,9,10]
print(i1)

i2 = list(range(15))
# The range() function defaults to 0 as a starting value
# range(15), which means values from 0 to 14 (but not including 15)
# [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(i2)

i3 = list(range(1, 11, 2))
# The range() function defaults to increment the sequence by 1,
# however it is possible to specify the increment value by
# adding a third parameter: range(1, 11, 2)
# in this list 1 and 11 is for "range" and 2
# is for "Step Range" basically it means there will be a gap of two number between two number
# e.g [1,3,5,7,9]
print(i3)

for i4 in range(0, 11, 2):
    print(i4)
# Increment the sequence with 2 (default is 1):

for i5 in "Mumbai":
    print(i5)

for i6 in [1, 2, 3, 4, 5]:
    print(i6)



# Note:- When to use "for" and "while" loop
# basically when we know about the that how many time will run that loop is "for Loop"
# and in which we don't know that how many time loop will run is called "while loop"