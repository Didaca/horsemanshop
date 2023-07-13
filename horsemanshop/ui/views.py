from django.views import generic
from django.contrib.auth.models import User
from rest_framework import generics, permissions

from horsemanshop.shop.models import Article
from horsemanshop.ui.serializers import UsersSerializer, UserSerializer


class HomePageView(generic.TemplateView):
    template_name = "home.html"


class ArticleDetailsView(generic.DetailView):
    queryset = Article.objects.all()
    template_name = 'details.html'


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [
        permissions.IsAdminUser
    ]


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAdminUser
    ]
