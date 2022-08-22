from distutils.log import error


Mat=[]

size=int(input("Tamaño de la matriz cuadrada: "))

for i in range (0,size):
    Mat.append([])
    for j in range (0,size):
        Mat[i].append(int(input()))

for i in range (0,size):
    Mat.append([])
    for j in range (0,size):
        if (Mat[i][j]!=Mat[j][i]):
            print("Matriz no simetrica!")
            print("ERROR FATAL")
            error=0/0

print("Matriz simetrica!")
for i in range(0,size):
    print(Mat[i])