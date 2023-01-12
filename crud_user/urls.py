from django.urls import path
from .api import user_api_view,user_detail_api_view
from .views import Login, Logout

urlpatterns = [
    path('users/', user_api_view, name= 'user_list' ),
    path('users/<int:pk>/',user_detail_api_view, name= 'user_detail_view' ),
]
