#takes a string of names separated by a space
#splits the string into a list of names
#prints to the console "Hello name" for each name


# this is an easier way of grabbing input, but less explicit
# names = input("Some names please ")
print("Some names please ")
names = input()

def hello_names(names):
    list_names = names.split()
    for name in list_names:
        print("Hello," + " " + name)

hello_names(names)
