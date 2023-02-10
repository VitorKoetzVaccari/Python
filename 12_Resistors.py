
resistor=[]

while True:
    try:
        howmany=int(input("how many resistors? "))
        break
    except:
        print("U have to choose a number ... ")
        print(" ")

while True:
    try:
        i=1 
        while i<=howmany:
            value=int(input("Resistor "+ str(i) + " value: "))
            resistor.append(value)
            print(resistor)
            
            '''if i>1:
                connection=input("series (s) or parallel (p)?")
                if connection == "s":
                    print("series")
                    break
                else:
                    print("erered ")
                    break
            else:
                continue
'''
    except:
        print("Value not accepted ")               
             
       

        