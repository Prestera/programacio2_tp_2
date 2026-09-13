from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

from servicios.servicio_financiero import ServicioFinanciero


resumen = Blueprint(
    "resumen",
    __name__,
    template_folder="templates"
)


@resumen.route("/resumen")
@login_required
def mostrar():
    servicio = ServicioFinanciero()

    total_gastos = servicio.total_gastos(
        current_user.id_usuario
    )

    total_ingresos = servicio.total_ingresos(
        current_user.id_usuario
    )

    balance = servicio.balance(
        current_user.id_usuario
    )

    gastos_por_categoria = servicio.gastos_por_categoria(
        current_user.id_usuario
    )

    mes = request.args.get("mes", type=int)
    año = request.args.get("año", type=int)

    if mes is None:
        mes = 9

    if año is None:
        año = 2026

    gastos_del_mes = servicio.gastos_por_mes(
        current_user.id_usuario,
        año,
        mes
    )

    ingresos_por_categoria = servicio.ingresos_por_categoria(
        current_user.id_usuario
    )

    ingresos_del_mes = servicio.ingresos_por_mes(
        current_user.id_usuario,
        año,
        mes
    )
    balance_del_mes = servicio.balance_por_mes(
        current_user.id_usuario,
        año,
        mes
    )

    return render_template(
        "resumen/resumen.html",
        total_gastos=total_gastos,
        total_ingresos=total_ingresos,
        balance=balance,
        gastos_por_categoria=gastos_por_categoria,
        gastos_del_mes=gastos_del_mes,
        ingresos_por_categoria=ingresos_por_categoria,
        ingresos_del_mes=ingresos_del_mes,
        balance_del_mes=balance_del_mes,
        año=año,
        mes=mes
    )