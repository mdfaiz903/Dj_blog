
from django.urls import path
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from .views import loginuser,logoutUser,signupView,profileView,Pass_change,activate
urlpatterns = [

    path('Pass_change/',Pass_change,name='Pass_change'),
    path('activate/<uidb64>/<token>/',activate,name='activate'),
    path('login/',loginuser,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('signup/',signupView,name='signup'),
    path('profile/',profileView.as_view(),name='profile'),
    path('accounts/password_reset/ ',PasswordResetView.as_view(template_name='user/password_reset.html'),name='password_reset'),
    path('accounts/password_reset/done/',PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),name='password_reset_confirm'),
    path('accounts/reset/done/',PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),name='password_reset_complete'),

]