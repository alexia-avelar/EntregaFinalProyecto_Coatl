class BoletoObj:
    def __init__(
        self,
        tipo,
        fecha,
        hora,
        compradetallada_idcompra,
        sala_idsala,
        peliculas_idpeliculas,
        usuario_idusuario,
        sucursal_idsucursal,
        idboleto=0,
    ):
        self.tipo = tipo
        self.fecha = fecha
        self.hora = hora
        self.compradetallada_idcompra = compradetallada_idcompra
        self.sala_idsala = sala_idsala
        self.peliculas_idpeliculas = peliculas_idpeliculas
        self.sucursal_idsucursal = sucursal_idsucursal
        self.usuario_idusuario = usuario_idusuario
        self.idboleto = idboleto
