#madlibs
name=input("Name : ") 
food=input("Put a food?: ")
verb1=input("Verb?: ")
verb2=input("Verb?: ")
verb3=input("verb?: ")
noun=input("Noun? :")
number=input("Number? :")
cg=input("Celebrity Guest? :")
adjective=input("Adjective? ") 

Madlib = f"It was {food} day, and {name} was super {adjective} for lunch. But when she went outside to eat, a {noun} stole her {food}! {name} chased the {noun} all over school. She {verb1}, {verb2}, and {verb3} through the playground. Then she tripped on her {noun} and the {noun} escaped! Luckily, {name}s friends were willing to share their {food} with her"

print(Madlib)

#odd/even?
num=int(input("Number: "))

if (num%2) == 0:
    print("even")
else:
    print("odd")
