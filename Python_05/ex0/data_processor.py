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
        try:
            extracted_data = self._data.pop(0)
            return extracted_data
        except Exception as err:
            print(f"{err.__class__.__name__}: {err}")
            return (0, "Empty")


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


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(
                    isinstance(i, str)
                    and not isinstance(i, bool)
                    for i in data)
        else:
            return (isinstance(data, str)
                    and not isinstance(data, bool))

    def ingest(self, data:
               str | list[str]
               ) -> None:
        if self.validate(data):
            if isinstance(data, str):
                tup = (self._counter, str(data))
                self._data.append(tup)
                self._counter += 1
            else:
                for i in data:
                    tup = (self._counter, str(i))
                    self._data.append(tup)
                    self._counter += 1
        else:
            raise TypeError("Improper text data")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def is_valid_dict(item: Any) -> bool:
            return (
                set(item.keys()) == {"log_level", "log_message"}
                and
                all(isinstance(key, str) for key in item.keys())
                and
                all(isinstance(val, str) for val in item.values())
                )

        if isinstance(data, dict):
            return (is_valid_dict(data))

        if isinstance(data, list) and all(isinstance(item, dict) for item in data):
            return (all(is_valid_dict(item) for item in data))

        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")

        def store_log(log_entry: dict[str, str]):
            level = log_entry["log_level"]
            message = log_entry["log_message"]
            tup = (self._counter, level + ": " + message)
            self._data.append(tup)
            self._counter += 1

        if isinstance(data, list):
            for log_entry in data:
                store_log(log_entry)
        elif isinstance(data, dict):
            store_log(data)


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
    n = 3
    print(f"Extracting {n} values...")
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
    n = 1
    print(f"Extracting {n} value...")
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
            [{"k": "v", "a": "b"}, {"h": "w", "dict": 1}],
            [{"k": "v", "a": "b"}, {"h": "w", "d": "l"}, "hi"],
            {"k": "v", "a": "b", "h": "w"},
            [{"k": "v", "a": "b", "h": "w"}, {"h": "w", "d": "l"}],
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
    print(f"Extracting {n} values...")
    for _ in range(n):
        output = log_processor.output()
        print(f"Log entry {output[0]}: {output[1]}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    print("\n\n+++++++++++++++++++++++++")
    print("Testing Numeric Processor...\n")
    numeric_processor_test()

    print("\n\n+++++++++++++++++++++++++\n")
    print("Testing Text Processor...")
    text_processor_test()

    print("\n\n+++++++++++++++++++++++++\n")
    print("Testing Log Processor...")
    log_processor_test()


if __name__ == "__main__":
    main()
