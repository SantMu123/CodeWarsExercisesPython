"""
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. 
No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.
"""

def Multiply(lista):
    longitud = len(lista)-1
    for i in range(longitud):
        for j in range(i,longitud):
            if lista[i] > lista[j]:
                aux = lista[j]
                lista[j] = lista[i]
                lista[i] = aux   
        
    return lista[0]+ lista[1]


#resultado = Multiply([19, 5, 42, 2, 77])
#resultado = Multiply([4,7,12,5,2,8,10])
#resultado = Multiply([10, 343445353, 3453445, 3453545353453])
resultado = Multiply([4,7,-5,5,2,-25,10])

print(resultado)


