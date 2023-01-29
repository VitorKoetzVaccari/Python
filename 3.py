lista=[]

while True:
    try:
        nbr=int(input("choose how many number the list will have"))
        break
    except:
        print("wrong value")


while True:
    i=0
    while i<nbr:
        try:
            x=int(input("choose number"))
            lista.insert(i,x)
            print(lista)
            i+=1
        except:
            print("Try again!")
    break
  
  
  
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
