# if else in python
male = True

if male:
    print("You are a male.")

male = False

if male:
    print("You are a male.")
else:
    print("You are not a male.") 

male = False
tall = True

if male:
    print("You are a male.")
elif male or tall:
    print("You are not a male but tall")

male = False
tall = False

if male:
    print("You are a male.")
elif male or tall:
    print("You are not a male but tall")
else:
    print("You are neither a male nor a tall")    


male = True
tall = True

if not male:
    print("You are a male.")
elif male and tall:
    print("You are a male and also tall")
else:
    print("You are neither a male nor a tall")      