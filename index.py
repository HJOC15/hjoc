from random import randint
x= 1 
y= 500
oportu=10

num= int(input("Numero a ocultar entre 1 y 500"))
while oportu >= 1:
    maquina = int((randint(x,y)))
    aux = int(maquina)
    if(maquina==num):
        print("El nùmero es:" + str(maquina))
        print("He ganado")
        break
    print("El numero es mayor o menor a " + str(maquina))
    ayuda=input()

    if(ayuda=="mayor"):
        x = aux
        oportu=oportu-1
        print(oportu)
    elif (ayuda=="menor"):
            y=aux
            oportu=oportu-1
            print(oportu)
