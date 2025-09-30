📚 Biblioteca UNAL – Proyecto de Programación Orientada a Objetos (POO)

Este es un proyecto de consola que simula una Biblioteca con funcionalidades básicas tanto para usuarios como administradores, utilizando Programación Orientada a Objetos (POO) en Python.

🚀 Características principales

Registro e inicio de sesión para usuarios y administradores.

Los usuarios pueden:

Pedir libros (pendiente de implementación completa).

Devolver libros (pendiente de implementación completa).

Los administradores pueden:

Agregar libros al catálogo.

Ver información de su perfil (por implementar).

Uso de encapsulamiento y propiedades (@property) para atributos privados.

🧱 Estructura del código

Biblioteca: Clase principal que contiene el catálogo de libros y permite registrar usuarios y administradores.

Libro: Clase para representar los libros, con atributos privados como categoría, título, autor y número de páginas.

Usuario: Clase que representa al usuario normal. Incluye métodos de autenticación y acciones sobre libros.

Administrador: Clase que representa al administrador. Puede editar el catálogo (agregar libros).

main(): Menú interactivo que permite al usuario o administrador navegar por las funcionalidades.

🏁 Cómo ejecutar

Asegúrate de tener Python 3 instalado.

Guarda el código en un archivo, por ejemplo: biblioteca.py.

Abre una terminal o consola en la carpeta del archivo.

Ejecuta:

python biblioteca.py

🔧 Funcionalidades por mejorar

Implementar métodos completos para:

pedir_libro() y devolver_libro() en la clase Usuario.

mostrar_catalogo() en Biblioteca.

editar_catalogo() en Administrador.

Mejorar la persistencia de datos (actualmente se pierde al cerrar el programa).

Manejo de errores para entradas incorrectas.

Uso de listas o bases de datos para almacenar usuarios y libros de forma permanente.

📌 Notas importantes

El catálogo está encapsulado dentro de la clase Biblioteca como un atributo privado.

Algunas validaciones dependen de que previamente se haya registrado un usuario o administrador, de lo contrario pueden ocurrir errores.

👨‍💻 Autor

Desarrollado como parte de un proyecto de evaluación de POO.
Puedes adaptarlo y expandirlo para añadir funcionalidades más completas o una interfaz gráfica en el futuro.

¿Quieres que este proyecto sea ejecutable en la web (por ejemplo, con una interfaz web en Flask) o empaquetarlo como app de escritorio? Puedo ayudarte con eso también.
