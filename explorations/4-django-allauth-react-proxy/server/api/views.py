from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets

from api.serializers import UserSerializer, GroupSerializer


# TODO: Prob want to only allow users within same group, or even just self
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Support "me` as pk, https://stackoverflow.com/a/36626403/1960509
    def get_object(self):
        pk = self.kwargs.get('pk')

        if pk == "me":
            return self.request.user

        return super().get_object()


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
