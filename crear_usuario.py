from app import crear_app
from models import db
from models.usuario import Usuario


app = crear_app()

with app.app_context():
    usuario = Usuario(
        nombre="Herto",
        username="herto"
    )
    usuario.establecer_password("1234")

    usuario2 = Usuario(
        nombre= "Marcela",
        username="marcela"
    )
    usuario2.establecer_password("asdf")

    db.session.add(usuario2)
    db.session.commit()

    print("Usuario creado correctamente.")