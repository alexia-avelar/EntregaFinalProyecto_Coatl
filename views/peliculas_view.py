from prettytable import PrettyTable
from logic.peliculas_logic import PeliculasLogic


logic = PeliculasLogic()


def viewAllPeliculas():
    peliculasObjList = logic.getAllPeliculas()
    table = PrettyTable()
    table.field_names = ["Id", "Titulo", "Descripción", "Fecha", "Hora"]

    for peliculas in peliculasObjList:
        table.add_row(
            [
                peliculas["idpeliculas"],
                peliculas["titulo"],
                peliculas["descripcion"],
                peliculas["fecha"],
                peliculas["hora"],
            ]
        )
    print(table)


def addPelicula():
    print("Ingrese nueva pelicula")
    titulo = input("Título:")
    descripcion = input("Descripción:")
    fecha = input("Fecha:")
    hora = input("Hora: ")

    logic.createPeliculasObj(titulo, descripcion, fecha, hora)
    logic.insertPeliculas(titulo, descripcion, fecha, hora)
    print("Película añadida con éxito")


def updatePelicula():
    print("Actualice la pelicula")
    idpelicula = int(input("Id de pelicula a actualizar: "))
    oldPelicula = logic.getPeliculaById(idpelicula)

    update = int(input("¿Actualizar Titulo? Si -1 No - 0 "))
    if update == 1:
        print(f"Título anterior: {oldPelicula['titulo']}")
        titulo = input("titulo: ")
    else:
        titulo = oldPelicula["titulo"]

    update = int(input("¿Actualizar Descripcion? Si - 1 No - 0 "))
    if update == 1:
        print(f"Descripción anterior: {oldPelicula['descripcion']}")
        descripcion = input("descripcion: ")
    else:
        descripcion = oldPelicula["descripcion"]

    update = int(input("¿Actualizar Fecha? Si - 1 No - 0 "))
    if update == 1:
        print(f"Fecha anterior: {oldPelicula['fecha']}")
        fecha = input("fecha: ")
    else:
        fecha = oldPelicula["fecha"]

    update = int(input("¿Actualizar Hora? Si - 1 No - 0 "))
    if update == 1:
        print(f"Hora anterior: {oldPelicula['hora']}")
        hora = input("hora: ")
    else:
        hora = oldPelicula["hora"]

    pelicula = logic.updatePeliculasById(idpelicula, titulo, descripcion, fecha, hora)
    print("La información de la película ha sido actualizada")


def deletePelicula():
    print("Eliminar Película")
    idpelicula = int(input("ID de pelicula a eliminar: "))
    logic.deletePeliculasById(idpelicula)
    print("Película eliminada con éxito")
