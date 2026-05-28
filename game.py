print("Welcome to this game")
playing=input("Do you want to play this game?: ")
if playing.lower()=="yes":
    print("Welcome")
else:
    quit()
answer=input("What does the abbreviation CPU stands for?: ")
if answer.lower()== "central processing unit":
    print("Correct")
else:
    print("Incorrect")
answer=input("What does the abbreviation GPU stands for?: ")
if answer.lower()=="graphic processing unit":
    print("Correct")
else:
    print("Incorrect")
answer=input("What does the abbreviation ROM stands for?: ")
if answer.lower()=="read only memory":
    print("Correct")
else:
    print("Incorrect")
answer=input("What does the abbreviation RAM stands for?: ")
if answer.lower()=="random access memory":
    print("Correct")
else:
    print("Incorrect")
answer=input("What does the abbreviation GUI stands for?: ")
if answer.lower()== "graphic user interface":
    print("Correct")
else:
    print("Incorrect")
answer=input("What does the abbreviation VSC stands for?: ")
if answer.lower()== "visual studio code":
    print("Correct")
else:
    print("Incorrect")
answer=input("What does the abbreviation PS stands for?: ")
if answer.lower()== "power supply":
    print("Correct")
else:
    print("Incorrect")
answer=input("What does the abbreviation BIOS stands for?: ")
if answer.lower()== "basic input output system":
    print("Correct")
else:
    print("Incorrect")
answer=input("What does the abbreviation POST stands for?: ")
if answer.lower()== "power on self test":
    print("Correct")
else:
    print("Incorrect")
print("Congratulations, you have finished successfully!!")
name="Hezbon"
def greet():
    print("Hello",name)
greet()
def add_two_numbers(num1,num2):
    print(num1+num2) 
    
add_two_numbers(60,20)