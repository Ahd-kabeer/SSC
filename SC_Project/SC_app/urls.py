from django.urls import path
from SC_app import views
urlpatterns = [
    path('index',views.index,name='index'),
    path('',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('logout',views.signout,name='logout'),
    path('form',views.Book_rooms,name='form'),
    
]