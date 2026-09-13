from repositorios.repositorioGenericos import RepositorioGenerico
from models.gasto import Gasto

class ServicioGasto:
    def __init__(self):
        self.__repositorio = RepositorioGenerico(Gasto)
        
    def crear(self, datos):
        return self.__repositorio.crear(datos)
    
    def listar_por_usuario(self, usuario_id):
        return self.__repositorio.listar_por({
            "usuario_id": usuario_id
        })
        
    def obtener_por_usuario(self, id_gasto, usuario_id):
        gastos = self.__repositorio.listar_por({
            "id_gasto": id_gasto,
            "usuario_id": usuario_id
        })
        if not gastos:
            raise ValueError("No existe el gasto para este usuario")
        
        return gastos[0]
    
    def actualizar(self, id_gasto, usuario_id, datos):
        self.obtener_por_usuario(id_gasto, usuario_id)

        return self.__repositorio.actualizar(
            id_gasto,
            datos
    )
        
    def eliminar(self, id_gasto, usuario_id):
        self.obtener_por_usuario(id_gasto, usuario_id)

        return self.__repositorio.eliminar(id_gasto)     