import string
# We can use the string.ascii_uppercase method to store all uppercase characters in a variable
az_upper = string.ascii_uppercase
# after the execution 
# az_Upper will be equal to 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

try:
    fhand = open('article1.txt', 'r')
except:
    print('File not found')
    exit()

text = fhand.read()

# Continue with your exercise...


