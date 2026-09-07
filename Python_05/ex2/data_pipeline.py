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
        if self.data:
            extracted_data = self.data.pop(0)
            return extracted_data
        else:
            raise Exception("Data is empty")


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExportPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        output = []
        for tup in data:
            output.append(tup[1])
        processed_output = ",".join(output)
        print(processed_output)


class JSONExportPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        output = []
        for tup in data:
            string = f'"item_{tup[0]}": "{tup[1]}"'
            output.append(string)
        processed_output = f"{{{", ".join(output)}}}"
        print(processed_output)


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
        print("\n== DataStream statistics ==")
        if not self.registered_processors:
            print("No processor found, no data")
        else:
            for processor in self.registered_processors:
                print(
                    f"{processor.name}: total "
                    f"{processor.index} items processed, "
                    f"remaining {len(processor.data)} on processor"
                    )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.registered_processors:
            processed_data: list[tuple[int, str]] = []
            for _ in range(nb):
                try:
                    tup = processor.output()
                    processed_data.append(tup)
                except Exception:
                    pass
            try:
                do_plugin(plugin, processed_data)
            except Exception as err:
                print(f"Invalid plugin: {err}")


def do_plugin(plugin: ExportPlugin, data: list[tuple[int, str]]) -> None:
    plugin.process_output(data)


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

    data_1 = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
            'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO',
                'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
        ]

    print(f"\nSend first batch of data on stream: {data_1}")
    data_stream.process_stream(data_1)
    data_stream.print_processors_stats()

    nb = 3
    print(f"\nSend {nb} processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()

    data_stream.output_pipeline(nb, csv_plugin)
    data_stream.print_processors_stats()

    data_2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR',
            'log_message': '500 server crash'},
            {'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'}],
        [32, 42, 64, 84, 128, 168],
        'World hello'
        ]

    print(f"\nSend another batch of data: {data_2}\n")
    data_stream.process_stream(data_2)
    data_stream.print_processors_stats()

    nb = 5
    print(f"\nSend {nb} processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()

    data_stream.output_pipeline(nb, json_plugin)
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
