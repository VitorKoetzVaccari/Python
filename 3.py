import time

print("""
Step 1 - Create a list and ask for the user how many items (only numbers) it will have.
Step 2 - Ask for numbers.
Step 3 - Organize those numbers in ascending order.
""")

print("Step 1\n")
lista=[]
while True:
    try:
        nbr=int(input("Choose how many number the list will have: "))
        break
    except:
        print("Dude, u gotta choose an number ... Try again")

print("\nStep 2\n")
while True:
    i=0
    while i<nbr:
        try:
            p=str(i+1)
            x=int(input("Choose number " + p +": "))
            lista.insert(i,x)
            print(lista)
            i+=1
        except:
            print("Try again!")
    break
  
  
print("Step 3")
a=0
while a<nbr:
    b=0
    while b<nbr:
        if b>a and lista[b]<lista[a]:
            lista.insert(a, lista[b])
            lista.pop(b+1)
            b+=1
        else:
            b+=1
    a+=1

print("Step 3\n\n")
print(lista)
time.sleep(200)