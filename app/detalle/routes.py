from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

from models.gasto import Gasto
from models.ingreso import Ingreso


detalle = Blueprint(
    "detalle",
    __name__,
    template_folder="templates"
)


@detalle.route("/detalle")
@login_required
def mostrar():

    mes = request.args.get("mes", type=int)
    año = request.args.get("año", type=int)

    if mes is None:
        mes = 9

    if año is None:
        año = 2026

    gastos = Gasto.query.filter_by(
        usuario_id=current_user.id_usuario
    ).all()

    ingresos = Ingreso.query.filter_by(
        usuario_id=current_user.id_usuario
    ).all()

    gastos_del_mes = [
        gasto for gasto in gastos
        if gasto.fecha.year == año and gasto.fecha.month == mes
    ]

    ingresos_del_mes = [
        ingreso for ingreso in ingresos
        if ingreso.fecha.year == año and ingreso.fecha.month == mes
    ]

    return render_template(
        "detalle/detalle.html",
        gastos=gastos_del_mes,
        ingresos=ingresos_del_mes,
        mes=mes,
        año=año
    )