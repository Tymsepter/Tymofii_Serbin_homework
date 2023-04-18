import time


class FileHandler:
    def __init__(self, file_path, mode):
        self.file = open(file_path, mode)
        self.counter = 0

    def write(self, text):
        self.file.write(text)
        self.counter += 1

    def read(self):
        self.file.seek(0)
        return self.file.read()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        with open('log.txt', 'a') as log_file:
            log_file.write(f"{time.ctime()}: {self.counter} lines written to {self.file.name}\n")


