import pytest
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from model_bakery import baker


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def simple_user_client():
    User = get_user_model()
    user = User.objects.create_user(
        'user123@mail.ru', '1234567890qwerty')
    token = Token.objects.get_or_create(user_id=user.id)
    list_token = list(token)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + list_token[0].key)
    return client


@pytest.fixture
def shop_factory():
    def factory(**kwargs):
        return baker.make('Shop', **kwargs)
    return factory


@pytest.fixture
def product_factory():
    def factory(**kwargs):
        return baker.make('Product', **kwargs)
    return factory


@pytest.fixture
def product_info_factory():
    def factory(**kwargs):
        return baker.make('ProductInfo', **kwargs)
    return factory


@pytest.fixture
def category_factory():
    def factory(**kwargs):
        return baker.make('Category', **kwargs)
    return factory
