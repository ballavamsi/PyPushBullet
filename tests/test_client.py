import unittest
from client import Client

class TestClient(unittest.TestCase):
    def test_send_message(self):
        client = Client()
        response = client.send_message("Test message")
        # Assert that the response is correct
        self.assertEqual(response, "Message sent successfully")