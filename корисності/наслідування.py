import abc
import json


class Writer(abc.ABC):

    @abc.abstractmethod
    def write(self, *lines: str, end: str = "\n", sep=" "):
        raise NotImplemented()


class ConsoleWriter(Writer):
    def write(self, *lines: str, end: str = "\n", sep=" "):
        print(*lines, end=end, sep=sep)


a = ConsoleWriter()
a.write("Hello, 12345", "!")


class TextFileWriter(Writer):
    def write(self, *lines: str, end: str = "\n", sep=" "):
        with open("Hello.txt", "w") as file_object:
            file_object.write(sep.join(lines) + end)


a = TextFileWriter()
a.write("Hello, 12345", "!")


class JsonWriter(Writer):
    def write(self, *lines: str, end: str = "\n", **kwargs):
        with open("output.json", "w") as f:
            json.dump(lines, f, **kwargs)
        print(f"Data written to output.json{end}")


writer = JsonWriter()
data = {"name": "Tymofii", "city": "Ruzomberok"}
writer.write(data, indent=4)
