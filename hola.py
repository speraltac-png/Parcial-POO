#autor : Santiago Peralta Castellanos
#Caso de uso: Bilioteca universitaria(parial)
#Registro libros
#Registro usuarios


class Biblioteca(): #Clase Principal
    def __init__(self): #Constructor clase principal
        self.__catalogo = [] #lista del catalogo
        self.__usuarios = [] #lista de usuarios      
        self.__administradores = [] #lista de administradores

    def registrar_libros(self, libro): #Metodo que agrega los libros a el catalogo
        self.__catalogo.append(libro) #Acá se agregan

    def mostrar_catalogo(self): # Metodo que muestra el catalogo de libros        
        if len(self.__catalogo) == 0: #Valida la cantidad de libros que hay en el catalogo, si es 0 
            print("No hay libros en el catálogo") #Imprime que no hay libros
        else:
            for i, libro in enumerate(self.__catalogo, 1): #De lo contrario ejecuta la funcion enumerate que los enumera
                print(f"{i}. {libro}") # Se recorre la lista enumerada y se imprime los valores de las tuplas que devuelve

    def registrar_usuario(self, nombre, apellido, edad, documento, clave, nombre_usuario): # Metodo de registrar usuario
        usuario1 = Usuario(nombre, apellido, edad, documento, clave, nombre_usuario, self) #Crea un objeto usuario
        self.__usuarios.append(usuario1) #lo añade a la lista de usuarios
        return usuario1 #Returna ese usuario en particular 

    def registrar_administrador(self, nombre, apellido, edad, documento, clave, nombre_administrador): #Metodo de registrar administrador
        admin1 = Administrador(nombre, apellido, edad, documento, clave, nombre_administrador, self) #Crea el objeto administrador  
        self.__administradores.append(admin1) #Agrega el objeto administrador a la lista de administradores
        return admin1 #Returna el administrador   
    
    @property 
    def catalogo(self):  #Es un getter del atributo privado catalogo
        return self.__catalogo

    @property
    def usuarios(self):  #Es un getter del atributo privado usuarios
        return self.__usuarios
    
    @property
    def administradores(self):  #Es un getter del atributo privado administradores
        return self.__administradores
            

class Libro(): #Clase libro a la cual se me olvido encapsular los atributos
    def __init__(self, categoria, titulo, autor, numero_paginas): #Constructor de la clase libro
        self.categoria = categoria
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas 
        self.disponible = True

    def __str__(self): #Esta funcion describe como se va a comportar el objeto cuando se imprima en pantalla
        estado = "Disponible" if self.disponible else "Prestado" # estado va a ser disponible si disponible es true, de lo contrario va a ser prestado
        return f"[{self.categoria}] {self.titulo} - {self.autor} ({self.numero_paginas} págs) - {estado}" #retorna todas las caracteristicas del libro
        

class Usuario(): #clase usuario, a la que tambien olvide encapsularle algunos atributos
    def __init__(self, nombre, apellido, edad, documento, clave, nombre_usuario, biblioteca): #constructor de la clase usuario
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.documento = documento
        self.__clave = clave
        self.__usuario_normal = nombre_usuario
        self.biblioteca = biblioteca
        self.libros_prestados = []

    @property
    def clave(self): #getter y setter de el atributo privado clave
        return self.__clave
    @clave.setter
    def clave(self, valor):
        self.__clave = valor

    @property 
    def nombre_usuario(self): #Getter del nombre de usuario
        return self.__usuario_normal

    def validar_usuario_normal(self, usuario_normal, clave_usuario): #metodo que valida si el usuario si esta registrado
        return (usuario_normal == self.__usuario_normal and clave_usuario == self.__clave) # Si las condiciones se cumplen devuelve true
        
    def pedir_libro(self, titulo): #metodo de prestar libro
        for libro in self.biblioteca.catalogo: # Recorre los libros de la biblioteca a la que el usuario se registró
            if libro.titulo == titulo and libro.disponible: # valida si el titulo coincide y si el libro está disponible
                libro.disponible = False #Ahora el libro ya no está disponible, por lo que la variable debe ser falsa
                self.libros_prestados.append(libro) # Agrega el libro a los libros prestados del usuario
                print(f"Has pedido el libro: {libro.titulo}") #Imprime en pantalla el libro que el usuario pidio prestado
                return
        print("El libro no está disponible o no existe en el catálogo.") # Si no encuentra el libro en el catalogo, escribe que no lo encontró

    def devolver_libro(self, titulo): #Metodo de devolver libro
        for libro in self.libros_prestados: #Recorre la lista de libros prestados
            if libro.titulo == titulo: #Si el titulo coincide 
                libro.disponible = True #Lo asigna como disponible
                self.libros_prestados.remove(libro) #Lo quita de la lista de libros prestados
                print(f"Has devuelto el libro: {libro.titulo}") #Imprime que has devuelto el libro
                return
        print("No tienes este libro en préstamo.") #Si no lo encuentra imprime que no lo has tomado prestado

    def mostrar_perfil(self): #Muestra el perfil del usuario
        print(f"Usuario: {self.nombre} {self.apellido}, Edad: {self.edad}, Documento: {self.documento}") #imprime los atributos
        if len(self.libros_prestados) > 0: #Si existen libros prestados
            print("Libros prestados:") #Los imprime
            for libro in self.libros_prestados: #Recorre la lista e imprime todos los libros que le han sido prestados
                print(f"- {libro.titulo}") #Realmente imprime solo el titulo
        else:
            print("No tienes libros prestados.") # Si no hay libros prestados, se imprime que no hay


class Administrador(): #Clase administrador
    def __init__(self, nombre, apellido, edad, documento, clave, nombre_administrador, biblioteca): #constructor clase administrador
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.documento = documento
        self.__clave = clave
        self.__usuario_admin = nombre_administrador
        self.biblioteca = biblioteca

    @property
    def clave(self): #getter y setter de la clave
        return self.__clave
    @clave.setter
    def clave(self, valor):
        self.__clave = valor

    @property #getter del nombre de usuario admin
    def nombre_administrador(self):
        return self.__usuario_admin

    def validar_usuario_admin(self, usuario_admin, clave_admin): #validar usuario admin
        return (usuario_admin == self.__usuario_admin and clave_admin == self.__clave) #Lo mismo que usuario normal, devuelve true si la clave y el usuario coinciden   
            
    def agregar_libro(self, categoria, titulo, autor, numero_paginas): #método para añadir libros al catálogo
        libro_nuevo = Libro(categoria, titulo, autor, numero_paginas) #Crea el objeto libro
        self.biblioteca.registrar_libros(libro_nuevo) #Registra los libros a la biblioteca del administrador
        print(f"Libro '{titulo}' agregado al catálogo.") #Imprime el libro que fue agregado

    def eliminar_libro(self, titulo): #Metodo que elimina los libros del catalogo
        for libro in self.biblioteca.catalogo: #recorre el catalogo de la biblioteca del administador
            if libro.titulo == titulo: #Si el libro coincide
                self.biblioteca.catalogo.remove(libro) #Lo elimina del catalogo
                print(f"Libro '{titulo}' eliminado del catálogo.") #Imprime el libro que fue eliminado del catalogo
                return
        print("El libro no existe en el catálogo.") #Si no lo encuentra, nos lo dice

    def mostrar_catalogo(self): #Muestra el catalogo
        self.biblioteca.mostrar_catalogo()

    def mostrar_usuarios(self): #Muestra los usuarios
        if len(self.biblioteca.usuarios) == 0: #Si no hay usuarios imprime que no hay usuarios
            print("No hay usuarios registrados.")
        else:
            print("Usuarios registrados:") #Si encuentra usuarios registrados 
            for u in self.biblioteca.usuarios: #Recorre la lista de usuarios
                print(f"- {u.nombre_usuario}") #Imprime cada nombre de usuario


def main(): #Funcion main, aca es donde se ejecuta todo
    print("Bilbioteca parcial POO")
    bibloUnal = Biblioteca() #Crea el objeto biblioteca UNAL
    
    while True: #Esto hace que el menu se repita y el usuario pueda hacer mas de una tarea
        tipo_usuario = int(input("\n1. Usuario 2. Administrador 3. Salir\n>>> ")) #Acá el usuario indica el tipo al que pertenece
        if (tipo_usuario == 3): #Esto lo saca del programa 
            break

        if (tipo_usuario == 1): #Se desplega un menu de opciones para el usuario regular
            registro = int(input("1. Registrarse 2. Iniciar sesión \n>>> ")) #registro o inicio de sesion
            if (registro == 1): #Se desplega el registro donde pide los datos necesarios
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                edad = input("Edad: ")
                documento = input("Documento: ")
                nombre_usuario = input("Nombre de usuario: ")
                clave = input("Clave: ")
                bibloUnal.registrar_usuario(nombre, apellido, edad, documento, clave, nombre_usuario) # llama el metodo de Biblioteca registrar usuario
                print("Usuario registrado con éxito") 

            if (registro == 2): #Inicio de sesion del usuario regular
                nombre_de_usuario = input("Nombre de usuario: ") 
                clave_usuario = input("Clave: ") 
                usuario_encontrado = None 
                for u in bibloUnal.usuarios: # recorre la lista de usuarios de la biblioteca
                    if u.validar_usuario_normal(nombre_de_usuario, clave_usuario): #valida si al usuario le corresponden el nombre y la clave 
                        usuario_encontrado = u #Si es así le asigna a usuario encontrado true o false
                        break #Si lo encuentra sale del for

                if(usuario_encontrado): #Si usuario encontrado es true
                    print("Ingreso correcto")
                    while True: #desplega el menu de usuario normal
                        opcion = int(input("\n1. Pedir libro 2. Devolver libro 3. Mostrar perfil 4. Salir\n>>> ")) 
                        if(opcion == 1):
                            titulo = input("Título del libro a pedir: ")#pide el titulo del libro que el usuario quiere pedir
                            usuario_encontrado.pedir_libro(titulo) #llama el metodo de usuario pedir libro y le pasa el titulo del libro para que lo busque
                        if(opcion == 2):
                            titulo = input("Título del libro a devolver: ") #pide el titulo del libro que el usuario quiere devolver
                            usuario_encontrado.devolver_libro(titulo) #llama el metodo de usuario devolver libro y le pasa el titulo del libro para que lo busque
                        if(opcion == 3):
                            usuario_encontrado.mostrar_perfil() #llama el metodo de usuario mostrar perfil
                        if(opcion == 4):
                            break #Sale del while 
                else:
                    print("Clave o usuario incorrectos, intentelo de nuevo") #Si no coincide con ningun usuario imprime esto

        if (tipo_usuario == 2): #Opciones de administrador
            registro = int(input("1. Registrarse 2. Iniciar sesión \n>>> "))
            if (registro == 1): #Registro igual al del usuario
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                edad = input("Edad: ")
                documento = input("Documento: ")
                nombre_administrador = input("Nombre de administrador: ")
                clave = input("Clave: ")
                bibloUnal.registrar_administrador(nombre, apellido, edad, documento, clave, nombre_administrador) #Llama el metodo de Biblioteca que registra administradores
                print("Administrador registrado con éxito")

            if (registro == 2): #Inicio de sesion de administradores, funciona igual que el de usuarios
                usuario_admin = input("Nombre de administrador: ") 
                clave_admin = input("Clave: ")
                admin_encontrado = None
                for a in bibloUnal.administradores: #Recorre la lista de administradores de la biblioteca
                    if a.validar_usuario_admin(usuario_admin, clave_admin): #Para cada administrador revisa si el usuario y la contraseña coinciden
                        admin_encontrado = a #Si conincide con alguno devuelve true
                        break

                if(admin_encontrado): #Si encuentra el admin se ejecutan las funciones de administrador
                    print("Ingreso correcto")
                    while True:
                        opciones_admin = int(input("\n1. Agregar libros 2. Eliminar libros 3. Mostrar catálogo 4. Mostrar usuarios 5. Salir\n>>> "))
                        if(opciones_admin == 1): #Metodo de agregar libro
                            categoria = input("Categoria del libro: ")
                            titulo = input("Titulo del libro: ")
                            autor = input("Autor del libro: ")
                            numero_paginas = input("Numero de paginas del libro: ")
                            admin_encontrado.agregar_libro(categoria, titulo, autor, numero_paginas)
                        if(opciones_admin == 2): #metodo de eliminar libro
                            titulo = input("Titulo del libro a eliminar: ")
                            admin_encontrado.eliminar_libro(titulo)
                        if(opciones_admin == 3): #metodo de mostrar catalogo
                            admin_encontrado.mostrar_catalogo()
                        if(opciones_admin == 4): #metodo de mostrar usuarios
                            admin_encontrado.mostrar_usuarios()
                        if(opciones_admin == 5): #Opcion para salir
                            break
                else:
                    print("Clave o usuario incorrectos, intentelo de nuevo")    

if __name__ == "__main__": #Forma correcta de llamar al main para que no quede como código suelto
    main()


