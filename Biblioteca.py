class Biblioteca():
    def __init__(self):
        self.__catalogo = []

    def registrar_libros(self):
        print("asdasd")    

    def mostrar_catalogo(self):         
        print("asdasd")

    def registrar_usuario(self, nombre, apellido, edad, documento, clave, nombre_usuario):
        usuario1 = Usuario(nombre, apellido, edad, documento, clave, nombre_usuario) 
        return usuario1  

    def registrar_administrador(self, nombre, apellido, edad, documento, clave, nombre_administrador): 
        admin1 = Administrador(nombre, apellido, edad, documento, clave, nombre_administrador)   
        return admin1    
    
    @property 
    def catalogo(self):
        print(self.__catalogo)
    @catalogo.setter
    def catalogo(self, valor):
        self.__catalogo = valor 
            

class Libro():
    def __init__(self, categoria, titulo, autor, numero_paginas):
        self.__categoria = categoria
        self.__titulo = titulo
        self.__autor = autor
        self.__numero_paginas = numero_paginas 
        
class Usuario():
    def __init__(self, nombre, apellido, edad, documento, clave, nombre_usuario):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.documento = documento
        self.__clave = clave
        self.__usuario_normal = nombre_usuario

    @property
    def clave(self):
        return self.clave
    @clave.setter
    def clave(self, valor):
        self.__clave = valor

    @property
    def nombre_usuario(self):
        return self.__usuario_normal
    @nombre_usuario.setter
    def nombre_admin(self, valor):
        self.__usuario_normal = valor     

    def validar_usuario_normal(self, usuario_normal, clave_usuario):
        if (usuario_normal == self.__usuario_normal and clave_usuario == self.__clave):
            print("Ingreso correcto")
            return True
        else:
            print("clave o usuario incorrectos, intentelo de nuevo")    
        
    def pedir_libro(self):
        print("asdasd")

    def devolver_libro(self):
        print("adsad")

class Administrador():
    def __init__(self, nombre, apellido, edad, documento, clave, nombre_administrador):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.documento = documento
        self.__clave = clave
        self.__usuario_admin = nombre_administrador

    @property
    def clave(self):
        return self.clave
    @clave.setter
    def clave(self, valor):
        self.__clave = valor

    @property
    def nombre_administrador(self):
        return self.__usuario_admin
    @nombre_administrador.setter
    def nombre_admin(self, valor):
        self.__usuario_admin = valor    


    def validar_usuario_admin(self, usuario_admin, clave_admin):
        if (usuario_admin == self.__usuario_admin and clave_admin == self.__clave):
            print("Ingreso correcto")
            return True
        else:
            print("clave o usuario incorrectos, intentelo de nuevo")    
            

    def editar_catalogo():
        print("Editar catalogo")   

                     
def main():
    print("Bilbioteca parcial POO")
    libros = []
    admin = 0
    usuario = 0
    bibloUnal = Biblioteca()
    
    while True:
        tipo_usuario = int(input("1. Usuario 2. Administrador"))
        if (tipo_usuario == 1):
            registro = int(input("1. Regisrarse 2. Iniciar sesión \n"))
            if (registro == 1):
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                edad = input("Edad")
                documento = input("Documento")
                nombre_usuario = input("Nombre de usuario: ")
                clave = input("Clave")
                usuario = bibloUnal.registrar_usuario(nombre, apellido, edad, documento, clave, nombre_usuario)
                usuario.clave = clave
            if (registro == 2):
                nombre_de_usuario = input("Nombre de usuario: ")
                clave_usuario = input("Clave: ") 
                validar = usuario.validar_usuario_normal(nombre_de_usuario,clave_usuario)   
                if(validar == True):
                    print("Opciones de usuario")
                    print("1. Pedir libro 2. Devolver libro 3. Mostrar informacion del perfil")
                    opcion = input(">>>")

        if (tipo_usuario == 2):
            registro = int(input("1. Regisrarse 2. Iniciar sesión \n"))
            if (registro == 1):
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                edad = input("Edad")
                documento = input("Documento")
                nombre_administrador = input("Nombre de administrador: ")
                clave = input("Clave")
                admin = bibloUnal.registrar_administrador(nombre, apellido, edad, documento, clave, nombre_administrador)
                admin.clave = clave
            if (registro == 2):
                usuario_admin = input("Nombre de usuario: ")
                clave_admin = input("Clave: ")
                validar = admin.validar_usuario_admin(usuario_admin, clave_admin)
                if(validar == True):
                    print("Opciones de administrador")
                    opciones_admin = int(input("1. agregar libros 2. mostrar informacion del pefil"))
                    if(opciones_admin == 1):
                        categoria = input("Categoria del libro")
                        titulo = input("Titulo del libro")
                        autor = input("Autor del libro")
                        numero_paginas = input("numero de paginas del libro")
                        libro_nuevo = Libro(categoria, titulo, autor, numero_paginas)
                        libros.append(libro_nuevo)
                        bibloUnal.catalogo(libros)
                        print(bibloUnal.catalogo)




                    

            
                  
main()
      
