#Rock, papers, scissors
import random

#User choice
while True:
    x=input("choose Rock (R), Paper (P) or scissor (S)")
    if x=='r': 
        print("You: Rock")
        break
    elif x=='p':
        print("You: Paper")
        break
    elif x=='s':
        print("You: Scissor")
        break
    else:
        print("value not accepted")

#Computer choice
lista=['r','p','s']
z=random.randint(0,2)
print("Computer: " + lista[z])

#Comparison
if z==x:
    print("Tie")
