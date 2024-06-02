#numeric Literals
a = 0b1010
b = 100
c = 0o512  #do google for better understanding
d = 0x12c
print(a, b, c, d)

float_1 = 10.5
float_2 = 1.5e2
float_3 = 1.5e-3
print(float_1, float_2, float_3)


#string Literals
string = 'python'
strings = "python"
multi_string = """this is multiline string with more than one line code"""
unicode = u"\U0001f600\U0001F606\U0001F923"  # string ke pahele 'u' laga padega
char = "B"
raw_str = r"raw \n string"
print(string)
print(strings)
print(char)
print(multi_string)
print(unicode)
print(raw_str)

#boolean literals
# In this literals the python consider "true" boolean as 1 and "false" boolean as a 0 for.eg

a = True+9    #True=1
b = False*12  #false=0
print("a:", a)
print("b:", b)