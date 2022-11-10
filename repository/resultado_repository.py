from model.resultado import Resultado
from repository.repository_interface import InterfaceRepository
from repository.candidato_repository import RepositorioCandidato


class RepositorioResultado(InterfaceRepository[Resultado]):
    def __init__(self):
        super().__init__()
        self.repo_can = RepositorioCandidato()

    def find_all(self):
        lista_resultados = super().find_all()
        for x in lista_resultados:
            id_candidato = x["id_candidato"]
            del x["id_candidato"]
            x["candidato"] = self.repo_can.find_by_id(id_candidato)
        return lista_resultados

    def find_by_id(self, id):
        resultado = super().find_by_id(id)
        id_candidato = resultado["id_candidato"]
        del resultado["id_candidato"]
        resultado["candidato"] = self.repo_can.find_by_id(id_candidato)

        return resultado