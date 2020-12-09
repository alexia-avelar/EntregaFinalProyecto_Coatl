from core.dx_logic import Logic
from persist_objects.sala_obj import SalaObj


class SalaLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName = "sala"

    def getAllSalas(self):
        salaList = super().getAllRows(self.tableName)
        salaObjList = []
        for element in salaList:
            salaObjList.append(element)
        return salaObjList

    def createSalaObj(self, capacidad, tipo):
        salaDict = dict(capacidad=capacidad, tipo=tipo)
        return salaDict

    def insertSala(self, capacidad, tipo):
        database = self.database
        sql = (
            f"INSERT INTO `dbcine`.`sala`(`idsala`,`capacidad`,`tipo`)"
            + f"VALUES(0,{capacidad},'{tipo}');"
        )
        row = database.executeNonQueryRows(sql)
        return row

    def updateSalaById(self, idsala, capacidad, tipo):
        database = self.database
        sql = (
            "UPDATE `dbcine`.`sala` "
            + f"SET `capacidad` = {capacidad}, `tipo` = '{tipo}'"
            + f"WHERE `idsala` = {idsala};"
        )
        row = database.executeNonQueryRows(sql)
        return row

    def getSalaById(self, idsala):
        database = self.database
        sql = "SELECT * FROM `dbcine`.`sala` " + f"where idsala ={idsala};"
        salaDict = database.executeQueryOneRow(sql)
        return salaDict

    def deleteSalaById(self, idsala):
        database = self.database
        sql = "DELETE FROM `dbcine`.`sala` " + f"WHERE idsala = {idsala};"
        row = database.executeNonQueryRows(sql)
        return row
