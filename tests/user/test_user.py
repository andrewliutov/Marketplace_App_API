from rest_framework.status import HTTP_200_OK
import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_create_user(api_client):
    """Тест создания пользователя"""
    url = reverse('user-register')
    user = {"first_name": "Имя2",
            "last_name": "Фамилия2",
            "email": "test@test.com",
            "password": "1234567890qwerty",
            "company": "Sony",
            "position": "Supervisor"
            }
    resp = api_client.post(url, user)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert resp_json['Status'] == True


@pytest.mark.django_db
def test_add_contact(simple_user_client):
    """Тест добавления контактов пользователя"""
    url = reverse('user-contact')
    contact = {"city": "Город2", "street": "Улица3", "phone": "+0123456789"}
    resp = simple_user_client.post(url, contact)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert resp_json['Status'] == True
