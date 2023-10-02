import unittest
from logger import Logger

class TestLogger(unittest.TestCase):
    def test_log(self):
        logger = Logger()
        logger.log("Test message")
        # Assert that the message was logged successfully
        self.assertIn("Test message", logger.get_logs())
