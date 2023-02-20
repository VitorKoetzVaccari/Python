import matplotlib.pyplot as plt

dominio=[]
imagem=[]

i=0
while i<10:
    y=i**2
    dominio.append(i)
    imagem.append(y)
    plt.plot(dominio,imagem)
    i+=1
    
plt.show()