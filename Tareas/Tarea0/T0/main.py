print("Bienvenido a DCConecta2")
print("Desea iniciar sesión=1, registrarse=2 o salir del programa=3")
respuesta=input("")
if respuesta=="1":
    print("Ingresar nombre de usuario: ")
    nombre_usuario=input("")
    lista_usuarios=[]
    archivo_nombres=open("usuarios.csv","r")
    lineas = archivo_nombres.readlines()
    for linea in lineas:
        lista_usuarios.append(linea)
    archivo_nombres.close()
    print(lista_usuarios)
    def iniciar_sesión(nombre_usuario):
         pass
if respuesta is not "1" or "2" or "3":
    respuesta=3
