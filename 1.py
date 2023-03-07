
print(
"""
Step 1 - Ask for some numbers and add them into a list. 
Step 2 - Check if the input value is actually an number.
Obs: thats an infinite list ...
"""
)

lista=[]

i=1
while i<4:
        try:
            idade=int(input("Age? "))
            if idade != 0:
                lista.append(idade)
                print (lista)
                i += 1
        except:
            print("Valor não aceito")
        
       