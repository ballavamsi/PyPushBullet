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

    
    def send_attachment(self, file_name, file_path):
        if os.path.exists(file_path) is False:
            logger.error(f"File {file_path} does not exist")
            return {
                "error": "File does not exist",
                "status": 400
            }
        
        # get file type
        file_type = file_name.split(".")[-1]
        if file_type not in ["png", "jpg", "jpeg", "gif"]:
            logger.error(f"File type {file_type} is currently not supported")
            return {
                "error": "File type is not currently supported, Try with png, jpg, jpeg or gif",
                "status": 400
            }
        
        # api call file_type create it
        file_type = f'image/{file_type}'

        with open(file_path, "rb") as file:
            res = self.session.post(self.base_url + "upload-request",
                                    json={
                                        "file_name": file_name,
                                        "file_type": file_type
                                    })
            if res.status_code == 200:
                response = res.json()
                upload_url = response['upload_url']
                file_url = response['file_url']
                file_data = response['data']
                res = requests.post(upload_url, data=file_data, files={'file': file})
                if res.status_code == 204:
                    res = self.session.post(self.base_url + "pushes",
                                            json={
                                                "type": "file",
                                                "file_name": file_name,
                                                "file_type": file_type,
                                                "file_url": file_url
                                            })
                    if res.status_code == 200:
                        logger.info("File sent")
                        return {
                            "status": 200
                        }
                    else:
                        logger.error(f"Error while sending image: {res.text}")
                        return {
                            "error": res.text,
                            "status": res.status_code
                        }
                else:
                    logger.error(f"Error while uploading image: {res.text}")
                    return {
                        "error": res.text,
                        "status": res.status_code
                    }
            else:
                logger.error(f"Error while getting upload url: {res.text}")
                return {
                    "error": res.text,
                    "status": res.status_code
                }
