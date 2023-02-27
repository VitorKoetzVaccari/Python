import matplotlib.pyplot as plt

D=[]
Im=[]
O=[0,0]
Y=[0,10]
X=[0,4]

plt.plot(X,O)
plt.plot(O,Y)
i=-4
while i<4:
    y=i**2+i
    D.append(i)
    Im.append(y)
    plt.plot(D,Im)
    i+=0.1
    if y==0:
        print(i)
    else:
        continue
print(D)
print(Im)
plt.show()