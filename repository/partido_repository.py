from model.partido import Partido
from repository.repository_interface import InterfaceRepository


class RepositorioPartido(InterfaceRepository[Partido]):
    def find_by_query(self, query):
        return self.repo.query(query)

    def find_by_aggregate(self, query):
        return self.repo.aggregate(query)