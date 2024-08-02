from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('adidas/', views.adidas, name='adidas'),

    path('nike/', views.nike, name='nike'),

    path('jordan/', views.jordan, name='jordan'),

    path('puma/', views.puma, name='puma'),

    path('new_balance/', views.new_balance, name='new_balance'),
    
    path('vans/', views.vans, name='vans'),
    
    path('reebok/', views.reebok, name='reebok'),
    
    path('balenciaga/', views.balenciaga, name='balenciaga'),
    
    path('accounts/register/', views.register, name='register'), 
    
    path('accounts/login/', views.login, name='login'), #url to login user
    
    # path('login_or_register/', views.login_or_register, name='login_or_register'), 
    
    path('logout/', views.logout, name='logout'), #url to logout user
    
    path('search/', views.search, name='search'), #url to search product
    
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'), #url to display product details
    
    path('cart/', views.cart, name='cart'),
    
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'), #url to add item to cart

    path("cart_count/", views.cart_count, name = "cart_count"), #this is used to get the number of items in the cart
    
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'), #url to remove item from cart
    
    # path('update_cart/<int:id>/', views.update_cart, name='update_cart'),
    
    path('empty_cart', views.empty_cart, name='empty_cart'), #url to empty cart
    
    path('checkout', views.checkout, name='checkout'),
    
    path('favorite', views.favorite, name='favorite'), #url to display favorites
    
    path('add_to_favorite/<int:product_id>/', views.add_to_favorite, name='add_to_favorite'), #url to add item to favourites
    
    path('remove_from_favorite/<int:product_id>/', views.remove_from_favorite, name='remove_from_favorite'), #url to delete item from favoutites

    path('toggle_favorite/<int:product_id>/', views.toggle_favorite, name='toggle_favorite'), #toggle the favorite icon to add and remove product from favorite list
    
    path('discounted_products/', views.discounted_products, name='discounted_products'), #url to display discounted products

    path('trending/', views.trending, name = 'trending'),

    path('outdoor/', views.outdoor, name = 'outdoor'),

    path('new/', views.new, name = 'new'),

    path('create_order', views.create_order, name = 'create_order'), #this is to allow the user make an order

    path('order_details/<int:order_id>/', views.order_details, name='order_details'), #this is to display a user's order

    path('update_cart_item/<int:item_id>/', views.update_cart_item, name = 'update_cart_item'),
    
    path("orders/", views.orders, name = "orders"), #url to page to display orders

    path('send_message/', views.send_message, name='send_message'),

    path('add_product/', views.add_product, name='add_product'),


]
