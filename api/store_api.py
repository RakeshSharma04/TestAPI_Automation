import requests
from utils.headers import get_api_key_header

class StoreAPI:
    BASE_URL = "https://petstore.swagger.io/v2"

    def __init__(self):
        self.headers = get_api_key_header()

    def get_inventory(self):
        url = f"{self.BASE_URL}/store/inventory"
        response = requests.get(url, headers=self.headers)
        return response

    def create_order(self, order_payload):
        url = f"{self.BASE_URL}/store/order"
        response = requests.post(url, headers=self.headers, json=order_payload)
        return response
