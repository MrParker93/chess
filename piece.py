from collections import namedtuple
from abc import ABC, abstractmethod

Coordinates = namedtuple("Coordinates", ["x", "y"])

class Piece(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def get_position(self) -> tuple[int, int]:
        pass

    @abstractmethod
    def all_possible_moves(self) -> list[Coordinates[int, int]]:
        pass

    @abstractmethod
    def legal_moves(self) -> list[Coordinates[int, int]]:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass

    @abstractmethod
    def draw_moves(self) -> None:
        pass