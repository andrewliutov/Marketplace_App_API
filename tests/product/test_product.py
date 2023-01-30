from rest_framework.status import HTTP_200_OK
import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_get_category(category_factory, api_client):
    """Тест на получение категории товаров"""
    category1 = category_factory()
    category2 = category_factory()
    url = reverse('categories')
    resp = api_client.get(url)
    resp_json = resp.json()
    assert resp.status_code == HTTP_200_OK
    assert resp_json['count'] == 2


@pytest.mark.django_db
def test_product(api_client, product_factory, category_factory, product_info_factory, shop_factory):
    """Тест на получение списка товаров"""
    category = category_factory()
    product1 = product_factory(category_id=category.id)
    product2 = product_factory(category_id=category.id)
    shop = shop_factory()
    product_info = product_info_factory(product_id=product1.id, shop_id=shop.id)
    product_info2 = product_info_factory(product_id=product2.id, shop_id=shop.id)
    url = reverse('products')
    resp = api_client.get(url)
    resp_json = resp.json()
    assert resp.status_code == HTTP_200_OK
    assert len(resp_json) == 2
