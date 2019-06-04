from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_page, name='start_page'),
    path('url_list_1/', views.url_list_1, name='url_list_1'),
    path('url_list_2/', views.url_list_2, name='url_list_2'),
    path('url_list_3/', views.url_list_3, name='url_list_3'),
    path('<int:url_number>/starshine0/', views.star_shine0, name='star_shine0'),
    path('<int:url_number>/starshine1/', views.star_shine1, name='star_shine1'),
    path('<int:url_number>/starshine2/', views.star_shine2, name='star_shine2'),
    path('<int:url_number>/starshine3/', views.star_shine3, name='star_shine3'),
    path('star/<int:url_number>/', views.star, name='star'),
    path('new_star/<int:url_number>/', views.new_star, name='new_star'),
    path('women/<int:pk>/', views.women_list, name='women_list'),
    path('test1/', views.test1, name='test1'),
    path('test2/<str:aaa>/<str:bbb>/', views.test2, name='test2'),
    path('test3/', views.test3, name='test3'),
]
