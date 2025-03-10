from abc import ABC, abstractmethod


# Abstract Base Class (ABC) for FileHandler
class FileHandler(ABC):

    @abstractmethod
    def read(self, file_path):
        pass

    @abstractmethod
    def write(self, file_path, data):
        pass


# Concrete class for handling text files
class TextFileHandler(FileHandler):

    def read(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()

    def write(self, file_path, data):
        with open(file_path, 'w') as file:
            file.write(data)


# Concrete class for handling binary files
class BinaryFileHandler(FileHandler):

    def read(self, file_path):
        with open(file_path, 'rb') as file:
            return file.read()

    def write(self, file_path, data):
        with open(file_path, 'wb') as file:
            file.write(data)


# Demonstration
if __name__ == "__main__":
    # Text file handling
    text_handler = TextFileHandler()
    text_handler.write("file.pdf", "You are opening a read only PDF file.")
    print(text_handler.read("file.pdf"))  # Output: You are opening a read only PDF file.

    # Binary file handling
    binary_handler = BinaryFileHandler()
    binary_data = b'\x00\x01\x02\x03'
    binary_handler.write("example.bin", binary_data)
    print(binary_handler.read("example.bin"))  # Output: b'\x00\x01\x02\x03'