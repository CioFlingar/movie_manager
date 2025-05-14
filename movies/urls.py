from django.urls import path, include
from rest_framework import routers
from .views import MovieViewSet, ActionViewSet

router = routers.SimpleRouter()
router.register(r"movies", MovieViewSet, basename="movies")
router.register(r"action", ActionViewSet, basename="action")



urlpatterns = [
    path("", include(router.urls)),
]
