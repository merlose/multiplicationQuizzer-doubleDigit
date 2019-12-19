import random

int1 = random.randint(11,99)

int2 = random.randint(11,99)

ans = int1*int2

print ("Whats is",int1,"multiplied by",int2,"?"),

answer = int(input("Your answer:"))
#requires int to define what type the input will be

if answer == ans:
    print("Correct")
else:
    print ("Incorrect.",int1,"*",int2,"=",ans)

print (input("Hit ENTER to end"))