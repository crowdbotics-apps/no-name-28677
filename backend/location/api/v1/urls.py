from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    MapLocationViewSet,
    CustomerLocationViewSet,
    TaskerLocationViewSet,
    TaskLocationViewSet,
)

router = DefaultRouter()
router.register("maplocation", MapLocationViewSet)
router.register("customerlocation", CustomerLocationViewSet)
router.register("tasklocation", TaskLocationViewSet)
router.register("taskerlocation", TaskerLocationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
