import random
caracteres = "+-/*!&$#?=@abcdefghijklmñnopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"
longitud = int(input("Cuantos caracteres quieres que tenga?:"))
contraseña = ""

for i in range(longitud):
    contraseña = contraseña + random.choice(caracteres) 
print("La contraseña segura es:", contraseña)
