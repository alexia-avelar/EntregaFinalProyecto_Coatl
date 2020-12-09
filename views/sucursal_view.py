from prettytable import PrettyTable
from logic.sucursal_logic import SucursalLogic

logic = SucursalLogic()


def viewAllSucursales():
    sucursalObjList = logic.getAllSucursales()
    table = PrettyTable()
    table.field_names = [
        "Id",
        "Nombre",
        "Departamento",
        "Dirección",
    ]

    for sucursal in sucursalObjList:
        table.add_row(
            [
                sucursal["idsucursal"],
                sucursal["nombre"],
                sucursal["departamento"],
                sucursal["direccion"],
            ]
        )
    print(table)


def addSucursal():
    print("Agregue nueva sucursal")
    nombre = input("Nombre sucursal:")
    departamento = input("Departamento:")
    direccion = input("Direccion:")

    logic.createSucursalObj(nombre, departamento, direccion)
    logic.insertSucursal(nombre, departamento, direccion)
    print("Sucursal creada con éxito")


def updateSucursal():
    print("Actualice la sucursal")
    idsucursal = int(input("Id de sucursal a actualizar: "))
    oldSucursal = logic.getSucursalById(idsucursal)

    update = int(input("¿Desea actualizar el nombre? Si - 1 No - 0 "))
    if update == 1:
        print(f"Nombre anterior: {oldSucursal['nombre']}")
        nombre = input("Ingrese el nuevo nombre de la película: ")
    else:
        nombre = oldSucursal["Ingrese el nuevo nombre:"]

    update = int(input("¿Desea actualizar el departamento? Si - 1 No - 0 "))
    if update == 1:
        print(f"Departamento anterior: {oldSucursal['departamento']}")
        departamento = input("Ingrese el nuevo departamento: ")
    else:
        departamento = oldSucursal["departamento"]

    update = int(input("¿Desea actualizar la dirección? Si - 1 No - 0 "))
    if update == 1:
        print(f"Direccion anterior: {oldSucursal['direccion']}")
        direccion = input("Ingrese la nueva dirección: ")
    else:
        direccion = oldSucursal["direccion"]

    sucursal = logic.updateSucursalById(idsucursal, nombre, departamento, direccion)
    print("La información de la sucursal ha sido actualizada")


def deleteSucursal():
    print("Eliminar sucursal")
    idsucursal = int(input("Id de sucursal a eliminar: "))
    logic.deleteSucursalById(idsucursal)
    print("Sucursal eliminada con éxito")
