from model.candidato import Candidato
from repository.candidato_repository import RepositorioCandidato

class ControladorCandidato():
    def __init__(self):
        self.repo = RepositorioCandidato()

    # Listar
    def index(self):
        return self.repo.find_all()

    # Crear
    def create(self, info_candidato):
        nuevo_candidato = Candidato(info_candidato)
        return self.repo.save(nuevo_candidato)

    # Leer
    def show(self, id):
        return self.repo.find_by_id(id)

    # Actualizar
    def update(self, id, info_candidato):
        candidato_actualizado = Candidato(info_candidato)
        return self.repo.update(id, candidato_actualizado)

    # Eliminar
    def delete(self, id):
        return self.repo.delete(id)

    def find_by_query(self, query):
        return self.repo.query(query)
