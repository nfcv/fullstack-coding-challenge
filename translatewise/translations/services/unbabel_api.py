import json
import requests


class UnbabelApi(object):

    def __init__(self, username: str, api_key: str):
        self.username = username
        self.api_key = api_key
        self.base_url = "https://sandbox.unbabel.com/tapi/v2"
        self.headers = {
            'Authorization': f"ApiKey {self.username}:{self.api_key}",
            'Content-Type': 'application/json'
        }

    def post_translation(self,
                         text: str,
                         source_language: str,
                         target_language: str,
                         callback_url=None):

        payload = {k: v for k, v in locals().items() if v not in (self, None)}
        url = f'{self.base_url}/translation/'
        result = requests.post(url, data=json.dumps(payload), headers=self.headers)

        if result.status_code not in (201, 202):
            raise Exception("Unexpected Error:", result.content)

        return result.json()
