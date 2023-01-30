
"""
Step 1 - Create a list and ask for the user to input some numbers.
Step 2 - Separete them in 2 lists (one for odd number and other for even numbers) automatically.
"""

lista_even=[]
lista_odd=[]

while True:
    try:
        x=int(input("choose a number: "))
        if x%2==0:
            lista_even.append(x)
            print("even lista: ", lista_even )
            print("odd lista: ", lista_odd)
        else:
            lista_odd.append(x)
            print("even lista: ", lista_even )
            print("odd lista: ", lista_odd)
    except:
        print("Invalid number")