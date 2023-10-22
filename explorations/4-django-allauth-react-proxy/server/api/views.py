from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from api.serializers import UserSerializer


# TODO: Prob want to only allow users within same group, or even just self
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    For now, limited to user themself
    """
    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(pk=user.pk)
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Support "me` as pk, https://stackoverflow.com/a/36626403/1960509
    def get_object(self):
        pk = self.kwargs.get('pk')

        if pk == "me":
            return self.request.user

        return super().get_object()
