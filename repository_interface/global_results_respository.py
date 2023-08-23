from typing import Protocol


class GlobalResultsRepository(Protocol):

    def get():
        ...
