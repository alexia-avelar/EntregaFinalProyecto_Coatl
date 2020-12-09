from core.dx_logic import DatabaseX
from logic.usuario_logic import UsuarioLogic

logic = UsuarioLogic()
database = DatabaseX()


def login():
    email = input("Ingrese su correo electrónico: ")
    password = input("Ingrese su contraseña : ")

    user = logic.verificarUsuario(email, password)

    if user is None:
        print("No se pudo iniciar sesión.")
        print("Corrobore los datos ingresados y vuelva a intentar.")
    else:
        print("Bienvenido a su cine, ", user["user"])
