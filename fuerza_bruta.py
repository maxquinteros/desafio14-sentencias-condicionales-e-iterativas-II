import getpass
from string import ascii_lowercase

contraseña_ingresada = getpass.getpass("Introduce tu contraseña: ")
contraseña_adivinada = ""
letra = ""
intento = 0

for letra in contraseña_ingresada:
        for abc in ascii_lowercase:
            intento += 1
            if letra == abc:
                contraseña_adivinada += abc
                break

if intento == 1:
    print(f"La contraseña fue forzada en {intento} intento")

else:
    print(
        f"La contraseña fue forzada en {intento} intentos"
    )
