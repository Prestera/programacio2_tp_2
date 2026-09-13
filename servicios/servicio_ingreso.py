from repositorios.repositorioGenericos import RepositorioGenerico
from models.ingreso import Ingreso


class ServicioIngreso:

    def __init__(self):
        self.__repositorio = RepositorioGenerico(Ingreso)

    def crear(self, datos):
        return self.__repositorio.crear(datos)

    def listar_por_usuario(self, usuario_id):
        return self.__repositorio.listar_por({
            "usuario_id": usuario_id
        })

    def obtener_por_usuario(self, id_ingreso, usuario_id):
        ingresos = self.__repositorio.listar_por({
            "id_ingreso": id_ingreso,
            "usuario_id": usuario_id
        })

        if not ingresos:
            raise ValueError("No existe el ingreso para este usuario.")

        return ingresos[0]

    def actualizar(self, id_ingreso, usuario_id, datos):
        self.obtener_por_usuario(id_ingreso, usuario_id)

        return self.__repositorio.actualizar(
            id_ingreso,
            datos
        )

    def eliminar(self, id_ingreso, usuario_id):
        self.obtener_por_usuario(id_ingreso, usuario_id)

        return self.__repositorio.eliminar(id_ingreso)