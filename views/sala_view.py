from prettytable import PrettyTable
from logic.sala_logic import SalaLogic

logic = SalaLogic()


def viewAllSalas():
    salasObjList = logic.getAllSalas()
    table = PrettyTable()
    table.field_names = ["Id", "Capacidad", "Tipo"]

    for sala in salasObjList:
        table.add_row([sala["idsala"], sala["capacidad"], sala["tipo"]])
    print(table)


def addSala():
    print("Añada una nueva sala")
    capacidad = input("Capacidad: ")
    tipo = input("Tipo:")

    logic.createSalaObj(capacidad, tipo)
    logic.insertSala(capacidad, tipo)
    print("Sala creada con éxito")


def updateSala():
    print("Actualice la información de la sala")
    idsala = int(input("Id de sala a actualizar: "))
    oldSala = logic.getSalaById(idsala)

    update = int(input("¿Desea actualizar la capacidad de sala? Si - 1  No - 0: "))
    if update == 1:
        print(f"Capacidad anterior: {oldSala['capacidad']}")
        capacidad = int(input("Ingrese la nueva capacidad de sala: "))
    else:
        capacidad = oldSala["capacidad"]

    update = int(input("¿Desea actualizar el tipo de sala? Si - 1  No - 0: "))
    if update == 1:
        print(f"Tipo anterior: {oldSala['tipo']}")
        tipo = input("Ingrese el nuevo tipo de sala: ")
    else:
        tipo = oldSala["tipo"]

    sala = logic.updateSalaById(idsala, capacidad, tipo)
    print("La información de la sala ha sido actualizada")


def deleteSala():
    print("Eliminar sala")
    idsala = int(input("Id de sala a eliminar: "))
    logic.deleteSalaById(idsala)
    print("Sala eliminada con éxito")
