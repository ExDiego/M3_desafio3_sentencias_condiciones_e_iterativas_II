from string import ascii_lowercase
import getpass

abc=ascii_lowercase

print(type(abc))
password = getpass.getpass("ingrese la clave ")

contador = 0

for letra in password:
    for caracter in abc:
        contador += 1
        if letra == caracter:
            break

print(f"la palabra se encontró en {contador} iteraciones")