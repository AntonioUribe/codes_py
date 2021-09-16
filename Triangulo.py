print("Triangulo")
class Triangulos():
        
    def triangulo_isosceles(self):
        simbolo="*"
        numero_escalones=int(input("Escribe el numero de Escalones de tu triangulo"))

        #La variable impares soporta hasta 50 escalones de piramide
        impares=[2*x+1 for x in range(50)]
        numero_elementos=impares[numero_escalones-1]

        lista=[]
        for i in range(numero_escalones):
            k=[]
            for j in range(numero_elementos):
                k.append(" ")
            lista.append(k)

        contador=0
        n=int((len(lista[0])-1)/2)

        for i in range(len(lista)):
            for j in range(len(lista[0])):
                lista[i][n-contador:n+contador+1]=[i for i in simbolo*(2*contador+1)]
            contador+=1

        print("\n\n")
        for i in range(len(lista)):
            for j in range(len(lista[0])):
                print(lista[i][j],end="")
            
            print()
    def triangulo_escaleno(self):
        numero_escalones=int(input("Escribe el numero de Escalones de tu triangulo"))
        for i in range(numero_escalones,0,-1):
            print("*"*i)
            
Triangulos().triangulo_isosceles()
Triangulos().triangulo_escaleno()
