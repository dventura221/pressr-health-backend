from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('providers/', views.ProviderList.as_view(), name='provider_list'),
    path('providers/<int:pk>', views.ProviderDetail.as_view(),
         name='provider_detail'),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('readings/', views.ReadingList.as_view(), name='reading_list'),
    path('readings/<int:pk>', views.ReadingDetail.as_view(), name='reading_detail'),
    path('comments/', views.CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name='comment_detail')
]
