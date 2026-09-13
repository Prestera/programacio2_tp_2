from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user

from .forms import IngresoForm
from models.categoria import Categoria
from servicios.servicio_ingreso import ServicioIngreso


ingresos = Blueprint(
    "ingresos",
    __name__,
    template_folder="templates"
)


@ingresos.route("/ingresos/nuevo", methods=["GET", "POST"])
@login_required
def nuevo():

    form = IngresoForm()

    categorias = Categoria.query.filter_by(
        tipo="ingreso"
    ).order_by(Categoria.nombre).all()

    form.categoria_id.choices = [
        (categoria.id_categoria, categoria.nombre)
        for categoria in categorias
    ]

    if form.validate_on_submit():

        servicio = ServicioIngreso()

        datos = {
            "monto": form.monto.data,
            "fecha": form.fecha.data,
            "descripcion": form.descripcion.data,
            "categoria_id": form.categoria_id.data,
            "usuario_id": current_user.id_usuario
        }

        servicio.crear(datos)

        return redirect(url_for("ingresos.nuevo"))

    return render_template(
        "ingresos/nuevo.html",
        form=form
    )


@ingresos.route("/ingresos")
@login_required
def listar():

    servicio = ServicioIngreso()

    lista_ingresos = servicio.listar_por_usuario(
        current_user.id_usuario
    )

    return render_template(
        "ingresos/listar.html",
        ingresos=lista_ingresos
    )


@ingresos.route(
    "/ingresos/<int:id_ingreso>/editar",
    methods=["GET", "POST"]
)
@login_required
def editar(id_ingreso):

    servicio = ServicioIngreso()

    try:
        ingreso = servicio.obtener_por_usuario(
            id_ingreso,
            current_user.id_usuario
        )
    except ValueError:
        return "Ingreso no encontrado", 404

    mes=request.args.get("mes", 9, type=int),
    año=request.args.get("año", 2026, type=int)
    
    form = IngresoForm()

    categorias = Categoria.query.filter_by(
        tipo="ingreso"
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
            id_ingreso,
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

        form.monto.data = ingreso.monto
        form.fecha.data = ingreso.fecha
        form.descripcion.data = ingreso.descripcion
        form.categoria_id.data = ingreso.categoria_id

    return render_template(
        "ingresos/editar.html",
        form=form,
        ingreso=ingreso,
        mes=mes,
        año=año
    )


@ingresos.route(
    "/ingresos/<int:id_ingreso>/eliminar",
    methods=["POST"]
)
@login_required
def eliminar(id_ingreso):

    servicio = ServicioIngreso()

    try:
        servicio.eliminar(
            id_ingreso,
            current_user.id_usuario
        )
    except ValueError:
        return "Ingreso no encontrado", 404

    return redirect(
        url_for(
            "detalle.mostrar",
            mes=request.args.get("mes", 9, type=int),
            año=request.args.get("año", 2026, type=int)
        )
    )