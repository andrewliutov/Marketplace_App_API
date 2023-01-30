"""market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm
from users.views import RegisterAccount, ConfirmAccount, AccountDetails, ContactView, LoginAccount
from shop.views import ShopViewSet, PartnerUpdateView, PartnerStateViewSet, PartnerOrdersView
from product.views import ProductInfoView, CategoryView
from order.views import BasketView, OrderView

router = DefaultRouter()

router.register('shops', ShopViewSet, basename='shops')
router.register('partner/state', PartnerStateViewSet, basename='partner-state')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/register', RegisterAccount.as_view(), name='user-register'),
    path('user/register/confirm', ConfirmAccount.as_view(),
         name='user-register-confirm'),
    path('user/details', AccountDetails.as_view(), name='user-details'),
    path('user/contact', ContactView.as_view(), name='user-contact'),
    path('user/login', LoginAccount.as_view(), name='user-login'),
    path('user/password_reset', reset_password_request_token, name='password-reset'),
    path('user/password_reset/confirm', reset_password_confirm,
         name='password-reset-confirm'),

    path('products', ProductInfoView.as_view(), name='products'),
    path('categories', CategoryView.as_view(), name='categories'),

    path('partner/update', PartnerUpdateView.as_view(), name='partner-update'),
    path('partner/orders', PartnerOrdersView.as_view(), name='partner-orders'),

    path('basket', BasketView.as_view(), name='basket'),
    path('order', OrderView.as_view(), name='order'),

    path('api/v1/', include(router.urls))
]
