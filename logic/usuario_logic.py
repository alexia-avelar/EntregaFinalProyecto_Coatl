from core.dx_logic import Logic
from persist_objects.usuario_obj import UsuarioObj


class UsuarioLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName = "usuario"

    def getAllUsuarios(self):
        usuarioList = super().getAllRows(self.tableName)
        usuarioObjList = []
        for element in usuarioList:
            usuarioObjList.append(element)
        return usuarioObjList

    def createUsuarioObj(self, user, email, password):
        usuarioDict = dict(
            user=user,
            email=email,
            password=password,
        )
        return usuarioDict

    def insertUsuario(self, user, email, password):
        database = self.database
        sql = (
            f"INSERT INTO `dbcine`.`usuario`(`idusuario`,`user`,`email`, `password`) "
            + f"VALUES(0,'{user}','{email}','{password}');"
        )
        row = database.executeNonQueryRows(sql)
        return row

    def updateUsuarioByEmailPassword(self, user, email, password):
        database = self.database
        sql = (
            "UPDATE `dbcine`.`usuario` "
            + f"SET `user` = '{user}', `email` = '{email}', `password` = '{password}' "
            + f"WHERE `email` = '{email}' and `password` = '{password}';"
        )
        row = database.executeNonQueryRows(sql)
        return row

    def getUserById(self, idusuario):
        database = self.database
        sql = "SELECT * FROM `dbcine`.`usuario` " + f"where idusuario ={idusuario};"
        usuarioDict = database.executeQueryOneRow(sql)
        return usuarioDict

    def getUserByEmailPassword(self, email, password):
        database = self.database
        sql = (
            "SELECT * FROM `dbcine`.`usuario` "
            + f"WHERE `email` = '{email}' and `password` = '{password}';"
        )
        usuarioDict = database.executeQueryOneRow(sql)
        return usuarioDict

    def deleteUsuarioByEmailPassword(self, email, password):
        database = self.database
        sql = (
            "DELETE FROM `dbcine`.`usuario` "
            + f"WHERE `email` = '{email}' and `password` = '{password}';"
        )
        row = database.executeNonQueryRows(sql)
        return row

    def deleteUsuarioById(self, idusuario):
        database = self.database
        sql = "DELETE FROM `dbcine`.`usuario` " + f"WHERE idusuario = {idusuario};"
        row = database.executeNonQueryRows(sql)
        return row

    def verificarUsuario(self, email, password):
        user = {}
        database = self.database
        sql = f"""SELECT * FROM `dbcine`.`usuario` 
        WHERE email='{email}' and password='{password}';"""
        user = self.getUserByEmailPassword(email, password)

        if user is None:
            return user
        else:
            return user