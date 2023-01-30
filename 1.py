'''
Step 1 - Ask for some numbers and add them into a list.
Step 2 - Check if the input value is actually an number.
'''

lista=[]

i=1
while i<4:
        try:
            idade=int(input("age of person "))
            print (i)
            if idade != 0:
                lista.append(idade)
                print (lista)
                i += 1
                print (i)
        except:
            print("Valor não aceito")
        
       