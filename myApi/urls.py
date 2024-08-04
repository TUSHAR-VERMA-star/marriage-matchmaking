from django.urls import path
from .views import UserListCreateAPIView, UserDetailAPIView, UserMatchAPIView

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('users/<int:pk>/matches/', UserMatchAPIView.as_view(), name='user-match'),
]
