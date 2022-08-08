print("Ingrese un núumero")
num=int(input())
while(num>0):
    resto=int(num%10)
    print("Al dividir",num,"por 10 el resto es: ",resto)
    num//=10
