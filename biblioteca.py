#PROGRAMA REALIZADO POR SOFIA BURBANO-ALEJANDRO PORTILLA
# Clase Libro
#1 PUNTO CREA CLASE LIBRO CON PARAMETROS
class Libro:
    def __int__(self, titulo, codigo, autor, aniopub, disponible=True):
        self.titulo = titulo
        self.codigo = codigo
        self.autor = autor
        self.aniopub = aniopub
        self.disponible = disponible
    def disponibilidad(self):
        return "Libro disponible" if self.disponible else "Ups! no se encuentra disponible"

# Clase Biblioteca
#2 PUNTO CREA BIBLIOTECA COPN PARAMETROS
#3 INSTANCIA LOS OBJETOS DE LA CLASE BIBLIOTECA
#6 CREACION DE LAS FUNCIONES NECESARIAS PARA QUE PROGRAMA FUNCIONE DE FORMA CORRECTA APLICANDO LA POO
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print("------------------------------------------------------------")
        print(f'Libro "{libro.titulo}" agregado con exito a la biblioteca! ')

    def buscar_libro(self, identificador):
        for libro in self.libros:
            if libro.titulo == identificador or libro.codigo == identificador:
                return libro
        return None

    def listar_libros(self):
        if not self.libros:
            print("------------------------------------------")
            print("Lo sentimos, no hay libros en la biblioteca")
        else:
            for libro in self.libros:
                print(f'Título: {libro.titulo}, Autor: {libro.autor}, Año: {libro.aniopub}, Estado: {libro.disponibilidad()}')

    def prestar_libro(self, identificador):
        libro = self.buscar_libro(identificador)
        if libro:
            if libro.disponible:
                libro.disponible = False
                print(f'Listo, has prestado el libro: {libro.titulo}')
            else:
                print(f'Ups! el libro "{libro.titulo}" no está disponible')
        else:
            print("-------------------------")
            print("Ups, libro no encontrado.")

    def devolver_libro(self, identificador):
        libro = self.buscar_libro(identificador)
        if libro:
            if not libro.disponible:
                libro.disponible = True
                print(f'Has devuelto el libro con exito: {libro.titulo}')
            else:
                print(f'El libro "{libro.titulo}" ya estaba disponible.')
        else:
            print("---------------------------------")
            print("Lo sentimos, libro no encontrado.")

#MENU DE BIBLIOTECA DE POO (BIBLIOTECA)
#4 PUNTO IMPLEMENTA UN MENU CON 6 OPCIONES PUESTAS
#5 AGREGA CONDICIONALES Y CICLOS (IF , ELIF, WHILE)

def menu():
    biblioteca = Biblioteca()

    while True:
        print("---------Bienvedido a nuestra Biblioteca--------")
        print("\n--- Menú Biblioteca ---")
        print("1. Agregar un libro")
        print("2. Buscar un libro")
        print("3. Listar todos los libros")
        print("4. Prestar un libro")
        print("5. Devolver un libro")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("Ha seleccionado la Opcion de Agregar un libro")
            print("----------------------------------------------")
            titulo = input("Título: ")
            codigo = input("Código: ")
            autor = input("Autor: ")
            aniopub = input("Año de publicación: ")
            libro = Libro(titulo, codigo, autor, aniopub)
            biblioteca.agregar_libro(libro)

        elif opcion == "2":
            print("Ha seleccionado la Opcion de Buscar un libro")
            print("----------------------------------------------")
            identificador = input("Introduce el título o el código del libro: ")
            libro = biblioteca.buscar_libro(identificador)
            if libro:
                print(f'Título: {libro.titulo}, Autor: {libro.autor}, Año: {libro.aniopub}, Estado: {libro.disponibilidad()}')
            else:
                print("Ups!Libro no encontrado.")

        elif opcion == "3":
            print("Ha seleccionado la Opcion de Listar todos libros")
            print("----------------------------------------------")
            biblioteca.listar_libros()

        elif opcion == "4":
            print("Ha seleccionado la Opcion de Prestar un libro")
            print("----------------------------------------------")
            identificador = input("Introduce el título o el código del libro a prestar: ")
            biblioteca.prestar_libro(identificador)

        elif opcion == "5":
            print("Ha seleccionado la Opcion de Devolver un libro")
            print("----------------------------------------------")
            identificador = input("Introduce el título o el código del libro a devolver: ")
            biblioteca.devolver_libro(identificador)

        elif opcion == "6":
            print("Saliendo del programa, gracias por preferirnos!")
            print("----------------------------------------------")
            break

        else:
            print("Ups! Opción no válida, intenta de nuevo...")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
