#Se va comparando cada letra de la contraseña con letras del abcdario
from string import ascii_lowercase
from getpass import getpass

password = getpass("Ingrese su clave: ").lower()
contador = 0

for letra in password:
    for elemento in ascii_lowercase:
        contador = contador + 1
        if letra == elemento:
            break
print("La contraseña fue forzada en: ",contador , "intentos")






