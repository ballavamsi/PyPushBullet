# PyPushBullet
[![PyPI Version](https://img.shields.io/pypi/v/PyPushBullet.svg)](https://pypi.org/project/PyPushBullet/)
[![License](https://img.shields.io/pypi/l/PyPushBullet.svg)](https://github.com/ballavamsi/PyPushBullet/blob/main/LICENSE)
**PyPushBullet** is a Python library for interacting with the PushBullet API, allowing you to send notifications, links, and files to your devices easily.
## Installation
You can install **PyPushBullet** via pip:
```bash
pip install PyPushBullet
```
## Usage
### Initializing the PushBullet Client
Before using the library, you need to initialize the PushBullet client with your API key. You can either provide the API key explicitly or set it as an environment ariable.

```python
    from PyPushBullet.client import PushBullet
    # Initialize with API key provided explicitly
    api_key = 'YOUR_PUSHBULLET_API_KEY'
    pb = PushBullet(api_key)
    # Alternatively, set the API key as an environment variable
    # export PUSHBULLET_API_KEY=YOUR_PUSHBULLET_API_KEY
    # Then, initialize without providing the API key
    pb = PushBullet()
```
### Sending Notifications
Once the client is initialized, you can use it to send notifications to your devices:
```python
    title = 'Hello'
    body = 'This is a test notification'
    pb.send_notification(title, body)
```
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
## Acknowledgments
- This library is not affiliated with or endorsed by PushBullet. It is an independent open-source project.
- Feel free to contribute to this project by opening issues and pull requests.
## Author
- BALLA VAMSI SRINIVAS
- GitHub: [ballavamsi](https://github.com/ballavamsi)
