from models import db

class Gasto(db.Model):
    __tablename__ = "gastos"
    id_gasto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    monto = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    descripcion = db.Column(db.String(100), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id_usuario"), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey("categorias.id_categoria"), nullable=False)
       
    usuario = db.relationship(
        "Usuario",
        backref="gastos"
    )   
    
    categoria = db.relationship(
        "Categoria",
        backref="gastos"
    )