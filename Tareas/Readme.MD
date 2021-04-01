# Tarea 0: DCConecta2

## Consideraciones generales :octocat:

*Mi DCConecta2 funciona bien el menú de inicio, puede registrar, iniciar sesión y salirse de la aplicación.
*Después de registrarse o iniciar sesión entrea all menú de chats y despliega las opciones.
*Del menú de chats se puedden ver los contactos y ver la conversación, además se puede enviar mensajes.
*Ver grupos quedó mal implementado ya que muestra todos los grupos y no solo el que uno pide.
*Los archivos estan bien implementados, pudiendo abrir y sobrescribir en ellos.
*"paramentros.py" no fue ocupado.

### Cosas implementadas y no implementadas :white_check_mark: :x:
*Menú de inicio:
	Requisitos:
		[x] El menú de Inicio contiene todas las opciones pedidas en el enunciado.
	Iniciar sesión:
		[x] El usuario puede iniciar sesión, verificando que el nombre de usuario coincida con los datos del archivo usuarios.csv.
		[x] Si se ingresa un nombre no válido se informa al usuario y se vuelve al Menú de Inicio.
	Registrar usuario:
		[x] Se puede registrar un nuevo usuario, el nombre cumple con los requisitos dados en el enunciado (el usuario no está registrado, largo de [3, 15] sin incluir comas)
		[x] Si se ingresa un nombre de usuario no válido, se informa y se vuelve al Menú de Inicio
		[x] El nuevo usuario queda guardado con el archivo usuarios.csv
	Salir:
		[x]Se puede salir del programa de forma correcta.

*Flujo del programa:	
	Menú de chats:
		[x] El menú contiene todas las opciones mínimas pedidas en el enunciado.
		[x] Se puede volver al Menú de Inicio.
	Menú de contactos:
		[x] El menú tiene las opciones de ver contactos, añadir contactos y volver al menú anterior.
		[x] Al seleccionar ver contactos, se muestran todos los contactos del usuario correctamente.
		[ ] Al seleccionar un contacto, se despliega el historial. El historial se actualiza correctamente.
		[x] Se puede escribir un mensaje. El mensaje queda registrado correctamente en el archivo mensajes.csv, respetando el formato.
		[ ] Al escribir el comando VOLVER_FRASE, el usuario deberá volver a la opción ver contactos del menu de contactos.
		[ ] Se puede añadir un contacto de forma correcta. El contacto se almacena en el archivo contactos.csv
		[ ] Se verifica que el contacto sea válido. En caso contrario, se advierte al usuario y se vuelve al Menú de Contactos.
		[x] Se puede volver al Menú de Chats.
	Menú de grupos:
		[ ] El menú tiene las opciones de ver grupos, crear grupo y volver al menú anterior.
		[?] Al seleccionar ver grupos, se muestran todos los grupos a los que pertenece el usuario.
		[ ] Al seleccionar un grupo, se despliega el historial de forma correcta y en orden ascendente. El historial se actualiza correctamente.
		[ ] Se puede escribir un mensaje. El mensaje queda registrado correctamente en el archivo mensajes.csv, respetando el formato.
		[ ] Al escribir el comando VOLVER_FRASE, el usuario deberá volver a la opción ver grupos del menu de grupos
		[ ] Al escribir el comando ABANDONAR_FRASE, el usuario abandona el grupo, actualizando el archivo grupos.csv, y luego volver a la opción ver grupos del menu de grupos
		[ ] Al abandonar un grupo, se escribe un último mensaje de forma autómatica, quedando guardado en el archivo mensajes.csv
		[ ] Al crear un grupo, este queda registrado para todos los usuarios pertenecientes en el archivo grupos.csv
		[ ] Se verifica que el formato del grupo cumpla con las condiciones solicitadas (nombre del grupo no repetido, largo mínimo de 1 sin contener comas)
		[ ] Se verifica que el formato de los integrantes sea en el formato correcto y que los usuarios existan.
  		[ ] En caso de que no se pueda crear el grupo, se notifica al usuario y se vuelve al menú actual.
		[x] Se puede volver al Menú de Chats.
	Chats:
		[x] Se muestra cada mensaje de forma separada, mostrando la fecha, hora, emisor y el contenido.
		[x] Los mensajes se muestran en orden ascendente.
		[x] Se muestra cada mensaje de forma separada, mostrando el nombre del grupo, fecha, hora, emisor y el contenido.
		[ ] Los mensajes se muestran en orden ascendente.

*Archivos: [x]




## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  "main.py". Además se debe crear los siguientes archivos y directorios adicionales:
1. "contactos.csv"
2. "grupos.csv"
3. "usuarios.csv"




**EXTRA:** si van a explicar qué hace específicamente un método, no lo coloquen en el README mismo. Pueden hacerlo directamente comentando el método en su archivo. Por ejemplo:

```python
class Corrector:

    def __init__(self):
          pass

    # Este método coloca un 6 en las tareas que recibe
    def corregir(self, tarea):
        tarea.nota  = 6
        return tarea
```

Si quieren ser más formales, pueden usar alguna convención de documentación. Google tiene la suya, Python tiene otra y hay muchas más. La de Python es la [PEP287, conocida como reST](https://www.python.org/dev/peps/pep-0287/). Lo más básico es documentar así:

```python
def funcion(argumento):
    """
    Mi función hace X con el argumento
    """
    return argumento_modificado
```
Lo importante es que expliquen qué hace la función y que si saben que alguna parte puede quedar complicada de entender o tienen alguna función mágica usen los comentarios/documentación para que el ayudante entienda sus intenciones.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<link de código>: este hace \<lo que hace> y está implementado en el archivo <nombre.py> en las líneas <número de líneas> y hace <explicación breve de que hace>



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/main/Tareas/Descuentos.md).
