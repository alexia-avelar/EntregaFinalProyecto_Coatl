from prettytable import PrettyTable
from logic.usuario_logic import UsuarioLogic
from login import login


logic = UsuarioLogic()


def viewAllUsers():
    usuariosObjList = logic.getAllUsuarios()
    table = PrettyTable()
    table.field_names = [
        "Id",
        "User",
        "Email",
        "Password",
    ]

    for usuario in usuariosObjList:
        table.add_row(
            [
                usuario["idusuario"],
                usuario["user"],
                usuario["email"],
                usuario["password"],
            ]
        )
    print(table)


def createUser():
    print("Regístrese en la aplicación")
    user = input("Usuario: ")
    email = input("Email: ")
    password = input("Contraseña: ")

    logic.createUsuarioObj(user, email, password)
    logic.insertUsuario(user, email, password)
    print("Usuario creado con éxito")


def updateUser():
    print("Actualice su información personal")
    print("Inicie sesión")
    login()
    print("Verifique su correo y contraseña para continuar")
    email = input("Correo electrónico: ")
    password = input("Contraseña: ")
    oldUsuario = logic.getUserByEmailPassword(email, password)

    update = int(input("¿Desea actualizar su usuario? Si - 1 No - 0 "))
    if update == 1:
        print(f"Usuario anterior: {oldUsuario['user']}")
        user = input("Ingrese su nuevo usuario: ")
    else:
        user = oldUsuario["user"]

    update = int(input("¿Desea actualizar su correo electrónico? Si - 1 No - 0 "))
    if update == 1:
        print(f"Correo anterior: {oldUsuario['email']}")
        email = input("Ingrese el nuevo correo: ")
    else:
        email = oldUsuario["email"]

    update = int(input("¿Desea actualizar su contraseña? Si - 1 No - 0 "))
    if update == 1:
        print(f"Contraseña anterior: {oldUsuario['password']}")
        password = input("Ingrese la nueva contraseña: ")
    else:
        password = oldUsuario["password"]

    usuario = logic.updateUsuarioByEmailPassword(user, email, password)
    print("Su información personal ha sido actualizada")


def deleteMyUser():
    print("Eliminar mi cuenta")
    print("Inicie sesión")
    login()
    print("Verifique su correo electrónico y contraseña para continuar")
    email = input("Correo electrónico: ")
    password = input("Contraseña: ")
    logic.deleteUsuarioByEmailPassword(email, password)
    print("Su cuenta ha sido eliminada con éxito")


def deleteUser():
    print("Eliminar usuario")
    idusuario = int(input("Id de usuario a eliminar: "))
    logic.deleteUsuarioById(idusuario)
    print("Usuario eliminado con éxito")
