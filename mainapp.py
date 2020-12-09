from views.peliculas_view import (
    viewAllPeliculas,
    addPelicula,
    updatePelicula,
    deletePelicula,
)
from views.compradetallada_view import (
    addCompra,
    viewAllCompras,
    updateCompra,
    deleteCompra,
    viewMyCompras,
)

from views.boleto_view import addBoleto, viewAllBoletos, deleteBoleto, viewMyBoletos

from views.sucursal_view import (
    viewAllSucursales,
    addSucursal,
    updateSucursal,
    deleteSucursal,
)
from views.asiento_view import (
    viewAllAsientos,
    addAsiento,
    updateAsiento,
    deleteAsiento,
)
from views.sala_view import (
    viewAllSalas,
    addSala,
    updateSala,
    deleteSala,
)

from views.usuario_view import (
    viewAllUsers,
    createUser,
    updateUser,
    deleteMyUser,
    deleteUser,
    login,
)


def goToUsuarioSubMenuAdmin():
    while True:
        print("")
        print("Menú usuarios")
        print("0 - Regresar al menú principal: ")
        print("1 - Ver usuarios: ")
        print("2 - Agregar usuario: ")
        print("3 - Actualizar usuario: ")
        print("4 - Eliminar usuario: ")
        optionSucursal = int(input("Seleccione una opción: "))
        print("")

        if optionSucursal == 0:
            print("Regresando a menú principal...")
            break
        elif optionSucursal == 1:
            viewAllUsers()
        elif optionSucursal == 2:
            createUser()
        elif optionSucursal == 3:
            updateUser()
        elif optionSucursal == 4:
            deleteUser()
        else:
            print("Seleccione una opción válida ")


def goToSucursalesSubMenuAdmin():
    while True:
        print("")
        print("Menú Sucursal")
        print("0 - Regresar al menú principal: ")
        print("1 - Ver Sucursales: ")
        print("2 - Agregar Sucursal: ")
        print("3 - Actualizar Sucursal: ")
        print("4 - Borrar Sucursal: ")
        optionSucursal = int(input("Seleccione una opción: "))
        print("")

        if optionSucursal == 0:
            print("Regresando a menú principal...")
            break
        elif optionSucursal == 1:
            viewAllSucursales()
        elif optionSucursal == 2:
            addSucursal()
        elif optionSucursal == 3:
            updateSucursal()
        elif optionSucursal == 4:
            deleteSucursal()
        else:
            print("Seleccione una opción válida ")


def goToAsientosSubMenuAdmin():
    while True:
        print("")
        print("Asientos")
        print("Menu: ")
        print("0 - Regresar al menú principal: ")
        print("1 - Ver Asientos: ")
        print("2 - Agregar Asiento: ")
        print("3 - Actualizar Asiento: ")
        print("4 - Eliminar Asiento: ")
        optionAsiento = int(input("Seleccione una opción: "))
        print("")

        if optionAsiento == 0:
            print("Regresando a menú principal...")
            break
        elif optionAsiento == 1:
            viewAllAsientos()
        elif optionAsiento == 2:
            addAsiento()
        elif optionAsiento == 3:
            updateAsiento()
        elif optionAsiento == 4:
            deleteAsiento()
        else:
            print("Seleccione una opción válida ")


def goToSalaSubMenuAdmin():
    while True:
        print("")
        print("Menú Sala")
        print("0 - Regresar al menú principal: ")
        print("1 - Ver Salas: ")
        print("2 - Agregar Sala: ")
        print("3 - Actualizar Sala: ")
        print("4 - Eliminar Sala: ")
        optionSala = int(input("Seleccione una opción: "))
        print("")

        if optionSala == 0:
            print("Regresando a menú principal...")
            break
        elif optionSala == 1:
            viewAllSalas()
        elif optionSala == 2:
            addSala()
        elif optionSala == 3:
            updateSala()
        elif optionSala == 4:
            deleteSala()
        else:
            print("Seleccione una opción válida ")


def goToPeliculasSubMenuAdmin():
    while True:
        print("")
        print("Menú Películas")
        print("0 - Regresar a menú principal: ")
        print("1 - Ver Peliculas: ")
        print("2 - Agregar Pelicula: ")
        print("3 - Actualizar Pelicula: ")
        print("4 - Eliminar Pelicula: ")
        optionPelicula = int(input("Seleccione una opción: "))
        print("")

        if optionPelicula == 0:
            print("Regresando a menú principal...")
            break
        elif optionPelicula == 1:
            viewAllPeliculas()
        elif optionPelicula == 2:
            addPelicula()
        elif optionPelicula == 3:
            updatePelicula()
        elif optionPelicula == 4:
            deletePelicula()
        else:
            print("Seleccione una opción válida ")


def goToBoletoSubMenuAdmin():
    while True:
        print("")
        print("Menú Boletos: ")
        print("0 - Regresar a menú principal: ")
        print("1 - Ver reservas (boletos): ")
        print("2 - Crear reserva (boleto): ")
        optionBoleto = int(input("Seleccione una opción: "))
        print("")

        if optionBoleto == 0:
            print("Regresando a menú principal...")
            break
        elif optionBoleto == 1:
            viewAllBoletos()
        elif optionBoleto == 2:
            addBoleto()
        else:
            print("Seleccione una opción válida ")


def goToCompraDetalladaSubMenuAdmin():
    while True:
        print("")
        print("Menú Compra Detallada: ")
        print("0 - Regresar a menú principal: ")
        print("1 - Ver todas las compras: ")
        print("2 - Crear compra: ")
        print("3 - Actualizar una compra: ")
        print("4 - Eliminar una compra: ")
        optionCompra = int(input("Seleccione una opción: "))
        print("")

        if optionCompra == 0:
            print("Regresando a menú principal...")
            break
        elif optionCompra == 1:
            viewAllCompras()
        elif optionCompra == 2:
            addCompra()
        elif optionCompra == 3:
            updateCompra()
        elif optionCompra == 4:
            deleteCompra()
            deleteBoleto()
        else:
            print("Seleccione una opción válida ")


while True:
    print("")
    print("Bienvenid@ a la app cine")
    print(
        "¿Desea ingresar como cliente o administrador? 1 - Administrador  2 - Cliente normal  0 - Salir de la aplicación"
    )
    tipo = int(input("Seleccione una opción:"))
    print("")
    if tipo == 0:
        print("Saliendo de la aplicación...")
        break
    elif tipo == 1:
        print("Ingrese contraseña de acceso a administradores: ")
        contra = input("Contraseña: ")
        if contra == "adminCine2020":
            print("")
            print("Menú administradores: ")
            print("0 - Salir de la app: ")
            print("1 - Usuario: ")
            print("2 - Sucursales: ")
            print("3 - Peliculas: ")
            print("4 - Salas: ")
            print("5 - Asientos: ")
            print("6 - Boletos: ")
            print("7 - Detalle de compra: ")
            option = int(input("Seleccione una opción: "))
            print("")

            if option == 0:
                print("Saliste de la aplicación")
                break
            elif option == 1:
                goToUsuarioSubMenuAdmin()
            elif option == 2:
                goToSucursalesSubMenuAdmin()
            elif option == 3:
                goToPeliculasSubMenuAdmin()
            elif option == 4:
                goToSalaSubMenuAdmin()
            elif option == 5:
                goToAsientosSubMenuAdmin()
            elif option == 6:
                goToBoletoSubMenuAdmin()
            elif option == 7:
                goToCompraDetalladaSubMenuAdmin()
            else:
                print("Seleccione una opción válida ")

        else:
            print("")
            print("Contraseña incorrecta. Intente otra vez")
            print("")

    elif tipo == 2:
        print("")
        print("Menú clientes: ")
        print("0 - Salir de la app: ")
        print("1 - Registrarse: ")
        print("2 - Iniciar sesión: ")
        option = int(input("Seleccione una opción: "))
        print("")

        if option == 0:
            print("Saliste de la aplicación")
            break
        elif option == 1:
            createUser()
        elif option == 2:
            login()
            print("")
            print("Menú clientes: ")
            print("1 - Ver Sucursales: ")
            print("2 - Ver peliculas: ")
            print("3 - Ver salas: ")
            print("4 - Ver asientos: ")
            print("5 - Ver mis boletos: ")
            print("6 - Realizar una reserva (boleto): ")
            print("7 - Ver mis compras: ")
            optionUsuario = int(input("Seleccione una opción"))
            print("")
            if optionUsuario == 1:
                viewAllSucursales()
            elif optionUsuario == 2:
                viewAllPeliculas()
            elif optionUsuario == 3:
                viewAllSalas()
            elif optionUsuario == 4:
                viewAllAsientos()
            elif optionUsuario == 5:
                viewMyBoletos()
            elif optionUsuario == 6:
                addBoleto()
            elif optionUsuario == 7:
                viewMyCompras()
            else:
                print("Seleccione una opción válida ")
        else:
            print("Seleccione una opción válida ")

    else:
        print("Seleccione una opción válida ")
