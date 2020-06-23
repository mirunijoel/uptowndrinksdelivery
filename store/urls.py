from django.urls import path

from . import views

urlpatterns = [
    # Leave as empty string for base url
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('product/<int:pk>/', views.product_view, name="product"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    # need to double check the below code
    path('sign_up/', views.sign_up, name='user_sign'),
    path('process_order/', views.processOrder, name="process_order"),

]
