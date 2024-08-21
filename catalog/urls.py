from urls import path
from .views import ProductViews

urlpatterns = [
    path('products', ProductViews.get_products),
    path('product/<str:id>', ProductViews.get_product_detail)
]
