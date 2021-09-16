print("\n\n\t\t'Calculadora de montos'\n")
print("\nEscribe el monto para que saber la cantidad de billetes de 500,200,100,50,20 y de monedas de 10,5,2,1\n")
monto_inicial=int(input("Monto: "))
billete_500=0
billete_200=0
billete_100=0
billete_50=0
billete_20=0
monedas_10=0
monedas_5=0
monedas_2=0
monedas_1=0



while monto_inicial!=0:

    if(monto_inicial>=500):
        billete_500=int(monto_inicial/500)
        monto_inicial%=500
    elif(monto_inicial>=200):
        billete_200=int(monto_inicial/200)
        monto_inicial%=200
    elif(monto_inicial>=100):
        billete_100=int(monto_inicial/100)
        monto_inicial%=100
    elif(monto_inicial>=50):
        billete_50=int(monto_inicial/50)
        monto_inicial%=50
    elif(monto_inicial>=20):
        billete_20=int(monto_inicial/20)
        monto_inicial%=20
    elif(monto_inicial>=10):
        monedas_10=int(monto_inicial/10)
        monto_inicial%=10
    elif(monto_inicial>=5):
        monedas_5=int(monto_inicial/5)
        monto_inicial%=5
    elif(monto_inicial>=2):
        monedas_2=int(monto_inicial/2)
        monto_inicial%=2
    elif(monto_inicial>=1):
        monedas_1=int(monto_inicial/1)
        monto_inicial%=1

print(f'\n\tCantidad: {monto_inicial}  \n\tbilletes de 500: {billete_500}\n\tBilletes de 200: {billete_200}\n\tBilletes de 100: {billete_100}\n\tBilletes de 50: {billete_50}\n\tBilletes de 20: {billete_20}\n\tMonedas de 10: {monedas_10}\n\tMonedas de 5: {monedas_5}\n\tBilletes de 2: {monedas_2}\n\tMonedas de 1: {monedas_1}')

print("Cantidad:",billete_100)
