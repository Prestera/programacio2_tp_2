from models.gasto import Gasto
from models.ingreso import Ingreso


class ServicioFinanciero:

    def total_gastos(self, usuario_id):
        gastos = Gasto.query.filter_by(usuario_id=usuario_id).all()

        total = sum(gasto.monto for gasto in gastos)

        return total

    def total_ingresos(self, usuario_id):
        ingresos = Ingreso.query.filter_by(usuario_id=usuario_id).all()

        total = sum(ingreso.monto for ingreso in ingresos)

        return total

    def balance(self, usuario_id):
        total_ingresos = self.total_ingresos(usuario_id)
        total_gastos = self.total_gastos(usuario_id)

        return total_ingresos - total_gastos
    
    def balance_por_mes(self, usuario_id, año, mes):
        ingresos = self.ingresos_por_mes(
            usuario_id,
            año,
            mes
        )

        gastos = self.gastos_por_mes(
            usuario_id,
            año,
            mes
        )

        total_ingresos = sum(ingresos.values())
        total_gastos = sum(gastos.values())

        return total_ingresos - total_gastos
    
    def gastos_por_categoria(self, usuario_id):
        gastos = Gasto.query.filter_by(usuario_id=usuario_id).all()

        resumen = {}

        for gasto in gastos:
            categoria = gasto.categoria.nombre

            if categoria not in resumen:
                resumen[categoria] = 0

            resumen[categoria] += gasto.monto

        return resumen
    
    def gastos_por_mes(self, usuario_id, año, mes):
        gastos = Gasto.query.filter_by(
            usuario_id=usuario_id
        ).all()

        resumen = {}

        for gasto in gastos:
            if gasto.fecha.year == año and gasto.fecha.month == mes:
                categoria = gasto.categoria.nombre

                if categoria not in resumen:
                    resumen[categoria] = 0

                resumen[categoria] += gasto.monto

        return resumen
    
    def ingresos_por_categoria(self, usuario_id):
        ingresos = Ingreso.query.filter_by(usuario_id=usuario_id).all()

        resumen = {}

        for ingreso in ingresos:
            categoria = ingreso.categoria.nombre

            if categoria not in resumen:
                resumen[categoria] = 0

            resumen[categoria] += ingreso.monto

        return resumen
    
    def ingresos_por_mes(self, usuario_id, año, mes):
        ingresos = Ingreso.query.filter_by(
            usuario_id=usuario_id
        ).all()

        resumen = {}

        for ingreso in ingresos:
            if ingreso.fecha.year == año and ingreso.fecha.month == mes:
                categoria = ingreso.categoria.nombre

                if categoria not in resumen:
                    resumen[categoria] = 0

                resumen[categoria] += ingreso.monto

        return resumen    