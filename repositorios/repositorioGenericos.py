from models import db

class RepositorioGenerico:
    def __init__(self, modelo):
        self.__modelo = modelo
        
    def crear(self, datos):
        objeto = self.__modelo(**datos)
        
        db.session.add(objeto)
        db.session.commit()
        return objeto
            
    def listar(self):
        return self.__modelo.query.all()
    
    def listar_por(self, filtros):
        return self.__modelo.query.filter_by(**filtros).all()
    
    def obtener(self, id):
        return db.session.get(self.__modelo, id)
    
    def actualizar(self, id, datos):
        objeto = self.obtener(id)

        if objeto is None:
            raise ValueError("No existe el registro")

        for campo, valor in datos.items():
            setattr(objeto, campo, valor)

        db.session.commit()

        return objeto
    
    def eliminar(self, id):
        objeto = self.obtener(id)
        
        if objeto is None:
            raise ValueError("No existe ese registro")
        
        db.session.delete(objeto)
        db.session.commit()
        
    