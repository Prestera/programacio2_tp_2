from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user

from .forms import GastoForm
from models.categoria import Categoria
from servicios.servicio_gasto import ServicioGasto


gastos = Blueprint(
    "gastos",
    __name__,
    template_folder="templates"
)


@gastos.route("/gastos/nuevo", methods=["GET", "POST"])
@login_required
def nuevo():
    form = GastoForm()

    categorias = Categoria.query.filter_by(
        tipo="gasto"
    ).order_by(Categoria.nombre).all()

    form.categoria_id.choices = [
        (categoria.id_categoria, categoria.nombre)
        for categoria in categorias
    ]

    if form.validate_on_submit():
        servicio = ServicioGasto()

        datos = {
            "monto": form.monto.data,
            "fecha": form.fecha.data,
            "descripcion": form.descripcion.data,
            "categoria_id": form.categoria_id.data,
            "usuario_id": current_user.id_usuario
        }

        servicio.crear(datos)

        return redirect(url_for("gastos.nuevo"))

    return render_template(
        "gastos/nuevo.html",
        form=form
    )


@gastos.route("/gastos")
@login_required
def listar():
    servicio = ServicioGasto()

    listar_gastos = servicio.listar_por_usuario(
        current_user.id_usuario
    )

    return render_template(
        "gastos/listar.html",
        gastos=listar_gastos
    )


@gastos.route(
    "/gastos/<int:id_gasto>/editar",
    methods=["GET", "POST"]
)
@login_required
def editar(id_gasto):

    servicio = ServicioGasto()

    try:
        gasto = servicio.obtener_por_usuario(
            id_gasto,
            current_user.id_usuario
        )
    except ValueError:
        return "Gasto no encontrado", 404

    mes = request.args.get("mes", 9, type=int)
    año = request.args.get("año", 2026, type=int)
    
    form = GastoForm()

    categorias = Categoria.query.filter_by(
        tipo="gasto"
    ).order_by(Categoria.nombre).all()

    form.categoria_id.choices = [
        (categoria.id_categoria, categoria.nombre)
        for categoria in categorias
    ]

    if form.validate_on_submit():

        datos = {
            "monto": form.monto.data,
            "fecha": form.fecha.data,
            "descripcion": form.descripcion.data,
            "categoria_id": form.categoria_id.data
        }

        servicio.actualizar(
            id_gasto,
            current_user.id_usuario,
            datos
        )

        return redirect(
            url_for(
                "detalle.mostrar",
                mes=mes,
                año=año
            )
        )

    if request.method == "GET":

        form.monto.data = gasto.monto
        form.fecha.data = gasto.fecha
        form.descripcion.data = gasto.descripcion
        form.categoria_id.data = gasto.categoria_id

    return render_template(
        "gastos/editar.html",
        form=form,
        gasto=gasto,
        mes=mes,
        año=año
    )


@gastos.route(
    "/gastos/<int:id_gasto>/eliminar",
    methods=["POST"]
)
@login_required
def eliminar(id_gasto):

    servicio = ServicioGasto()

    try:
        servicio.eliminar(
            id_gasto,
            current_user.id_usuario
        )
    except ValueError:
        return "Gasto no encontrado", 404

    return redirect(
        url_for(
            "detalle.mostrar",
            mes=request.args.get("mes", 9, type=int),
            año=request.args.get("año", 2026, type=int)
        )
    )