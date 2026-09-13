from flask import Flask


from app.extensions import login_manager, csrf
from app.auth.routes import auth
from app.gastos.routes import gastos
from app.ingresos.routes import ingresos
from app.resumen.routes import resumen
from app.dashboard.routes import dashboard
from app.detalle.routes import detalle


from models import db
from models.categoria import Categoria
from models.gasto import Gasto
from models.ingreso import Ingreso
from models.usuario import Usuario


def crear_app():
    app = Flask(__name__)

    # Configuración
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gestion_financiera.db"
    app.config["SECRET_KEY"] = "clave-secreta"

    # Inicialización de extensiones
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    login_manager.login_view = "auth.login"

    # Registro de Blueprints
    app.register_blueprint(auth)
    app.register_blueprint(gastos)
    app.register_blueprint(ingresos)
    app.register_blueprint(resumen)
    app.register_blueprint(dashboard)
    app.register_blueprint(detalle)
    

    # Creación de tablas
    with app.app_context():
        db.create_all()

    return app


@login_manager.user_loader
def cargar_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))