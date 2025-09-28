import unittest
from app import app

class PlusApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_17(self):
        response = self.app.get('/is_prime/17')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertAlmostEqual(data['message'], True)

    def test_36(self):
        response = self.app.get('/is_prime/36')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertAlmostEqual(data['message'], False)

    def test_13219(self):
        response = self.app.get('/is_prime/13219')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertAlmostEqual(data['message'], True)

if __name__ == '__main__':
    unittest.main()
