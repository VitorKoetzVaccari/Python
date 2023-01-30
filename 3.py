
"""
Step 1 - Create a list and ask for the user how many items (only numbers) it will have.
Step 2 - Ask for numbers.
Step 3 - Organize those numbers in ascending order.
"""

#Step 1
lista=[]
while True:
    try:
        nbr=int(input("choose how many number the list will have: "))
        break
    except:
        print("wrong value")


#Step 2
while True:
    i=0
    while i<nbr:
        try:
            p=str(i+1)
            x=int(input("choose number " + p + ": "))
            lista.insert(i,x)
            print(lista)
            i+=1
        except:
            print("Try again!")
    break
  
  
#Step 3
a=0
while a<nbr:
    b=0
    while b<nbr:
        if b>a and lista[b]<lista[a]:
            lista.insert(a, lista[b])
            lista.pop(b+1)
            print(lista)
            b+=1
        else:
            print(lista)
            b+=1
    a+=1