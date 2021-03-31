print("Bienvenido a DCConecta2")
respuesta=0
lista_usuarios_registrados=[]
lista_usuarios=[]
lista_contactos=[]
respuesta_chat=0
lista_mensajes=[]
    ################################
archivo_nombres=open("../T0/usuarios.csv", "r")
lineas = archivo_nombres.readlines()
for linea in lineas:
    lista_usuarios.append(linea)
archivo_nombres.close()
    ################################
for i in range(len(lista_usuarios)):
    lista_usuarios[i] = lista_usuarios[i].replace("\n", "")
    ################################
mensajes=open("../T0/mensajes.csv", "r")
lineas=mensajes.readlines()
for linea in lineas:
    lista_mensajes.append(linea)
mensajes.close()
while respuesta==0:
    print("[1] Desea iniciar sesión\n[2] Registrarse\n[3] Salir del programa")
    print("Indique su opción")
    respuesta=input("")
    if respuesta=="1":
        print("Ingresar nombre de usuario: ")
        nombre_usuario=input()Q1 V
        ################################
        if nombre_usuario not in lista_usuarios:
            respuesta=0
            print("No existe ese nombre de usuario")
        for i in lista_usuarios:
            if nombre_usuario==i:
                respuesta=1
        ################################
    if respuesta=="2":
        print("Ingrese nombre de usuario a registrar: ")
        nombre_a_registrar=input()
        ################################
        for i in range(len(lista_usuarios)):
            if nombre_a_registrar==lista_usuarios[i]:
                print("Nombre ya ingresado")
                respuesta=0
        ################################
        for i in nombre_a_registrar:
            if i==",":
                print("Nombre no valido")
                respuesta=0
        ################################
        largo_nombre=len(nombre_a_registrar)
        if largo_nombre<3 or largo_nombre>15:
            print("Nombre fuera de rango")
            respuesta=0
        else:
            ##escribir en csv
            pass
        ################################
while respuesta_chat==0:
    print("Menú de contactos\n Selecciona una opción\n [1] Ver contactos\n [2] Ver grupos\n [0] Volver")
    print("Indique su opción")
    respuesta_chats=input("")
    print("Ingrese nombre de usuario: ")
    nombre_usuario2=input("")
    ################################
    if respuesta_chats=="1":
        print("Menú de contactos\n [1] Ver contactos\n [2] Anadir contacto\n [0] Volver")
        respuesta_menu=input("")
        if respuesta_menu=="1":
            contactos=open("../T0/contactos.csv", "r")
            lineas = contactos.readlines()
            for linea in lineas:
                lista_contactos.append(linea)
            contactos.close()
        ################################
            for i in range(len(lista_contactos)):
                lista_contactos[i]=lista_contactos[i].replace("\n","")
        ################################
            for i in range(len(lista_contactos)):
                lista_contactos[i]=lista_contactos[i].split(",")
        ################################
            lista_contactos_usuario = []
            for i in range(0,len(lista_contactos)):
                if lista_contactos[i][0]==nombre_usuario2:
                    lista_contactos_usuario.append(lista_contactos[i][1])
        ################################
            print("Ver contacto\n Selecciona un contacto para ver las conversaciones o presiona 0 para volver al menú")
            for j in range(len(lista_contactos_usuario)):
                print("[",j+1,"]"+" "+lista_contactos_usuario[j])
            print("[ 0 ] Volver")
        ################################
        opcion_chat=input("")
        if opcion_chat=="0":
            respuesta_chat=0
        ################################
        for i in range(len(lista_mensajes)):
            lista_mensajes[i]=lista_mensajes[i].replace("\n","")
            lista_mensajes[i]=lista_mensajes[i].split(",")
        ################################
        lista_chats=[]
        for i in range(len(lista_mensajes)):
            if lista_mensajes[i][0]=="regular":
                lista_chats.append(lista_mensajes[i])
        ################################
        actually_chat=[]
        for i in range(len(lista_chats)):
            if lista_chats[i][1]==nombre_usuario2:
                actually_chat.append(lista_chats[i])
            elif lista_chats[i][2]==nombre_usuario2:
                actually_chat.append(lista_chats[i])
        ################################
        print("Este es tu chat con"+str(lista_contactos_usuario[j]))

    ################################
        #tengo que mostrar los contactos+imprimir el mensaje+0 volver atrás+seleccionar contacto
        #implementar volver

    ################################
  # for i in range(len(lista_mesajes)):
