# Portafolio
# Github 
from matplotlib import pyplot as plt

class Fibonacci():
    def __init__(self,iniciales,posicion):
        self.iniciales=iniciales
        self.posicion=posicion

    def agregar(self):
        for i in range(self.posicion-2):
            r = self.iniciales[i]+ self.iniciales[i+1]
            self.iniciales.append(r)
        r=0
        print(self.iniciales)
        return self.iniciales
    def grafica(self):
        return self.agregar()

    
numero_posicion=int(input("Escribe el numero de posicion que deseas obtener de Fibonacci"))
a=Fibonacci([0,1],numero_posicion).grafica()
fig, ax = plt.subplots()
ax.scatter(x = [x for  x in range(len(a))], y =a)
plt.savefig('diagrama-dispersion.png')
plt.show()
