from django.urls import path

from horsemanshop.ui.views import HomePageView, ArticleDetailsView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('article/<int:pk>/', ArticleDetailsView.as_view(), name='details')
]
