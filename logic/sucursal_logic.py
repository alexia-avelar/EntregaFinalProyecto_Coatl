from core.dx_logic import Logic
from persist_objects.sucursal_obj import SucursalObj


class SucursalLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName = "sucursal"

    def getAllSucursales(self):
        sucursalList = super().getAllRows(self.tableName)
        sucursalObjList = []
        for element in sucursalList:
            sucursalObjList.append(element)
        return sucursalObjList

    def createSucursalObj(self, nombre, departamento, direccion):
        sucursalDict = dict(
            nombre=nombre,
            departamento=departamento,
            direccion=direccion,
        )
        return sucursalDict

    def insertSucursal(self, nombre, departamento, direccion):
        database = self.database
        sql = (
            f"INSERT INTO `dbcine`.`sucursal`(`idsucursal`,`nombre`,`departamento`,`direccion`) "
            + f"VALUES(0,'{nombre}','{departamento}','{direccion}');"
        )
        row = database.executeNonQueryRows(sql)
        return row

    def updateSucursalById(self, idsucursal, nombre, departamento, direccion):
        database = self.database
        sql = (
            "UPDATE `dbcine`.`sucursal` "
            + f"SET `nombre` = '{nombre}', `departamento` = '{departamento}', `direccion` = '{direccion}' "
            + f"WHERE `idsucursal` = {idsucursal};"
        )
        row = database.executeNonQueryRows(sql)
        return row

    def getSucursalById(self, idsucursal):
        database = self.database
        sql = "SELECT * FROM `dbcine`.`sucursal` " + f"where idsucursal ={idsucursal};"
        sucursalDict = database.executeQueryOneRow(sql)
        return sucursalDict

    def deleteSucursalById(self, idsucursal):
        database = self.database
        sql = "DELETE FROM `dbcine`.`sucursal` " + f"WHERE idsucursal = {idsucursal};"
        row = database.executeNonQueryRows(sql)
        return row
