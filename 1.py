
print(
"""Step 1 - Ask for some numbers and add them into a list. 
Step 2 - Check if the input value is actually an number.
Obs: This list is only meant to have 3 values ..."""
)

lista=[]

i=1
while i<4:
        try:
            idade=int(input("\nAge? "))
            if idade != 0:
                lista.append(idade)
                print ("lista: ", lista)
                i += 1
        except:
            print("Valor não aceito")
        
       