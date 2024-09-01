import unittest
from src.extraction.extract_data import extract_from_source_1, extract_from_source_2

class TestExtraction(unittest.TestCase):
    def test_extract_from_source_1(self):
        data = extract_from_source_1()
        self.assertIsNotNone(data)

    def test_extract_from_source_2(self):
        data = extract_from_source_2()
        self.assertIsNotNone(data)

if __name__ == '__main__':
    unittest.main()
