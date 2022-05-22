from django.urls import re_path
from django.urls import include
from rest_framework.routers import DefaultRouter
from store import views

app_name = "store"

router = DefaultRouter()

router.register(r'store', views.productsViewset)

urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'index',views.index),
    re_path(r'products',views.products),
    re_path(r'product/(?P<product>[-\w]+)/$',views.product),
    re_path(r'product/buy-product',views.ProductAPIView.buy_product)
    
    
]
