from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from horsemanshop.shop.permissions import IsOwner


class IsOwnerPermissionsMixin:
    permission_classes = [
        IsOwner
    ]


class IsAuthenticatedOrReadOnlyPermissionsMixin:
    permission_classes = [
        IsAuthenticatedOrReadOnly
    ]


class IsAuthenticatedPermissionsMixin:
    permission_classes = [
        IsAuthenticated
    ]
