#Rock, papers, scissors
import random
lista=["Rock","Paper","Scissor",]

#User choice
while True:
    x=input("choose Rock (R), Paper (P) or scissor (S)")
    if x=='r': 
        print("You: "+lista[0])
        n=0
        break
    elif x=='p':
        print("You: "+lista[1])
        n=1
        break
    elif x=='s':
        print("You: "+lista[2])
        n=2
        break
    else:
        print("value not accepted")

#Computer choice
z=random.randint(0,2)
print("Computer: " + lista[z])

#Comparison
if n==z:
    print("Tie")
elif n>z:
    print("You win")
else:
    print("You lost")



        