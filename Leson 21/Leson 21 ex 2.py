import os
import unittest
from unittest.mock import patch
from Leson_21_ex_1 import FileHandler



class TestFileHandler(unittest.TestCase):
    FILE_PATH = "test.txt"

    def setUp(self):
        with open(self.FILE_PATH, "w") as f:
            f.write("")

    def tearDown(self):
        os.remove(self.FILE_PATH)
        os.remove("log.txt")

    def test_write(self):
        with FileHandler(self.FILE_PATH, "w") as f:
            f.write("Test line")
        with open(self.FILE_PATH) as f:
            content = f.read()
        self.assertEqual(content, "Test line")

    def test_read(self):
        with open(self.FILE_PATH, "w") as f:
            f.write("Test line")
        with FileHandler(self.FILE_PATH, "r") as f:
            content = f.read()
        self.assertEqual(content, "Test line")

    def test_exit(self):
        with FileHandler(self.FILE_PATH, "w") as f:
            f.write("Test line")
        with patch("builtins.open", side_effect=Exception("Mocked exception")):
            with self.assertRaises(Exception):
                f.__exit__(None, None, None)

    def test_log(self):
        with FileHandler(self.FILE_PATH, "w") as f:
            f.write("Test line")
        with open("log.txt") as f:
            content = f.read()
        self.assertTrue("Test line" in content)
        self.assertTrue(self.FILE_PATH in content)
        self.assertTrue("1 lines written" in content)

    def test_multiple_writes(self):
        with FileHandler(self.FILE_PATH, "w") as f:
            f.write("Line 1")
            f.write("Line 2")
        with open(self.FILE_PATH) as f:
            content = f.read()
        self.assertEqual(content, "Line 1Line 2")

    def test_write_count(self):
        with FileHandler(self.FILE_PATH, "w") as f:
            f.write("Line 1")
            f.write("Line 2")
        self.assertEqual(f.counter, 2)

    def test_read_non_existing_file(self):
        with self.assertRaises(FileNotFoundError):
            with FileHandler("non_existing_file.txt", "r") as f:
                f.read()

    def test_read_closed_file(self):
        with FileHandler(self.FILE_PATH, "w") as f:
            f.write("Test line")
        f.file.close()
        with self.assertRaises(ValueError):
            f.read()

    def test_write_closed_file(self):
        with FileHandler(self.FILE_PATH, "w") as f:
            f.file.close()
            with self.assertRaises(ValueError):
                f.write("Test line")


if __name__ == "__main__":
    unittest.main()