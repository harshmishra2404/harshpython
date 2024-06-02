# write a new file "practicefile.txt" using python .
# add the following data in it:
#
# hi everyone
# we are learning file I/O
# Using Java
# programming language Java

# ----->
# with open("practicefile.txt","w") as f:
#      data=f.write("Hi everyone\nwe are learning file I/O\nusing Java\nIn programming language Java")


# WAF that replace all occurrences of "java" with "python" in above file.
#----->
# with open("practicefile.txt", "r") as f:
#      data=f.read()
#      print(data)
#
# new_data = data.replace("Java", "Python")
# print(new_data)
#
# with open("practicefile.txt", "w") as f:
#      f.write(new_data)



# search if the word "learning " exists in the file or not
# ----->
# def check_for_word():
#     word = "python"
#     with open("demofile.txt", "r") as f:
#         data = f.read()
#         if(word in data):
#             print("found")
#         else:
#             print("not found")
#
# check_for_word()

# WAF to find in which line of the file does the word "learning" occour first.
# print(-1) if word not found
# ----->
# def check_for_line():
#     word="programming"
#     data = True
#     line_no = 1
#     with open("demofile.txt", "r") as f:
#         while data:
#             data= f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1
# check_for_line()

# form a file containing number separated by comma,print the count of even number
# ----->
# count = 0
# with open("demofile.txt","r") as f:
#     data= f.read()
#
#     num = data.split(",")
#     for val in num:
#         if(int(val)%2==0):
#             count +=1
#
# print(count)


