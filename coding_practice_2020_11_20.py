# 1. 
color = input("What is your favorite color? ")
print(color + "?! No why, that's my favourite colour too!")
print()

# 2.
cans = int(input("How many cans come in a pack? "))
packs = int(input("How many packs are there? "))
print("There are " + str(cans * packs) + " cans in total.")
print()

# 3.
length = int(input("Please enter the length in cm "))
width = int(input("Please enter the width in cm "))
height = int(input("Please enter the height in cm "))
print("The volume of the rectangular prism is " + str(length*width*height) + "cm cubed.")
print()

# 4. 
answer = input("Do you just join a google meet and mute the teacher? ")
if(answer == "yes" or "Yes"):
    print("That's probably not a good idea")
elif(answer == "no" or "No"):
    print("Ok. Good.")

