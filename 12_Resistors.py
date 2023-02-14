
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
        i=0 
        while i<howmany: 
            value=int(input("Resistor "+ str(i+1) + " value: "))
            resistor.append(value)
            print(resistor)
            
            if i==0:
                R_eq=resistor[0]
                print("R_Eq: " + str(R_eq))
                i+=1  
            else: 
                connection=input("series (s) or parallel (p)?")
                if connection == "s":
                    R_eq=R_eq+value
                    print("R_Eq: " + str(R_eq))
                    i+=1
                elif connection == "p":
                    print("parallel")
                    i+=1
                else:
                    print("Try again")
                    resistor.pop(i)
                    continue
    except:
        print("Value not accepted ")
       

        