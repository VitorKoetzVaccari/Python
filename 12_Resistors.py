
resistor=[]

while True:
    try:
        howmany=int(input("how many resistors? "))
        break
    except:
        print("U have to choose a number ... ")
        print(" ")


i=0 
while i<howmany: 
    while True:
        try:
            value=int(input("Resistor "+ str(i+1) + " value: "))
            resistor.append(value)
            print(resistor)
            break
        except:
            print("Value not accepted ")
    while True:
        try:
            if i==0:
                R_eq=resistor[0]
                print("R_Eq: " + str(R_eq))
                i+=1
                break
            else: 
                connection=input("series (s) or parallel (p)?")
                if connection == "s":
                    R_eq=R_eq+value
                    print("R_Eq: " + str(R_eq))
                    i+=1
                    break
                elif connection == "p":
                    R_eq=(R_eq*value)/(R_eq+value)
                    print("R_Eq: " + str(R_eq))
                    i+=1
                    break
                else:
                    print("Try again")
                    continue
        except:
            print("Value not accepted ")
            
    

  