name = input("What's your name friend?  ")

def greeting(name):
    print("Hello {}".format(name))

greeting(name)

answer = input("Would you like to play a game? Y/N  ")

def decision(answer):
    if answer.lower() == "y":
        print("Delightful")
    elif answer.lower() == "n":
        print("Shame. Come back later")
    else:
        print("Please choose an option")


decision(answer)


# Apparantly arrays are called lists in Python
# And hashes are called dictionaries
