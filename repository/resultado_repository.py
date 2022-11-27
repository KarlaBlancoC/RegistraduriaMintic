from model.resultado import Resultado
from repository.repository_interface import InterfaceRepository
from repository.candidato_repository import RepositorioCandidato
from repository.partido_repository import RepositorioPartido


class RepositorioResultado(InterfaceRepository[Resultado]):
    def __init__(self):
        super().__init__()
        self.repo_can = RepositorioCandidato()
        self.repo_par = RepositorioPartido()

    def find_all(self):
        lista_resultados = super().find_all()
        for x in lista_resultados:
            id_candidato = x["id_candidato"]
            candidato = self.repo_can.find_by_id(id_candidato)
            nombre_candidato = candidato["nombre"]
            apellido_candidato = candidato["apellido"]
            cedula_candidato = candidato["cedula"]
            partido = candidato["partido"]
            nombre_partido = partido["nombre"]
            del x["id_candidato"]
            x["nombre_candidato"] = nombre_candidato
            x["apellido_candidato"] = apellido_candidato
            x["nombre_partido"] = nombre_partido
            x["cedula_candidato"] = cedula_candidato
        return lista_resultados

    def find_by_id(self, id):
        resultado = super().find_by_id(id)
        id_candidato = resultado["id_candidato"]
        del resultado["id_candidato"]
        resultado["candidato"] = self.repo_can.find_by_id(id_candidato)

        return resultado

    def find_by_query(self,query):
        return self.repo.query(query)

    def find_by_aggregate(self,query):
        return self.repo.aggregate(query)