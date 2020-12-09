from core.dx_logic import Logic
from persist_objects.compradetallada_obj import CompraDetObj


class CompraDetLogic(Logic):
    def __init__(self):
        super().__init__()
        self.tableName = "compradetallada"

    def getAllCompras(self):
        compraList = super().getAllRows(self.tableName)
        compraObjList = []
        for element in compraList:
            compraObjList.append(element)
        return compraObjList

    def createCompraObj(
        self, tipo, precios_unitarios, cantidad, monto_total, estado, usuario_idusuario
    ):
        compraDict = dict(
            tipo=tipo,
            precios_unitarios=precios_unitarios,
            cantidad=cantidad,
            monto_total=monto_total,
            estado=estado,
            usuario_idusuario=usuario_idusuario,
        )
        return compraDict

    def insertCompra(
        self, tipo, precios_unitarios, cantidad, monto_total, estado, usuario_idusuario
    ):
        database = self.database
        sql = (
            f"INSERT INTO `dbcine`.`compradetallada`(`idcompra`,`tipo`,`precios_unitarios`,`cantidad`,`monto_total`,`estado`, `usuario_idusuario`) "
            + f"VALUES(0,'{tipo}','{precios_unitarios}',{cantidad},'{monto_total}'',{estado}', {usuario_idusuario});"
        )
        row = database.executeNonQueryRows(sql)
        return row

    def updateCompraById(
        self,
        idcompra,
        tipo,
        precios_unitarios,
        cantidad,
        monto_total,
        estado,
        usuario_idusuario,
    ):
        database = self.database
        sql = (
            "UPDATE `dbcine`.`compradetallada` "
            + f"SET `tipo` = '{tipo}', `precios_unitarios` = '{precios_unitarios}', `cantidad` = {cantidad}, `monto_total` = '{monto_total}', `estado` = '{estado}' , `usuario_idusuario` = {usuario_idusuario} "
            + f"WHERE `idcompra` = {idcompra};"
        )
        row = database.executeNonQueryRows(sql)
        return row

    def getCompraById(self, idcompra):
        database = self.database
        sql = (
            "SELECT * FROM `dbcine`.`compradetallada` " + f"where idcompra ={idcompra};"
        )
        compraDict = database.executeQueryOneRow(sql)
        return compraDict

    def getCompraByUser(self, usuario_idusuario):
        database = self.database
        sql = (
            "SELECT * FROM `dbcine`.`compradetallada` "
            + f"where usuario_idusuario ={usuario_idusuario};"
        )
        compraDict = database.executeQueryOneRow(sql)
        return compraDict

    def deleteCompraById(self, idcompra):
        database = self.database
        sql = (
            "DELETE FROM `dbcine`.`compradetallada` " + f"WHERE idcompra = {idcompra};"
        )
        row = database.executeNonQueryRows(sql)
        return row
