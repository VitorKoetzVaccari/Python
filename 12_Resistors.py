
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
            
            if i==1:
                i+=1  
            else: 
                connection=input("series (s) or parallel (p)?")
                if connection == "s":
                    print(sum(resistor))
                    i+=1
                elif connection == "p":
                    print("parallel")
                    i+=1
                else:
                    print("wrong value")
                    resistor.pop(i)
                    continue
                    
        break
    except:
        print("Value not accepted ")               
             
       

        