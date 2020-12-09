from prettytable import PrettyTable
from logic.asiento_logic import AsientoLogic

logic = AsientoLogic()


def viewAllAsientos():
    asientosObjList = logic.getAllAsientos()
    table = PrettyTable()
    table.field_names = ["Id", "Número de silla", "Letra de fila"]

    for asiento in asientosObjList:
        table.add_row(
            [asiento["idasiento"], asiento["silla_numero"], asiento["fila_letras"]]
        )
    print(table)


def addAsiento():
    print("Ingrese el número de asiento y la letra de fila")
    silla_numero = input("Número de asiento:")
    fila_letras = input("Letra de fila:")

    logic.createAsientoObj(silla_numero, fila_letras)
    logic.insertAsiento(silla_numero, fila_letras)
    print("Asiento añadido con éxito")


def updateAsiento():
    print("Actualización de asiento")
    idasiento = int(input("Id de asiento a actualizar: "))
    oldAsiento = logic.getAsientoById(idasiento)

    update = int(input("¿Desea actualizar el número de asiento? Si - 1  No - 0: "))
    if update == 1:
        print(f"Número anterior: {oldAsiento['silla_numero']}")
        silla_numero = input("Ingrese el nuevo número de asiento: ")
    else:
        silla_numero = oldAsiento["silla_numero"]

    update = int(input("¿Desea actualizar la letra de fila? Si - 1  No - 0: "))
    if update == 1:
        print(f"Letra anterior: {oldAsiento['fila_letras']}")
        fila_letras = input("Ingrese la nueva letra de asiento: ")
    else:
        fila_letras = oldAsiento["fila_letras"]

    asiento = logic.updateAsientoById(idasiento, silla_numero, fila_letras)
    print("La información del asiento ha sido actualizada")


def deleteAsiento():
    print("Eliminar asiento")
    idasiento = int(input("Id de asiento a eliminar: "))
    logic.deleteAsientoById(idasiento)
    print("Asiento eliminado con éxito")
