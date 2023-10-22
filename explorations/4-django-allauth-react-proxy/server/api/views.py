from django.contrib.auth.models import User
from rest_framework import permissions, mixins, viewsets

from api.serializers import UserSerializer


# Direct mixins for viewset, https://stackoverflow.com/a/23649843/1960509
class UserViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    For now, limited to user themself.
    Also supposed `/users/me` syntax
    """

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(pk=user.pk)

    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Support "me` as pk, https://stackoverflow.com/a/36626403/1960509
    def get_object(self):
        pk = self.kwargs.get("pk")

        if pk == "me":
            return self.request.user

        return super().get_object()
