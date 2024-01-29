"""
https://www.codewars.com/kata/600c18ec9f033b0008d55eec
"""

cantidad = eval(input("Ingrese la cantidad de numeros en reverse que quiere: "))
i = 0
num = 0
while num != cantidad:
    i += 1
    car = str(i)
    if car == car[::-1]:
        print(car, end=",")
        num+=1
        