print("Ingrese (En orden) A, B, C")
A=int(input())
B=int(input())
C=int(input())

print("De mayor a menor:")
if (A>B):
    if (B>C):
        print(A,B,C)
    else: 
        if (A>C):
            print(A,C,B)
        else: print(C,A,B)
else:
    if (A>C):
        print(B,A,C)
    else:
        if (B>C):
            print(B,C,A)
        else: print(C,B,A)