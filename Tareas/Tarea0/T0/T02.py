print("Bienvenido a DCConecta2")
respuesta=0
lista_usuarios_registrados=[]
lista_usuarios=[]
lista_contactos=[]
respuesta_chat=0
lista_mensajes=[]
lista_chat=[]
lista_grupos=[]
chat1=0
    ################################
archivo_nombres=open("usuarios.csv", "r")
lineas = archivo_nombres.readlines()
for linea in lineas:
    lista_usuarios.append(linea)
archivo_nombres.close()
    ################################
for i in range(len(lista_usuarios)):
    lista_usuarios[i] = lista_usuarios[i].replace("\n", "")
    ################################
mensajes=open("mensajes.csv", "r")
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
        nombre_usuario1 = input()
        ################################
        if nombre_usuario1 not in lista_usuarios:
            respuesta=0
            print("No existe ese nombre de usuario")
        for i in lista_usuarios:
            if nombre_usuario1==i:
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
            data2=open("usuarios.csv","a")
            data2.write(nombre_a_registrar)
            data2.close()
            respuesta=1
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
            contactos=open("contactos.csv", "r")
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
        for i in range(len(lista_mensajes)):
            lista_mensajes[i]=lista_mensajes[i].replace("\n","")
        ################################
        for i in range(len(lista_mensajes)):
            lista_mensajes[i]=lista_mensajes[i].split(",")
        ################################
        interacciones = []
        for i in range(len(lista_contactos)):
            if nombre_usuario2==lista_contactos[i][0]:
                interacciones.append(lista_contactos[i])
        ################################
        for k in range(len(interacciones)):
            print("[",k+1,"]",interacciones[k][1]) ###interacciones[k][1]= al tipo
        ################################
        opcion=int(input())
        if opcion==0:
            respuesta=0
        else:
            nombre=interacciones[opcion-1][1]
        ################################
            for i in range(len(lista_mensajes)):
                if lista_mensajes[i][0]=="regular" and (nombre_usuario2==lista_mensajes[i][1] or nombre_usuario2==lista_mensajes[i][2]):
                    lista_chat.append(lista_mensajes[i])
            ################################
            print("Estos chats tienes con "+str(nombre))
            for k in range(len(lista_chat)):
                if (nombre_usuario2==lista_chat[k][1] or nombre_usuario2==lista_chat[k][2]) and (nombre==lista_chat[k][1] or nombre==lista_chat[k][2]):
                    if nombre_usuario2==lista_chat[k][1]:
                        print(lista_chat[k][3], lista_chat[k][1], lista_chat[k][4])
                    if nombre_usuario2==lista_chat[k][2]:
                        print(lista_chat[k][3], lista_chat[k][1], lista_chat[k][4])
            mensaje_devuelta=input()

            if mensaje_devuelta=="VOLVER_FRASE":
                respuesta=1
            else:
                a=open("mensajes.csv","a")
                a.write(mensaje_devuelta)
                a.close()
       ################################
        if respuesta_menu=="0":
            respuesta_chat=1
    ################################
        if respuesta_menu=="2":
            print("Por favor ingresar usuario a agregar")
        usuario_agregar=input("")
        for i in range(len(archivo_nombres)):
            if archivo_nombres==usuario_agregar:
                lista_contactos.append(usuario_agregar)
            else:
                print("Opción no valida")
    ################################
    if respuesta_chats=="2":
        ################################
        for i in range(len(lista_mensajes)):
            lista_mensajes[i]=lista_mensajes[i].replace("\n","")
            lista_mensajes[i]=lista_mensajes[i].split(",")
        ################################
        for i in range(len(lista_mensajes)):
            if lista_mensajes[i][0]=="grupo":
                lista_grupos.append(lista_mensajes[i])
        ################################
        for i in range(len(lista_grupos)):
            if nombre_usuario2==lista_grupos[i][1]:
                for k in range(len(lista_grupos)):
                    nombre_grupo=lista_grupos[k][2]
                    print(nombre_grupo)
                    for j in range(len(lista_grupos)):
                        if nombre_grupo==lista_grupos[j][3]:
                            print(lista_grupos[j][3], lista_grupos[j][1], lista_grupos[j][4])




