import requests
import logging
import os

# Create a logger for this module
logger = logging.getLogger(__name__)
# Configure logging
logging.basicConfig(level=logging.INFO)

class PushBullet:
    def __init__(self, api_key=None):
        if api_key is None:
            # If no API key is provided, check for an environment variable
            api_key = os.environ.get("PUSHBULLET_API_KEY")
            if api_key is None:
                raise ValueError("API key is not provided and PUSHBULLET_API_KEY environment variable is not set")

        self.api_key = api_key
        self.base_url = "https://api.pushbullet.com/v2/"
        self.session = requests.Session()
        self.session.headers.update({
            "Access-Token": api_key,
            "Content-Type": "application/json"
        })
        logger.info(f'Initialized Pushbullet client with API key: {api_key}')

    def send_notification(self, title, body):
        data = {
            "type": "note",
            "title": title,
            "body": body
        }
        try:
            response = self.session.post(self.base_url + "pushes", json=data)
            response.raise_for_status()
            # Log the successful notification
            logger.info(f'Successfully sent notification: {title}')
        except requests.exceptions.RequestException as e:
            # Log any request-related errors
            logger.error(f'Failed to send notification: {title}. Error: {e}')
