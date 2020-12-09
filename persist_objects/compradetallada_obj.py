class CompraDetObj:
    def __init__(
        self,
        tipo,
        precios_unitarios,
        cantidad,
        monto_total,
        estado,
        usuario_idusuario,
        idcompra=0,
    ):
        self.tipo = tipo
        self.precios_unitarios = precios_unitarios
        self.cantidad = cantidad
        self.monto_total = monto_total
        self.estado = estado
        self.usuario_idusuario = usuario_idusuario
        self.idcompra = idcompra
