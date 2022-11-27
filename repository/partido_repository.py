from model.partido import Partido
from repository.repository_interface import InterfaceRepository


class RepositorioPartido(InterfaceRepository[Partido]):

    def find_by_aggregate(self, query):
        return self.repo.aggregate(query)
