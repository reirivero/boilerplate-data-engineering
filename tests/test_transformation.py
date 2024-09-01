import unittest
from src.transformation.transform_data import transform_data

class TestTransformation(unittest.TestCase):
    def test_transform_data(self):
        data = {'key': 'value'}
        transformed_data = transform_data(data)
        self.assertIsNotNone(transformed_data)

if __name__ == '__main__':
    unittest.main()
