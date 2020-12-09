class UsuarioObj:
    def __init__(self, nombrecompleto, user, email, password, idusuario=0):
        self.idusuario = idusuario
        self.nombrecompleto = nombrecompleto
        self.user = user
        self.email = email
        self.password = password
