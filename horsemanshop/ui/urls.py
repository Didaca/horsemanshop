from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from horsemanshop.ui.views import HomePageView, ArticleDetailsView, UserListView, UserDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('auth-token/', obtain_auth_token, name='auth_token'),
    path('article/<int:pk>/', ArticleDetailsView.as_view(), name='details'),

    path('users/', UserListView.as_view(), name='users'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_details')
]
