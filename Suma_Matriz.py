import random

Mat1=[]
Mat2=[]
MatTotal=[]

print("Ingrese las dimensiones de las matrices (Ambas tendran las mismas medidas)")
x=int(input("Largo: "))
y=int(input("Alto: "))

for i in range (0, x):
    Mat1.append([])
    Mat2.append([])
    MatTotal.append([])
    for j in range (0, y):
        Mat1[i].append(random.randint(1,1000))
        Mat2[i].append(random.randint(1,1000))
        MatTotal[i].append(Mat1[i][j]+Mat2[i][j])

for i in range (0,x):
    print(MatTotal[i])