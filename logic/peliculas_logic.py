from core.dx_logic import Logic
from persist_objects.peliculas_obj import PeliculasObj


class PeliculasLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName = "peliculas"

    def getAllPeliculas(self):
        peliculasList = super().getAllRows(self.tableName)
        peliculasObjList = []
        for element in peliculasList:
            peliculasObjList.append(element)
        #     newPeliculas = self.createPeliculasObj(element)
        #     peliculasObjList.append(newPeliculas)
        return peliculasObjList

    def createPeliculasObj(self, titulo, descripcion, fecha, hora):
        peliculasDict = dict(
            titulo=titulo, descripcion=descripcion, fecha=fecha, hora=hora
        )
        return peliculasDict

    def insertPeliculas(self, titulo, descripcion, fecha, hora):
        database = self.database
        sql = (
            f"INSERT INTO `dbcine`.`peliculas`(`idpeliculas`,`titulo`,`descripcion`,`fecha`, `hora`) "
            + f"VALUES(0,'{titulo}','{descripcion}','{fecha}','{hora}');"
        )
        row = database.executeNonQueryRows(sql)
        return row

    def updatePeliculasById(self, idpeliculas, titulo, descripcion, fecha, hora):
        database = self.database
        sql = (
            "UPDATE `dbcine`.`peliculas` "
            + f"SET `titulo` = '{titulo}', `descripcion` = '{descripcion}', `fecha` = '{fecha}', `fecha` = '{hora}' "
            + f"WHERE `idpeliculas` = {idpeliculas};"
        )
        row = database.executeNonQueryRows(sql)
        return row

    def getPeliculaById(self, idpeliculas):
        database = self.database
        sql = (
            "SELECT * FROM `dbcine`.`peliculas` " + f"where idpeliculas ={idpeliculas};"
        )
        peliculasDict = database.executeQueryOneRow(sql)
        return peliculasDict

    def deletePeliculasById(self, idpeliculas):
        database = self.database
        sql = (
            "DELETE FROM `dbcine`.`peliculas` " + f"WHERE idpeliculas = {idpeliculas};"
        )
        row = database.executeNonQueryRows(sql)
        return row
