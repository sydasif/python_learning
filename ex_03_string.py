# 03 String Exercise

print("Network Technician") # string inside " "
print("Network\nTechnician") # \n add new line
print("Network\"Technician") # \" add "
#print("Network"Technician") # error in code
print("Network\Technician") # string

# variable
phrase = "Network Technician"
print(phrase) # will print string
print(phrase + " is cool") # string concatenation

# String function
print(phrase.lower()) # print in lower case
print(phrase.upper()) # print in upper case
print(phrase.isupper()) # check is upper or not
print(phrase.upper().isupper()) # use double function
print(phrase.replace("Technician", "Engineer")) # replace string
print(len(phrase)) # to check length of string
# String index
phrase = "Network Technician"
print(phrase[0]) # N
print(phrase[3]) # w
print(phrase.index('N')) # to check index of string 
print(phrase.index('a'))
print(phrase.index('Technician'))
#print(phrase.index('z')) # error

