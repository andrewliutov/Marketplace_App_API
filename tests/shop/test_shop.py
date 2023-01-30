from rest_framework.status import HTTP_200_OK
import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_get_shop(api_client, shop_factory):
    """Тест получения списка магазинов"""
    shop1 = shop_factory()
    shop2 = shop_factory()
    url = reverse('shops-list')
    resp = api_client.get(url)
    resp_json = resp.json()
    assert resp.status_code == HTTP_200_OK
    assert resp_json['count'] == 2
