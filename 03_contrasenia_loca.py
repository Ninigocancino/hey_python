
nivel_seguridad = input("¿Qué tan segura quieres que sea tu contrasenia'? Ingresa una opción (basica/media/alta): ").upper()

if nivel_seguridad == "BASICA":
    print("")
    print("Elige una pregunta clave:")
    print("")
    print("1) es el felino más gande del mundo: ")
    print("2) es el país más grande del mundo: ")
    print("3) es el planeta más grande del sistema solar: ")
    print("")

    ep_clave_01 = input("Elige una opción: ")

    contrasenia_asig = []

    if ep_clave_01 == "1":
        respuesta_p1 = input('nombra el felino más grande del mundo: ').upper()
        if respuesta_p1 == "TIGRE":
            contrasenia_asig.append(respuesta_p1)
        else: 
            print("Respuesta incorrecta")

        for i in contrasenia_asig:
            print(f" Tu contaseña es: {i}")

            print("")
            print("Provemos que funcione")
            print("")

            test_1 = input("Ingresa tu contraseña por favor: ").upper()

            if test_1 == contrasenia_asig[0]:
                print("")
                print("BIENVENIDO")

    elif ep_clave_01 == "2":
        respuesta_p2 = input('nombra el país más grande del mundo: ').upper()
        if respuesta_p2 == "RUSIA":
            contrasenia_asig.append(respuesta_p2)
        else: 
            print("Respuesta incorrecta")

        for i in contrasenia_asig:
            print(f"Tu contraseña es: {i}")

            print("")
            print("Provemos que funcione")
            print("")

            test_2 = input("Ingresa tu contaseña por favor: ").upper()

            if test_2 == contrasenia_asig[0]:
                print("")
                print("BIENVENIDO")


    elif ep_clave_01 == "3":
        respuesta_p3 = input('nombra el planeta más grande del sistema solar: ').upper()
        if respuesta_p3 == "JUPITER":
            contrasenia_asig.append(respuesta_p3)
        else: 
            print("Respuesta incorrecta")
    


elif nivel_seguridad == "MEDIA":
    print("")
    print("Ingresa la información necesaria:")
    fecha = input("Ingresa (con números)el día y el mes de una fecha importante: ").upper()
    fruta_favorita = input("Ingresa el nombre de tu fruta favorita: ").upper()
    nombre_mascota =input("Ingresa el nombre de tu mascota favorita: ").upper()
    apellido_abuela = input("Ingresa el apellido de tu abuela materna: ").upper()

    contrasenia = fecha + fruta_favorita + nombre_mascota + apellido_abuela

    ingresar = input("Ingresa la contraseña: ").upper()

    if ingresar == contrasenia:
        print("Bienvenido")