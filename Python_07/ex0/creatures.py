from abc import ABC, abstractmethod

class Creature(ABC):
    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        message = f"{self.name} is a {self.type} type Creature"
        return message

class Flameling(Creature):
    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        message = f"{self.name} uses Ember"
        return

def main():
    print("Testing factory")

if __name__ == "__main__":
    main()
