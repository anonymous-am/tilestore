from django.urls import path
from . import views

# create urls for views................
urlpatterns = [
    path('addProduct/', views.addProduct),
    path('addCategory/', views.addCategory),
    path('placeOrder/', views.placeOrder),
    path('fetchCategory/',views.getTilesCategory),
    path('fetchProduct/',views.getProduct),
    path('fetchProductDetail/',views.getProductdetail),

]


