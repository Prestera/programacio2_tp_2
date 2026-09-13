from app import crear_app
from models import db
from models.categoria import Categoria


app = crear_app()

with app.app_context():

    categorias = [
        ("Alimentación", "gasto"),
        ("Transporte", "gasto"),
        ("Servicios", "gasto"),
        ("Entretenimiento", "gasto"),
        ("Salud", "gasto"),
        ("Otros", "gasto"),
        ("Sueldo", "ingreso"),
        ("Freelance", "ingreso"),
        ("Inversiones", "ingreso"),
        ("Otros ingresos", "ingreso"),
        
    ]

    for nombre, tipo in categorias:
        categoria = Categoria(
            nombre=nombre,
            tipo=tipo
        )
        db.session.add(categoria)

    db.session.commit()

    print("Categorías creadas correctamente.")