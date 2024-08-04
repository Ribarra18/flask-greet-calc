import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_addition(self):
        response = self.app.get('/add?a=10&b=20')
        self.assertEqual(response.data.decode('utf-8'), '30')

    def test_subtraction(self):
        response = self.app.get('/sub?a=20&b=10')
        self.assertEqual(response.data.decode('utf-8'), '10')

    def test_multiplication(self):
        response = self.app.get('/mult?a=5&b=4')
        self.assertEqual(response.data.decode('utf-8'), '20')

    def test_division(self):
        response = self.app.get('/div?a=20&b=4')
        self.assertEqual(response.data.decode('utf-8'), '5.0')

    def test_division_by_zero(self):
        response = self.app.get('/div?a=10&b=0')
        self.assertEqual(response.data.decode('utf-8'), 'Error: Division by zero')

if __name__ == '__main__':
    unittest.main()
