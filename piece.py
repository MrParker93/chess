from abc import ABC, abstractmethod

class Piece(ABC):  
    @abstractmethod
    def move(self) -> None:
        pass
    
    @abstractmethod
    def get_coordinates(self) -> tuple[int, int]:
        pass
    
    @abstractmethod
    def draw(self) -> None:
        pass