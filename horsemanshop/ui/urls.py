from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from horsemanshop.ui.views import HomePageView, ArticleDetailsView, UserListView, UserDetailView, UserArticlesListView, \
    CreateUserView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('auth-token/', obtain_auth_token, name='auth_token'),
    path('article/<int:pk>/', ArticleDetailsView.as_view(), name='details'),

    path('users/', UserListView.as_view(), name='users'),
    path('create-user/', CreateUserView.as_view(), name='user_create'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_details'),
    path('user-articles/', UserArticlesListView.as_view(), name='user_articles')
]
