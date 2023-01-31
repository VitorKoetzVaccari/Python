# Fibonacci sequence (n first numbers)

lista=[]

while True:
    try:
        nmb=int(input("how many numbers? "))
        break
    except:
        print("value not accepted")

i=0
while i<nmb:
    if i==0 or i==1:
        lista.append(1)
        print(lista)
        i+=1
    else:
        lista.append(lista[i-1]+lista[i-2])
        print(lista)
        i+=1
