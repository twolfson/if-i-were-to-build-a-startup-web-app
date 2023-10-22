from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),,
    # TODO: Explore what this means
    path("api-auth/", include("rest_framework.urls"))
]
