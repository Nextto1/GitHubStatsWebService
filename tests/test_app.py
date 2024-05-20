# Import the unittest module and the create_app function from the app package
import unittest
from app import create_app

# Define a test case class inheriting from unittest.TestCase
class TestApp(unittest.TestCase):
    # Method to set up the test environment
    def setUp(self):
        # Create an instance of the Flask application
        self.app = create_app()
        # Create a test client for the Flask application
        self.client = self.app.test_client()

    # Method to test the index route
    def test_index(self):
        # Send a GET request to the index route
        response = self.client.get('/')
        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

# If this script is run directly, run the test cases
if __name__ == '__main__':
    unittest.main()