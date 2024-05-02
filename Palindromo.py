# Reconocer si una palabra es palíndromo
def palindromo(palabra):
    if palabra == palabra[::-1]:
        return "Es palindromo"
    else:
        return "No es palindromo"

palabra = input("Introduce una palabra: ")
print(palindromo(palabra))