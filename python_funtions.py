#takes a string of names separated by a space
#splits the string into a list of names
#prints to the console "Hello name" for each name

names = input("Some names please ")

def hello_names(names):
    list_names = names.split()
    for name in list_names:
        print("Hello" + " " + name)

hello_names(names)
