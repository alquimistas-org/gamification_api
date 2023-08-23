from repository_interface.global_results_respository import GlobalResultsRepository


class GlobalResultsService:
    def __init__(self, repository: GlobalResultsRepository) -> None:
        self.repository = repository

    def get(self):
        return self.repository.get()
