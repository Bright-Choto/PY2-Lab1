from abc import ABC, abstractmethod
from typing import List, Optional

class AbstractFurniture(ABC):
    def __init__(self, material: str, weight: float):
        if weight <= 0:
            raise ValueError("Вес должен быть больше 0.")
        self.material = material
        self.weight = weight

    @abstractmethod
    def assemble(self) -> None:
        ...

    @abstractmethod
    def move(self, new_location: str) -> None:
        ...

class AbstractTree(ABC):
    def __init__(self, species: str, age: int):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self.species = species
        self.age = age

    @abstractmethod
    def grow(self, years: int) -> None:
        ...

    @abstractmethod
    def photosynthesize(self) -> str:
        ...

class AbstractSocialNetwork(ABC):
    def __init__(self, name: str, active_users: int):
        if active_users < 0:
            raise ValueError("Количество активных пользователей не может быть отрицательным.")
        self.name = name
        self.active_users = active_users

    @abstractmethod
    def post_content(self, content: str) -> None:
        ...

    @abstractmethod
    def add_friend(self, friend_name: str) -> None:
        ...

if __name__ == "__main__":
    import doctest
    doctest.testmod()
