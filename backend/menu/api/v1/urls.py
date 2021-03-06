from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    ReviewViewSet,
    CategoryViewSet,
    ItemViewSet,
    CountryViewSet,
    ItemVariantViewSet,
)

router = DefaultRouter()
router.register("category", CategoryViewSet)
router.register("item", ItemViewSet)
router.register("review", ReviewViewSet)
router.register("itemvariant", ItemVariantViewSet)
router.register("country", CountryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
