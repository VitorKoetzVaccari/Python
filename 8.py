#sorteio

import random

x=random.randint(0,1000)
print("x = ", str(x))

c=1
while True:
    z=random.randint(0,1000)
    print("try " + str(c) + ": " + str(z))
    c+=1
    if x==z:
        print("try " + str(c) + ": " + str(z))
        break
    else:
        continue
        
            
        


