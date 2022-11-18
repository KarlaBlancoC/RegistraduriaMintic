from model.mesa import Mesa
from repository.repository_interface import InterfaceRepository


class RepositorioMesa(InterfaceRepository[Mesa]):
    def find_by_query(self, query):
        return self.repo.query(query)

    def find_by_aggregate(self, query):
        return self.repo.aggregate(query)