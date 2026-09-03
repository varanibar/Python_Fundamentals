from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[tuple[int, str]] = []
        self._index: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        try:
            extracted_data = self._data.pop(0)
            return extracted_data
        except Exception as err:
            print(f"{err.__class__.__name__}: {err}")
            return (-1, "Empty")


class NumericProcessor(DataProcessor):

    def validate(
                self,
                data: Any
                ) -> bool:

        if isinstance(data, list):
            return all(
                    isinstance(item, (int, float))
                    and not isinstance(item, bool)
                    for item in data
                    )

        else:
            return (
                    isinstance(data, (int, float))
                    and not isinstance(data, bool)
                    )

    def ingest(
            self,
            data: int | float | list[int] | list[float] | list[int | float]
            ) -> None:

        if self.validate(data):
            if isinstance(data, list):
                for item in data:
                    tup = (self._index, str(item))
                    self._data.append(tup)
                    self._index += 1
            else:
                tup = (self._index, str(data))
                self._data.append(tup)
                self._index += 1

        else:
            raise TypeError("Improper numeric data")


class TextProcessor(DataProcessor):

    def validate(
                self,
                data: Any
                ) -> bool:

        if isinstance(data, list):
            return all(
                    isinstance(item, str)
                    and not isinstance(item, bool)
                    for item in data)

        else:
            return (isinstance(data, str)
                    and not isinstance(data, bool))

    def ingest(
            self,
            data: str | list[str]
            ) -> None:

        if self.validate(data):
            if isinstance(data, list):
                for item in data:
                    tup = (self._index, item)
                    self._data.append(tup)
                    self._index += 1
            else:
                tup = (self._index, data)
                self._data.append(tup)
                self._index += 1

        else:
            raise TypeError("Improper text data")


class LogProcessor(DataProcessor):

    def validate(
                self,
                data: Any
                ) -> bool:

        def _validate_dict(
                        data: dict[str, str]
                        ) -> bool:
            return (
                all(isinstance(key, str) for key in data.keys())
                and
                all(isinstance(val, str) for val in data.values())
                )

        if isinstance(data, dict):
            return (_validate_dict(data))

        if isinstance(data, list):
            if all(isinstance(item, dict) for item in data):
                return (all(_validate_dict(item) for item in data))

        return False

    def ingest(
            self,
            data: dict[str, str] | list[dict[str, str]]
            ) -> None:

        if not self.validate(data):
            raise TypeError("Improper log data")

        def _store_log(log_entry: dict[str, str]) -> None:
            values = ": ".join(log_entry.values())
            tup = (self._index, values)
            self._data.append(tup)
            self._index += 1

        if isinstance(data, list):
            for log_entry in data:
                _store_log(log_entry)
        elif isinstance(data, dict):
            _store_log(data)


def numeric_processor_test() -> None:
    num_processor = NumericProcessor()

    tests = [
            42,
            "Hello",
            [1, 2, 3, 4, 5],
            [1, 2.1, 3],
            ["a", "b"]
            ]
    for test in tests:
        print(f"Trying to validate input '{test}': ", end="")
        print(f"{num_processor.validate(test)}")

    test_ingest = "foo"
    print(f"\nTest invalid ingestion of string '{test_ingest}'", end="")
    print(" without prior validation:")
    try:
        num_processor.ingest(test_ingest)
    except Exception as err:
        print(f"Got exception: {err}")

    num_data = [1, 2, 3, 4, 5]
    print(f"\nProcessing data: {num_data}")
    num_processor.ingest(num_data)
    n = 2
    print(f"Extracting {n} value(s)...")
    for _ in range(n):
        output = num_processor.output()
        print(f"Numeric value {output[0]}: {output[1]}")


def text_processor_test() -> None:
    text_processor = TextProcessor()

    tests = [
            42,
            "Hello",
            [1, 2, 3, 4, "a"],
            [1, 2.1, 3],
            ["a", "b"]
            ]
    for test in tests:
        print(f"Trying to validate input '{test}': ", end="")
        print(f"{text_processor.validate(test)}")

    text_data = ["Hello", "Nexus", "World"]
    print(f"\nProcessing data: {text_data}")
    text_processor.ingest(text_data)
    n = 2
    print(f"Extracting {n} value(s)...")
    for _ in range(n):
        output = text_processor.output()
        print(f"Text value {output[0]}: {output[1]}")


def log_processor_test() -> None:
    log_processor = LogProcessor()

    tests = [
            42,
            "Hello",
            [1, 2, 3, 4, "a"],
            {"c": "d", "a": "b", 1: "2"},
            {"a": "aa", "b": "bb", "c": "cc"},
            ]
    for test in tests:
        print(f"Trying to validate input '{test}': ", end="")
        print(f"{log_processor.validate(test)}")

    log_data = [{
                "log_level": "NOTICE",
                "log_message": "Connection to server"
                },
                {
                "log_level": "ERROR",
                "log_message": "Unauthorized access!!"
                }]

    print(f"\nProcessing data: {log_data}")
    log_processor.ingest(log_data)
    n = 2
    print(f"Extracting {n} value(s)...")
    for _ in range(n):
        output = log_processor.output()
        print(f"Log entry {output[0]}: {output[1]}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    print("\n+++++++++++++++++++++++++")
    print("Testing Numeric Processor...\n")
    numeric_processor_test()

    print("\n\n+++++++++++++++++++++++++")
    print("Testing Text Processor...\n")
    text_processor_test()

    print("\n\n+++++++++++++++++++++++++")
    print("Testing Log Processor...\n")
    log_processor_test()
    print("\n\n+++++++++++++++++++++++++")


if __name__ == "__main__":
    main()
