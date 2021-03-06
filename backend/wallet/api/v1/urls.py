from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    PaymentTransactionViewSet,
    TaskerPaymentAccountViewSet,
    CustomerWalletViewSet,
    PaymentMethodViewSet,
    TaskerWalletViewSet,
)

router = DefaultRouter()
router.register("taskerpaymentaccount", TaskerPaymentAccountViewSet)
router.register("taskerwallet", TaskerWalletViewSet)
router.register("paymentmethod", PaymentMethodViewSet)
router.register("paymenttransaction", PaymentTransactionViewSet)
router.register("customerwallet", CustomerWalletViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
