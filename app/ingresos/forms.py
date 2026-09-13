from flask_wtf import FlaskForm
from wtforms import DecimalField, DateField, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length, ValidationError

from validaciones.validaciones import validar_fecha_no_futura


def validar_fecha(form, field):
    try:
        validar_fecha_no_futura(field.data)
    except ValueError as error:
        raise ValidationError(str(error))


class IngresoForm(FlaskForm):
    monto = DecimalField(
        "Monto",
        validators=[
            DataRequired(),
            NumberRange(min=0.01)
        ]
    )

    fecha = DateField(
        "Fecha",
        validators=[
            DataRequired(),
            validar_fecha
        ],
        format="%Y-%m-%d"
    )

    descripcion = StringField(
        "Descripción",
        validators=[
            DataRequired(),
            Length(max=100)
        ]
    )

    categoria_id = SelectField(
        "Categoría",
        coerce=int,
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField("Guardar")