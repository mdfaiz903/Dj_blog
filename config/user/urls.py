
from django.urls import path
from .views import loginuser,logoutUser,signupView,profileView
urlpatterns = [

    path('login/',loginuser,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('signup/',signupView,name='signup'),
    path('profile/',profileView.as_view(),name='profile'),

]