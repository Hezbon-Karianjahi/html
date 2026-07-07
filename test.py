name=input("what is your name?: ")
email=input("what is your email?: ")
# print(f'{name} is {age} years old')
age=int(input("What is your age?: "))
if age<=29:
    print("Not qualified for party")
else:
    print("qualified")
answer=input("Do you want to play game?: ")
if answer.lower()=='yes':
    print("Welcome we have fun!!")
else:
    quit()
question=input("What is the full meaning of FIY?: ")
if question=="For your information":
    print("correct")
else:
    print(incorrect)
question=input("What is the full meaning of IKR?: ")
if question=="I know right?":
    print("correct")
else:
    print(incorrect)
question=input("What is the full meaning of IDK?: ")
if question=="I don't know":
    print("correct")
else:
    print(incorrect)
question=input("What is the full meaning of ASAP?: ")
if question=="As soon as possible":
    print("correct")
else:
    print(incorrect)
print("congratulations, you are through with questions!!")

