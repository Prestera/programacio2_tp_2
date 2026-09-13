from models import db

class Ingreso(db.Model):
    __tablename__ = "ingresos"
    id_ingreso = db.Column(db.Integer, primary_key=True, autoincrement=True)
    monto = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    descripcion = db.Column(db.String(100), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id_usuario"), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey("categorias.id_categoria"), nullable=False)
    
    usuario = db.relationship(
        "Usuario",
        backref="ingresos"
    )   
    
    categoria = db.relationship(
        "Categoria",
        backref="ingresos"
    )