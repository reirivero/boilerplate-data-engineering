import unittest
from src.loading.load_data import load_data

class TestLoading(unittest.TestCase):
    def test_load_data(self):
        data = {'key': 'value'}
        result = load_data(data)
        self.assertIsNone(result)  # Asumiendo que la función no retorna nada

if __name__ == '__main__':
    unittest.main()
