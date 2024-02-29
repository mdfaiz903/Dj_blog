from django.urls import path
from.views import homeView,PostDetails,PostCreate,PostUpdateView,post_delete,searchView
urlpatterns = [

    path('',homeView.as_view(),name='home'),
    path('postdetails/<int:pk>',PostDetails.as_view(),name='postdetails'),
    path('post-create/',PostCreate.as_view(),name='post-create'),
    path('post/<int:pk>/Delete/',post_delete.as_view(),name='post_delete'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post_update'),
    path('search/',searchView,name='search'),
  
]
