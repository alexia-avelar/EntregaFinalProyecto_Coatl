from logic.boleto_logic import BoletoLogic
from views.compradetallada_view import deleteCompra
from prettytable import PrettyTable

logic = BoletoLogic()


def viewAllBoletos():
    boletosObjList = logic.getAllBoletos()
    table = PrettyTable()
    table.field_names = [
        "Id",
        "Tipo",
        "Fecha",
        "Hora",
        "IdCompra",
        "Sala",
        "Película",
        "Sucursal",
        "Usuario",
    ]

    for boleto in boletosObjList:
        table.add_row(
            [
                boleto["idboleto"],
                boleto["tipo"],
                boleto["fecha"],
                boleto["hora"],
                boleto["compradetallada_idcompra"],
                boleto["sala_idsala"],
                boleto["peliculas_idpeliculas"],
                boleto["sucursal_idsucursal"],
                boleto["usuario_idusuario"],
            ]
        )
    print(table)


def viewMyBoletos():
    print("Mis boletos")
    usuario_idusuario = int(input("Ingrese su id de usuario: "))
    boletosObjList = logic.getBoletoByUser(usuario_idusuario)
    table = PrettyTable()
    table.field_names = [
        "Id",
        "Tipo",
        "Fecha",
        "Hora",
        "IdCompra",
        "Sala",
        "Película",
        "Sucursal",
        "Usuario",
    ]

    for boleto in boletosObjList:
        table.add_row(
            [
                boleto["idboleto"],
                boleto["tipo"],
                boleto["fecha"],
                boleto["hora"],
                boleto["compradetallada_idcompra"],
                boleto["sala_idsala"],
                boleto["peliculas_idpeliculas"],
                boleto["sucursal_idsucursal"],
                boleto["usuario_idusuario"],
            ]
        )
    print(table)


def addBoleto():
    print("Agregue una nueva reserva (boleto)")
    tipo = input("Tipo: ")
    fecha = input("Fecha: ")
    hora = input("Hora: ")
    compradetallada_idcompra = int(input("Id de compra "))
    sala_idsala = int(input("Id de sala "))
    peliculas_idpeliculas = int(input("Id de pelicula: "))
    sucursal_idsucursal = int(input("Id de sucursal: "))
    usuario_idusuario = int(input("Su id de usuario: "))

    logic.createBoletoObj(
        tipo,
        fecha,
        hora,
        compradetallada_idcompra,
        sala_idsala,
        peliculas_idpeliculas,
        sucursal_idsucursal,
        usuario_idusuario,
    )
    logic.insertBoleto(
        tipo,
        fecha,
        hora,
        compradetallada_idcompra,
        sala_idsala,
        peliculas_idpeliculas,
        sucursal_idsucursal,
        usuario_idusuario,
    )
    print("Reserva (boleto) realizada exitosamente")


def deleteBoleto():
    logic.deleteBoletoById(id)