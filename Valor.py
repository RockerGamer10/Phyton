print ("Ingrese un número")
valor=int(input())

calc={
    1: 100*valor,
    2: 100**valor,
    3: 100/valor
}

print ("Elija un número entre 1 y 3")
num=int(input())

calculo=calc.get(num,"0")
print(calculo)
