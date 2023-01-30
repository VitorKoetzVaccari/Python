
"""
Step 1 - Create a list and ask for the user to input some numbers.
Step 2 - Organize those numbers in ascending order as soon as they are added to the list.
"""

lista=[]

while True:
    try:
        z=int(input("Choose a number: "))
        lista.append(z) 
        a=0
        while a<len(lista):
            b=0
            while b<len(lista):
                if lista[b]<lista[a] and b>a:
                    lista.insert(a,lista[b])
                    lista.pop(b+1)
                    print(lista)
                    b+=1
                else:
                    print(lista)
                    b+=1
            a+=1
    except:
        print("wrong value")


