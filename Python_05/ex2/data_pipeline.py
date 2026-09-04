from abc import ABC, abstractmethod
from typing import Any, Protocol


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data: list[tuple[int, str]] = []
        self.index: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        try:
            extracted_data = self.data.pop(0)
            return extracted_data
        except Exception:
            return (-1, "Empty")


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass

class CSVPlugin(ExportPlugin):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print(data)
        output = []
        for item in data:
            output.append(item[1])
        print(output)
        

class DataStream():
    def __init__(self) -> None:
        self.registered_processors: list[Any] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.registered_processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        is_data_processed: bool = False
        for data in stream:
            for processor in self.registered_processors:
                if processor.validate(data):
                    processor.ingest(data)
                    is_data_processed = True
                    break
            if not is_data_processed:
                print(
                    "DataStream error - Can't process element in stream: "
                    f"{data}"
                    )
            is_data_processed = False

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.registered_processors:
            print("No processor found, no data")
        else:
            for processor in self.registered_processors:
                print(
                    f"{processor.name}: total "
                    f"{processor.index} items processed, "
                    f"remaining {len(processor.data)} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        pass



class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        self.name = "Numeric Processor"
        super().__init__()

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
                    tup = (self.index, str(item))
                    self.data.append(tup)
                    self.index += 1
            else:
                tup = (self.index, str(data))
                self.data.append(tup)
                self.index += 1

        else:
            raise TypeError("Improper numeric data")


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        self.name = "Text Processor"
        super().__init__()

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
                    tup = (self.index, item)
                    self.data.append(tup)
                    self.index += 1
            else:
                tup = (self.index, data)
                self.data.append(tup)
                self.index += 1

        else:
            raise TypeError("Improper text data")


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        self.name = "Log Processor"
        super().__init__()

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
            tup = (self.index, values)
            self.data.append(tup)
            self.index += 1

        if isinstance(data, list):
            for log_entry in data:
                _store_log(log_entry)
        elif isinstance(data, dict):
            _store_log(data)


def main() -> None:
    num_proc = NumericProcessor()
    txt_proc = TextProcessor()
    log_proc = LogProcessor()

    print("=== Code Nexus - Data Pipeline ===")

    print("\nInitialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("\nRegistering Processors")
    data_stream.register_processor(num_proc)
    data_stream.register_processor(txt_proc)
    data_stream.register_processor(log_proc)

    data = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
            'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO',
                'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
        ]

    print(f"\nSend first batch of data on stream: {data}\n")
    data_stream.process_stream(data)
    data_stream.print_processors_stats()

    nb = 3
    print(f"\nSend {nb} processed data from each processor to a CSV plugin:")
    csv_plugin = CSVPlugin()
    processed_data = []
    for _ in range(nb):
        processed_data.append(num_proc.output())
    csv_plugin.process_output(processed_data)
    # for _ in range(nb):
    #     txt_proc.output()
    # for _ in range(nb):
    #     log_proc.output()

    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
