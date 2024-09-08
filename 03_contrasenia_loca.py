
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

        for i in contrasenia_asig[0]:
            print("")
            print("Provemos que funcione")
            print("")

            test_3 = input("Ingresa tu contraseña por favor: ").upper()

            if test_3 == "JUPITER":
                print("")
                print("BIENVENIDO")
                exit()
    


elif nivel_seguridad == "MEDIA":
    print("")

    print("Elige un bloque de preguntas para formar tu contraseña")
    print("")

    print("1) Sobre ti")
    print("2) Sobre tu familia")
    print("3) Sobre tu mascota")
    print("4) sabre tu hobbie")

    contrasenia_asig_1 = [] 

    bloque_q = input("¿Con qué conjunto de preguntas te gustaría crear tu contraseña?: ")

    if bloque_q == "1":
        print("")
        print("Ingresa la información necesaria:")

        fecha = input("Ingresa (con números)el día y el mes de una fecha importante (agrega un cero cuándo solo exista un digito): ").upper()
        artista_fav = input("Ingresa el nombre de tu artista favorito: ").upper()
        totem =input("Ingresa el nombre del animal que te representa: ").upper()
        apellido_abuela = input("Ingresa el segundo apellido de tu abuela materna: ").upper()

        contrasenia = fecha + artista_fav + totem + apellido_abuela
        contrasenia_asig_1.append(contrasenia)

        for i in contrasenia_asig_1:
            print("")
            print(f"Tu contraseña es {i}")

            print("Provemos que funcione")

            ingresar = i.upper()

            test_media_1 = input("Por favor ingresa tu contraseña: ").upper()

            if test_media_1 == ingresar:
                print("BIENVENIDO")


    elif bloque_q == "2":
        print("")
        print("Ingresa la información necesaria:")

        n_familiares = input("Ingresa el numero de hermanos y el numero de primos que tienes (agrega un cero a la derecha si se tratan de cifras de un digito): ").upper()
        carinio_abue = input("Ingresa el nombre de cariño que le dabas a uno d etus abuelos: ").upper()
        ciudad_nac =input("Ingresa las iniciales del hospital donde nacio tu mama: ").upper()
        in_pater = input("Ingresa las iniciales de tus padres: ").upper()
        n_suerte = input("Ingresa tu numero de la suerte: ")

        contrasenia = n_familiares + carinio_abue + ciudad_nac + in_pater + n_suerte
        contrasenia_asig_1.append(contrasenia)

        for i in contrasenia_asig_1:
            print("")
            print(f"Tu contraseña es {i}")

            print("Provemos que funcione")

            ingresar = i.upper()

            test_media_2 = input("Por favor ingresa tu contraseña: ").upper()

            if test_media_2 == ingresar:
                print("BIENVENIDO")

    
    elif bloque_q == "3":
        print("")
        print("Ingresa la información necesaria:")

        edad_mascota = input("Ingresa la edad en meses de tu mascota favorita (agrega un cero a la derecha si se trata de una cifra de un digito): ").upper()
        nombre_mascota = input("Ingresa el nombre de tu mascota favorita: ").upper()
        especie_mascota =input("Ingresa la familia zoologica a la que pertenece tu mascota: ").upper()
        cuidador = input("Ingresa el nombre de la persona que suele cuidarlo: ").upper()
        n_placa = input("Ingresa los dos últimos digitos de la placa de tu mascota: ")

        contrasenia = edad_mascota + nombre_mascota + especie_mascota + cuidador + n_placa
        contrasenia_asig_1.append(contrasenia)

        for i in contrasenia_asig_1:
            print("")
            print(f"Tu contraseña es {i}")

            print("Provemos que funcione")

            ingresar = i.upper()

            test_media_3 = input("Por favor ingresa tu contraseña: ").upper()

            if test_media_3 == ingresar:
                print("BIENVENIDO")

    
    elif bloque_q == "4":
        print("")
        print("Ingresa la información necesaria:")

        tu_hobbie = input("Ingresa tu hobbie favorito): ").upper()
        record = input("Ingresa el mejor record en este hobbie, pueden ser mayores puntos obtenidos o racha de practica, si es un cifra de un digito agrega un cero a la derecha: ").upper()
        objeto_p =input("Ingresa el elemento principal para poder realizar este hobbie: ").upper()
        rival = input("Ingresa el nombre de tu rival principal sea equipo o persona: ").upper()
        tiempo_pract = input("Ingresa en meses el tiempo que llevas practicanto este hobbie: ")

        contrasenia = tu_hobbie + record + objeto_p + rival + tiempo_pract
        contrasenia_asig_1.append(contrasenia)

        for i in contrasenia_asig_1:
            print("")
            print(f"Tu contraseña es {i}")

            print("Provemos que funcione")

            ingresar = i.upper()

            test_media_4 = input("Por favor ingresa tu contraseña: ").upper()

            if test_media_4 == ingresar:
                print("BIENVENIDO")

elif nivel_seguridad == "ALTA":
    print("")

    print("Elige un bloque de preguntas para formar tu contraseña")
    print("")

    print("1) Sobre ti")
    print("2) Sobre tu familia")
    print("3) Sobre tu mascota")
    print("4) sabre tu hobbie")

    contrasenia_asig_2 = [] 

    bloque_q = input("¿Con qué conjunto de preguntas te gustaría crear tu contraseña?: ")

    if bloque_q == "1":
        print("")
        print("Ingresa la información necesaria:")

        fecha = input("Ingresa (con números)el día y el mes de una fecha importante (agrega un cero cuándo solo exista un digito): ").upper()
        artista_fav = input("Ingresa el nombre de tu artista favorito: ").upper()
        totem =input("Ingresa el nombre del animal que te representa: ").upper()
        apellido_abuela = input("Ingresa el segundo apellido de tu abuela materna: ").upper()

        l_artista_fav = []
        l_totem = []
        l_apellido_abuela = []
        l_random = []

        if artista_fav:
            l_artista_fav.append(artista_fav)
            print(l_artista_fav)

        if totem:
            l_totem.append(totem)
            print(l_totem)

        if apellido_abuela:
            l_apellido_abuela.append(apellido_abuela)
            print(l_apellido_abuela)


""""
        contrasenia = fecha + artista_fav + totem + apellido_abuela
        contrasenia_asig_2.append(contrasenia)

        for i in contrasenia_asig_2:
            print("")
            print(f"Tu contraseña es {i}")

            print("Provemos que funcione")

            ingresar = i.upper()

            test_media_1 = input("Por favor ingresa tu contraseña: ").upper()

            if test_media_1 == ingresar:
                print("BIENVENIDO")
"""
