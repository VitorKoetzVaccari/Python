import matplotlib.pyplot as plt

D=[]
Im=[]
O=[0,0]
Y=[0,100]
X=[100,0]

plt.plot(Y,O)
plt.plot(O,X)
i=-10
while i<10:
    y=i**2+i-6
    D.append(i)
    Im.append(y)
    plt.plot(D,Im)
    i+=1

plt.show()