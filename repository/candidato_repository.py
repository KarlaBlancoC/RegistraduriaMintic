from model.candidato import Candidato
from repository.repository_interface import InterfaceRepository
from repository.partido_repository import RepositorioPartido


class RepositorioCandidato(InterfaceRepository[Candidato]):
    def __init__(self):
        super().__init__()
        self.repo_par = RepositorioPartido()

    def find_all(self):
        lista_candidatos = super().find_all()
        for x in lista_candidatos:
            id_partido = x["id_partido"]
            del x["id_partido"]
            x["partido"] = self.repo_par.find_by_id(id_partido)
        return lista_candidatos

    def find_by_id(self, id):
        candidato = super().find_by_id(id)
        id_partido = candidato["id_partido"]
        del candidato["id_partido"]
        candidato["partido"] = self.repo_par.find_by_id(id_partido)

        return candidato

    def find_by_query(self, query):
        return self.repo.query(query)

    def find_by_aggregate(self, query):
        return self.repo.aggregate(query)
