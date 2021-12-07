import logging
from typing import Optional

import requests
from decouple import config

logger = logging.getLogger(__name__)


class APIHandler:
    """Handle making API calls to revel"""

    def __init__(self, baseURL: str):
        self.baseURL = baseURL
        self.order_item: Optional[dict] = None
        self.headers = {
            'Accept': 'appliction/json',
            'API-AUTHENTICATION': config('apikey')
        }

    def request_for_establishments(self, url=None, last_id=None, use_param=True, batch_size=500):
        """Make a request to get all Orders from Revel, with specified fields, or all
        if no field is specified.
        """
        request_params = {
            "format": "json",
            "limit": batch_size if batch_size < 100 else 100,
            "order_by": "id"
        }
        if last_id:
            request_params["id__gt"] = last_id

        request_url = url or '/enterprise/Establishment/'

        response_object = []

        if use_param:
            r = self._request_item(request_url, params=request_params)
        else:
            r = self._request_item(request_url)

        response_meta_info = r.get("meta")
        for data in r.get("objects"):
            response_object.append(data)
            if len(response_object) >= batch_size:
                break

        if len(response_object) < batch_size and response_meta_info.get("next"):
            request_url = response_meta_info.get("next")
            self.request_for_establishments(url=request_url, use_param=False)

        return response_object

    def _request_item(self, url, *args, **kwargs):
        request_url = f'{self.baseURL}{url}'
        r = requests.get(request_url, headers=self.headers, *args, **kwargs)
        return r.json()
