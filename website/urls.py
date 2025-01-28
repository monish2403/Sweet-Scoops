from django.urls import path
from website import views
urlpatterns = [
    
    path('', views.home),
    path('register/', views.user_register),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout),
    path('menu/', views.user_menu, name='menu_details'),
    path('ingridient/', views.user_ingridient),
]
