from model.resultado import Resultado
from repository.resultado_repository import RepositorioResultado
from repository.mesa_repository import RepositorioMesa
from repository.candidato_repository import RepositorioCandidato

class ControladorResultado():
    def __init__(self):
        self.repo = RepositorioResultado()
        self.repo_mesa = RepositorioMesa()
        self.repo_candidato = RepositorioCandidato()


    # Listar
    def index(self):
        return self.repo.find_all()

    # Crear
    def create(self, info_resultado):
        #Validar que el candidato y la mesa existan

        nuevo_resultado = Resultado(info_resultado)
        return self.repo.save(nuevo_resultado)

    # Leer
    def show(self, id):
        return self.repo.find_by_id(id)

    # Actualizar
    def update(self, id, info_resultado):
        resultado_actualizado = Resultado(info_resultado)
        return self.repo.update(id, resultado_actualizado)

    # Eliminar
    def delete(self, id):
        return self.repo.delete(id)

    def find_by_candidato(self, id_candidato):
        resultados = self.repo.query({"id_candidato": id_candidato})
        for x in resultados:
            del x["id_candidato"]
            id_mesa = x["id_mesa"]
            del x["id_mesa"]
            x["mesa"] = self.repo_mesa.find_by_id(id_mesa)
        return resultados

    def find_by_mesa(self, id_mesa):
        resultados = self.repo.query({"id_mesa": id_mesa})
        for x in resultados:
            del x["id_mesa"]
            id_candidato = x["id_candidato"]
            del x["id_candidato"]
            x["candidato"] = self.repo_candidato.find_by_id(id_candidato)
        return resultados



