from models import db 

class Categoria(db.Model):
    __tablename__ = "categorias"
    
    id_categoria = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False)
    tipo = db.Column(db.String(20),nullable=False)