from core.dx_logic import Logic
from persist_objects.boleto_obj import BoletoObj


class BoletoLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName = "boleto"

    def getAllBoletos(self):
        boletoList = super().getAllRows(self.tableName)
        boletoObjList = []
        for element in boletoList:
            boletoObjList.append(element)
        return boletoObjList

    def createBoletoObj(
        self,
        tipo,
        fecha,
        hora,
        compradetallada_idcompra,
        sala_idsala,
        peliculas_idpeliculas,
        sucursal_idsucursal,
        usuario_idusuario,
    ):
        boletoDict = dict(
            tipo=tipo,
            fecha=fecha,
            hora=hora,
            compradetallada_idcompra=compradetallada_idcompra,
            sala_idsala=sala_idsala,
            peliculas_idpeliculas=peliculas_idpeliculas,
            sucursal_idsucursal=sucursal_idsucursal,
            usuario_idusuario=usuario_idusuario,
        )
        return boletoDict

    def insertBoleto(
        self,
        tipo,
        fecha,
        hora,
        compradetallada_idcompra,
        sala_idsala,
        peliculas_idpeliculas,
        sucursal_idsucursal,
        usuario_idusuario,
    ):
        database = self.database
        sql = (
            f"INSERT INTO `dbcine`.`boleto`(`idboleto`,`tipo`,`fecha`,`hora`, `compradetallada_idcompra`, `sala_idsala`, `peliculas_idpeliculas`, `sucursal_idsucursal`, `usuario_idusuario`) "
            + f"VALUES(0,'{tipo}','{fecha}','{hora}',{compradetallada_idcompra},{sala_idsala},{peliculas_idpeliculas},{sucursal_idsucursal},{usuario_idusuario});"
        )
        row = database.executeNonQueryRows(sql)
        return row

    def updateBoletoById(
        self,
        idboleto,
        tipo,
        fecha,
        hora,
        compradetallada_idcompra,
        sala_idsala,
        peliculas_idpeliculas,
        sucursal_idsucursal,
        usuario_idusuario,
    ):
        database = self.database
        sql = (
            "UPDATE `dbcine`.`boleto` "
            + f"SET `tipo` = '{tipo}', `fecha` = '{fecha}', `hora` = '{hora}', `compradetallada_idcompra` = {compradetallada_idcompra},`sala_idsala` = {sala_idsala}, `peliculas_idpeliculas` = {peliculas_idpeliculas}, `sucursal_idsucursal` = {sucursal_idsucursal}, `usuario_idusuario` = {usuario_idusuario} "
            + f"WHERE `idboleto` = {idboleto};"
        )
        row = database.executeNonQueryRows(sql)
        return row

    def getBoletoById(self, idboleto):
        database = self.database
        sql = "SELECT * FROM `dbcine`.`boleto` " + f"where idboleto ={idboleto};"
        boletoDict = database.executeQueryOneRow(sql)
        return boletoDict

    def getBoletoByUser(self, usuario_idusuario):
        database = self.database
        sql = (
            "SELECT * FROM `dbcine`.`boleto` "
            + f"where usuario_idusuario = {usuario_idusuario};"
        )
        boletoDict = database.executeQueryOneRow(sql)
        return boletoDict

    def deleteBoletoById(self, idcompra):
        database = self.database
        sql = (
            "DELETE FROM `dbcine`.`boleto` "
            + f"WHERE compradetallada_idcompra = {idcompra};"
        )
        row = database.executeNonQueryRows(sql)
        return row
