from django.urls import path
from .views import homepage, CarDetailsView, buyNow

urlpatterns = [
    path('', homepage, name = 'homepage'),
    path('brand/<str:brand_slug>/', homepage, name = 'brand_wise_car'),
    path('details/<int:id>/', CarDetailsView.as_view(), name = 'car_details'),
    path('buy_now/<int:id>/', buyNow, name = 'buy_now'),
]