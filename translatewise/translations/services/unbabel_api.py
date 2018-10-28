import json
import requests
from config import Config


class UnbabelApi(object):

    def __init__(self,
                 username: str = Config.UNBABEL_API_USERNAME,
                 api_key: str = Config.UNBABEL_API_KEY):

        self.username = username
        self.api_key = api_key
        self.base_url = "https://sandbox.unbabel.com/tapi/v2"
        self.headers = {
            'Authorization': f"ApiKey {self.username}:{self.api_key}",
            'Content-Type': 'application/json'
        }

    def post_translation(self,
                         text: str,
                         uid: str,
                         source_language: str,
                         target_language: str,
                         callback_url=None):

        payload = {k: v for k, v in locals().items() if v not in (self, None)}
        url = f'{self.base_url}/translation/'
        result = requests.post(url, data=json.dumps(payload), headers=self.headers)

        if result.status_code not in range(200, 204):
            raise Exception("Unexpected Error:", result.content)

        return result.json()

    def fetch_translation(self, uid: str):
        url = f'{self.base_url}/translation/{uid}/'
        result = requests.get(url, headers=self.headers)

        if result.status_code not in range(200, 204):
            raise Exception("Unexpected Error:", result.content)

        return result.json()
