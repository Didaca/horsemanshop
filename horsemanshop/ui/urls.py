from django.urls import path

from horsemanshop.ui.views import HomePageView, ArticleDetailsView, UserListView, UserDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('article/<int:pk>/', ArticleDetailsView.as_view(), name='details'),

    path('users/', UserListView.as_view(), name='users'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_details')
]
