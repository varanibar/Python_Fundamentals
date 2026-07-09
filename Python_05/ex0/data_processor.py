from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self._counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise Exception("Data is empty")
        return (self._data.pop(0))


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(
                    isinstance(i, (int, float))
                    and not isinstance(i, bool)
                    for i in data)
        else:
            return (isinstance(data, (int, float))
                    and not isinstance(data, bool))

    def ingest(self, data:
               int | float | list[int] | list[float] | list[int | float]
               ) -> None:
        if self.validate(data):
            if isinstance(data, (int, float)):
                tup = (self._counter, str(data))
                self._data.append(tup)
                self._counter += 1
            else:
                for i in data:
                    tup = (self._counter, str(i))
                    self._data.append(tup)
                    self._counter += 1
        else:
            raise TypeError("Improper numeric data")


def numeric_processor_test() -> None:
    num_processor = NumericProcessor()
    test_1 = 42
    print(f"Trying to validate input '{test_1}': ", end="")
    print(f"{num_processor.validate(test_1)}")

    test_2 = "Hello"
    print(f"Trying to validate input '{test_2}': ", end="")
    print(f"{num_processor.validate(test_2)}")

    test_3 = "foo"
    print(f"Test invalid ingestion of string '{test_3}'", end="")
    print(" without prior validation:")
    try:
        num_processor.ingest(test_3)
    except Exception as err:
        print(f"Got exception: {err}")

    list_data = [1, 2, 3, 4, 5]
    print(f"Processing data: {list_data}")
    num_processor.ingest(list_data)
    print(num_processor._data)
    n = 3
    for _ in range(n):
        output = num_processor.output()
        print(f"Numeric value {output[0]}: {output[1]}")


def main() -> None:
    numeric_processor_test()


if __name__ == "__main__":
    main()
