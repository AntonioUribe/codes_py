#Numero romanos de 1-40
class Num_Romano:
    
    def __init__(self,numero,num,romano):
        self.numero = numero
        self.num = num
        self.romano = romano 
        
    
    def __str__(self):

        i=0
        resultado = ""
        while self.numero >0:
            while i<len(self.num):
                if self.numero // self.num[i] !=0:
                    resultado += self.romano[i]
                    self.numero-=self.num[i]
                else:
                    i+=1
        return f'''
            El numero Romano es:  {resultado}
                '''          
#print(Num_Romano(Numero_a_Romano,Lista_numeros,Lista_numeros_Romanos))
print(Num_Romano(4,[40,10, 9, 5, 4,1],["XL","X", "IX", "V", "IV","I"]))
