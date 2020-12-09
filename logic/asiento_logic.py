from core.dx_logic import Logic
from persist_objects.asiento_obj import AsientoObj


class AsientoLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName = "asiento"

    def getAllAsientos(self):
        asientoList = super().getAllRows(self.tableName)
        asientoObjList = []
        for element in asientoList:
            # newAsiento = self.createAsientoObj(element)
            asientoObjList.append(element)
        return asientoObjList

    # def createAsientoObj(self, idasiento, silla_numero, fila_letras):
    #     asientoObj = AsientoObj(id, silla_numero, fila_letras)
    #     return asientoObj

    def createAsientoObj(self, silla_numero, fila_letras):
        asientoDict = dict(silla_numero=silla_numero, fila_letras=fila_letras)
        return asientoDict

    def insertAsiento(self, silla_numero, fila_letras):
        database = self.database
        sql = (
            f"INSERT INTO `dbcine`.`asiento`(`idasiento`,`silla_numero`,`fila_letras`)"
            + f"VALUES(0,'{silla_numero}','{fila_letras}');"
        )
        row = database.executeNonQueryRows(sql)
        return row

    def updateAsientoById(self, idasiento, silla_numero, fila_letras):
        database = self.database
        sql = (
            "UPDATE `dbcine`.`asiento` "
            + f"SET `silla_numero` = '{silla_numero}', `fila_letras` = '{fila_letras}' "
            + f"WHERE `idasiento` = {idasiento};"
        )
        row = database.executeNonQueryRows(sql)
        return row

    def getAsientoById(self, idasiento):
        database = self.database
        sql = "SELECT * FROM `dbcine`.`asiento` " + f"where idasiento ={idasiento};"
        sucursalDict = database.executeQueryOneRow(sql)
        return sucursalDict

    def deleteAsientoById(self, idasiento):
        database = self.database
        sql = "DELETE FROM `dbcine`.`asiento` " + f"WHERE idasiento = {idasiento};"
        row = database.executeNonQueryRows(sql)
        return row
