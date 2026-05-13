from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),

    path('login/', views.user_login, name='login'),

    path('register/', views.register, name='register'),

    path('logout/', views.user_logout, name='logout'),

    path('products/', views.products, name='products'),

    #path('buy/<int:id>/',views.buy_product,name='buy_product'),

    path('success/',views.success,name='success'),

    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),

    path('testimonials/',views.testimonials,name='testimonials'),

    path('buy/<str:product_name>/',views.buy_product,name='buy_product'),
    path('order-success/', views.order_success, name='order_success'),

    path('my-orders/',views.my_orders,name='my_orders'),
    path('success/',views.success,name='success'),
    path('seller-register/',views.seller_register,name='seller_register'),
    path('seller-profile/',views.seller_profile,name='seller_profile'),

    path('seller-login/',views.seller_login,name='seller_login'),

path('seller-dashboard/',views.seller_dashboard,name='seller_dashboard'),

path(
    'accept-order/<int:order_id>/',
    views.accept_order,
    name='accept_order'
),

path(
    'reject-order/<int:order_id>/',
    views.reject_order,
    name='reject_order'
),

path(

    'accepted-orders/',

    views.accepted_orders,

    name='accepted_orders'

),


######################
path(
    'track-order/<int:order_id>/',
    views.track_order,
    name='track_order'
),

path(
    'received-order/<int:order_id>/',
    views.received_order,
    name='received_order'
),
####################

path('contact/', views.contact_page, name='contact'),
]