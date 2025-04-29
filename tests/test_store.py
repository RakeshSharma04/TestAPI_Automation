import pytest
from api.store_api import StoreAPI
from payloads.order_payload import create_sample_order
from responses.save_response import save_response_to_file


@pytest.fixture(scope="module")
def store_api():
    return StoreAPI()


def test_get_inventory(store_api):
    response = store_api.get_inventory()
    assert response.status_code == 200
    save_response_to_file(response, 'inventory_response.json')


def test_create_order(store_api):
    payload = create_sample_order()
    response = store_api.create_order(payload)
    assert response.status_code == 200 # assert if status is 200
    save_response_to_file(response, 'create_order_response.json')
