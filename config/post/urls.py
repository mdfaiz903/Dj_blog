from django.urls import path
from.views import homeView,PostDetails
urlpatterns = [
    path('',homeView.as_view(),name='home'),
    path('postdetails/<int:pk>',PostDetails.as_view(),name='postdetails'),
]
