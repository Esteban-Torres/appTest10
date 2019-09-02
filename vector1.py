fruits = ["Apple","Banana","Orange"]

print("El primer valor es: ", fruits[0])
print("El ultimo valor es: ", fruits[2])

N = []
i = 1

while i <= 10 :
    print("Press number ", i,": ")
    X = int(input())
    N.append(X)
    i = i + 1

'''Show list'''
i = 0
while i < 10:
    print("El valor en la posición ",i,"es ",N[i])
    i = i + 1