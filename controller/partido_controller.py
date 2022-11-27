from model.partido import Partido
from repository.partido_repository import RepositorioPartido


class ControladorPartido():
    def __init__(self):
        self.repo = RepositorioPartido()

    # Listar
    def index(self):
        return self.repo.find_all()

    # Crear
    def create(self, info_partido):
        nuevo_partido = Partido(info_partido)
        return self.repo.save(nuevo_partido)

    # Leer
    def show(self, id):
        return self.repo.find_by_id(id)

    # Actualizar
    def update(self, id, info_partido):
        partido_actualizado = Partido(info_partido)
        return self.repo.update(id, partido_actualizado)

    # Eliminar
    def delete(self, id):
        return self.repo.delete(id)

    def find_by_query(self, query):
        return self.repo.query(query)