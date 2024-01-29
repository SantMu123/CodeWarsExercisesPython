producto = eval(input("Ingrese el numero: "))
#can = eval(input("Ingrese la cantidad de numeros para el producto"))

for i in range(1,producto+1):
    for j in range(1,25):
        if (i*j == producto):
            print(f"({i},{j})", end = ",")