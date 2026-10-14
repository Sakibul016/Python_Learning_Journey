age=23
driving_license = True
car = False

if age>=18:
    if driving_license == True:
        if car == True:
            print("You can drive Bro")
        else:
            print("Sorry, You don't have a Car")
    else:
        print("You need a driving license.")
else:
    print("You are too young.")