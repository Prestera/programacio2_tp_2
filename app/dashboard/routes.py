from flask import Blueprint, render_template
from flask_login import login_required, current_user

from servicios.servicio_financiero import ServicioFinanciero


dashboard = Blueprint(
    "dashboard",
    __name__,
    template_folder="templates"
)


@dashboard.route("/")
@login_required
def inicio():
    servicio = ServicioFinanciero()

    total_ingresos = servicio.total_ingresos(current_user.id_usuario)
    total_gastos = servicio.total_gastos(current_user.id_usuario)
    balance = servicio.balance(current_user.id_usuario)

    return render_template(
        "dashboard/dashboard.html",
        total_ingresos=total_ingresos,
        total_gastos=total_gastos,
        balance=balance
    )