class Biblioteca():
    def __init__(self):
        self.__catalogo = []
        self.__usuarios = []       # lista de usuarios
        self.__administradores = [] # lista de administradores

    def registrar_libros(self, libro):
        self.__catalogo.append(libro)

    def mostrar_catalogo(self):         
        if len(self.__catalogo) == 0:
            print("No hay libros en el catálogo")
        else:
            for i, libro in enumerate(self.__catalogo, 1):
                print(f"{i}. {libro}")

    def registrar_usuario(self, nombre, apellido, edad, documento, clave, nombre_usuario):
        usuario1 = Usuario(nombre, apellido, edad, documento, clave, nombre_usuario, self) 
        self.__usuarios.append(usuario1)
        return usuario1  

    def registrar_administrador(self, nombre, apellido, edad, documento, clave, nombre_administrador): 
        admin1 = Administrador(nombre, apellido, edad, documento, clave, nombre_administrador, self)   
        self.__administradores.append(admin1)
        return admin1    
    
    @property 
    def catalogo(self):
        return self.__catalogo

    @property
    def usuarios(self):
        return self.__usuarios
    
    @property
    def administradores(self):
        return self.__administradores
            

class Libro():
    def __init__(self, categoria, titulo, autor, numero_paginas):
        self.categoria = categoria
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas 
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"[{self.categoria}] {self.titulo} - {self.autor} ({self.numero_paginas} págs) - {estado}"
        

class Usuario():
    def __init__(self, nombre, apellido, edad, documento, clave, nombre_usuario, biblioteca):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.documento = documento
        self.__clave = clave
        self.__usuario_normal = nombre_usuario
        self.biblioteca = biblioteca
        self.libros_prestados = []

    @property
    def clave(self):
        return self.__clave
    @clave.setter
    def clave(self, valor):
        self.__clave = valor

    @property
    def nombre_usuario(self):
        return self.__usuario_normal

    def validar_usuario_normal(self, usuario_normal, clave_usuario):
        return (usuario_normal == self.__usuario_normal and clave_usuario == self.__clave)
        
    def pedir_libro(self, titulo):
        for libro in self.biblioteca.catalogo:
            if libro.titulo == titulo and libro.disponible:
                libro.disponible = False
                self.libros_prestados.append(libro)
                print(f"Has pedido el libro: {libro.titulo}")
                return
        print("El libro no está disponible o no existe en el catálogo.")

    def devolver_libro(self, titulo):
        for libro in self.libros_prestados:
            if libro.titulo == titulo:
                libro.disponible = True
                self.libros_prestados.remove(libro)
                print(f"Has devuelto el libro: {libro.titulo}")
                return
        print("No tienes este libro en préstamo.")

    def mostrar_perfil(self):
        print(f"Usuario: {self.nombre} {self.apellido}, Edad: {self.edad}, Documento: {self.documento}")
        if len(self.libros_prestados) > 0:
            print("Libros prestados:")
            for libro in self.libros_prestados:
                print(f"- {libro.titulo}")
        else:
            print("No tienes libros prestados.")


class Administrador():
    def __init__(self, nombre, apellido, edad, documento, clave, nombre_administrador, biblioteca):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.documento = documento
        self.__clave = clave
        self.__usuario_admin = nombre_administrador
        self.biblioteca = biblioteca

    @property
    def clave(self):
        return self.__clave
    @clave.setter
    def clave(self, valor):
        self.__clave = valor

    @property
    def nombre_administrador(self):
        return self.__usuario_admin

    def validar_usuario_admin(self, usuario_admin, clave_admin):
        return (usuario_admin == self.__usuario_admin and clave_admin == self.__clave)    
            
    def agregar_libro(self, categoria, titulo, autor, numero_paginas):
        libro_nuevo = Libro(categoria, titulo, autor, numero_paginas)
        self.biblioteca.registrar_libros(libro_nuevo)
        print(f"Libro '{titulo}' agregado al catálogo.")

    def eliminar_libro(self, titulo):
        for libro in self.biblioteca.catalogo:
            if libro.titulo == titulo:
                self.biblioteca.catalogo.remove(libro)
                print(f"Libro '{titulo}' eliminado del catálogo.")
                return
        print("El libro no existe en el catálogo.")

    def mostrar_catalogo(self):
        self.biblioteca.mostrar_catalogo()

    def mostrar_usuarios(self):
        if len(self.biblioteca.usuarios) == 0:
            print("No hay usuarios registrados.")
        else:
            print("Usuarios registrados:")
            for u in self.biblioteca.usuarios:
                print(f"- {u.nombre_usuario}")


def main():
    print("Bilbioteca parcial POO")
    bibloUnal = Biblioteca()
    
    while True:
        tipo_usuario = int(input("\n1. Usuario 2. Administrador 3. Salir\n>>> "))
        if (tipo_usuario == 3):
            break

        if (tipo_usuario == 1):
            registro = int(input("1. Registrarse 2. Iniciar sesión \n>>> "))
            if (registro == 1):
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                edad = input("Edad: ")
                documento = input("Documento: ")
                nombre_usuario = input("Nombre de usuario: ")
                clave = input("Clave: ")
                bibloUnal.registrar_usuario(nombre, apellido, edad, documento, clave, nombre_usuario)
                print("Usuario registrado con éxito")

            if (registro == 2):
                nombre_de_usuario = input("Nombre de usuario: ")
                clave_usuario = input("Clave: ") 
                usuario_encontrado = None
                for u in bibloUnal.usuarios:
                    if u.validar_usuario_normal(nombre_de_usuario, clave_usuario):
                        usuario_encontrado = u
                        break

                if(usuario_encontrado):
                    print("Ingreso correcto")
                    while True:
                        opcion = int(input("\n1. Pedir libro 2. Devolver libro 3. Mostrar perfil 4. Salir\n>>> "))
                        if(opcion == 1):
                            titulo = input("Título del libro a pedir: ")
                            usuario_encontrado.pedir_libro(titulo)
                        if(opcion == 2):
                            titulo = input("Título del libro a devolver: ")
                            usuario_encontrado.devolver_libro(titulo)
                        if(opcion == 3):
                            usuario_encontrado.mostrar_perfil()
                        if(opcion == 4):
                            break
                else:
                    print("Clave o usuario incorrectos, intentelo de nuevo")

        if (tipo_usuario == 2):
            registro = int(input("1. Registrarse 2. Iniciar sesión \n>>> "))
            if (registro == 1):
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                edad = input("Edad: ")
                documento = input("Documento: ")
                nombre_administrador = input("Nombre de administrador: ")
                clave = input("Clave: ")
                bibloUnal.registrar_administrador(nombre, apellido, edad, documento, clave, nombre_administrador)
                print("Administrador registrado con éxito")

            if (registro == 2):
                usuario_admin = input("Nombre de administrador: ")
                clave_admin = input("Clave: ")
                admin_encontrado = None
                for a in bibloUnal.administradores:
                    if a.validar_usuario_admin(usuario_admin, clave_admin):
                        admin_encontrado = a
                        break

                if(admin_encontrado):
                    print("Ingreso correcto")
                    while True:
                        opciones_admin = int(input("\n1. Agregar libros 2. Eliminar libros 3. Mostrar catálogo 4. Mostrar usuarios 5. Salir\n>>> "))
                        if(opciones_admin == 1):
                            categoria = input("Categoria del libro: ")
                            titulo = input("Titulo del libro: ")
                            autor = input("Autor del libro: ")
                            numero_paginas = input("Numero de paginas del libro: ")
                            admin_encontrado.agregar_libro(categoria, titulo, autor, numero_paginas)
                        if(opciones_admin == 2):
                            titulo = input("Titulo del libro a eliminar: ")
                            admin_encontrado.eliminar_libro(titulo)
                        if(opciones_admin == 3):
                            admin_encontrado.mostrar_catalogo()
                        if(opciones_admin == 4):
                            admin_encontrado.mostrar_usuarios()
                        if(opciones_admin == 5):
                            break
                else:
                    print("Clave o usuario incorrectos, intentelo de nuevo")    

if __name__ == "__main__":
    main()

