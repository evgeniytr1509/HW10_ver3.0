from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'), #http://127.0.0.1:8000/register/
    path('login/', views.user_login, name='login'),
    path('quotes/', views.quotes, name='quotes'),
    path('add_author/', views.add_author, name='add_author'),  
    path('', views.quotes, name='quotes'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('all_authors/', views.all_authors, name='all_authors'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('quotes/', views.quotes, name='quotes'), # поиск по цитатам
    path('quotes/<str:tag>/', views.quotes_by_tag, name='quotes_by_tag'),
]