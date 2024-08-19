
fecha = input("Ingresa (con números)el día y el mes de una fecha importante: ").upper()
fruta_favorita = input("Ingresa el nombre de tu fruta favorita: ").upper()
nombre_mascota =input("Ingresa el nombre de tu mascota favorita: ").upper()
apellido_abuela = input("Ingresa el apellido de tu abuela materna: ").upper()

contrasenia = fecha + fruta_favorita + nombre_mascota + apellido_abuela

ingresar = input("Ingresa la contraseña: ").upper()

if ingresar == contrasenia:
    print("Bienvenido")