"""
Write a function that takes an array of words and smashes them together into a sentence 
and returns the sentence. You can ignore any need to sanitize words or 
add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the 
beginning or the end of the sentence!
"""

prueba = ["hello", "world", "this", "is", "great"]

longitud = len(prueba)
contador = 0
for i in prueba:

    if contador == 0:
        print('"', end = "")
        print(i, end = "")
        print(" ", end = "")
    elif contador == (longitud-1):
        print(i, end="")
    else:
        print(i, end = "")
        print(" ", end = "")

    contador += 1
    
print('"')