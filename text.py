
def Store():
    print ("You've just entered To the Egy Store ")
    print ("Do you take the Movie on the CD or the DVD?")
    answer = input("Type CD or DVD and hit 'Enter'.").lower()
    if answer == "CD" or answer == "cd" or answer == "Cd":
        print ("This is the Your CD ")
    elif answer == "DVD" or answer == "dvd" or answer == "Dvd":
        print ("Of course this is the DVD")
    else:
        print ("You didn't pick CD or DVD! Try again.")
        Store()

Store()
print ("FFFFaaaayez ")
print ("FFFFaaaayez ")
