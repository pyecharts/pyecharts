import inspect
import json
import os

import requests

ENV_KEY_API_ENDPOINT = "SCRIPTHON_API_ENDPOINT"
ENV_KEY_API_TOKEN = "SCRIPTHON_API_TOKEN"

DEFAULT_API_KEY = "pyecharts-0-5-0-rocks"
DEFAULT_API_EP = "https://infinite-headland-27281.herokuapp.com/translate"


class Python2Javascript:
    @staticmethod
    def translate(obj):
        source_lines, _ = inspect.getsourcelines(obj)
        endpoint = os.environ.get(ENV_KEY_API_ENDPOINT, DEFAULT_API_EP)
        api_token = os.environ.get(ENV_KEY_API_TOKEN, DEFAULT_API_KEY)
        headers = {
            "Content-Type": "application/json",
            "Authorization": api_token,
        }
        r = requests.post(
            endpoint,
            headers=headers,
            data=json.dumps({"source": "".join(source_lines)}),
        )
        if r.status_code == 200:
            content = r.json()
            return content["response"]

        else:
            raise IOError("Cannot connect to the online compiler")
