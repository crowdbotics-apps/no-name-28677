from rest_framework import serializers
from wallet.models import (
    PaymentTransaction,
    TaskerPaymentAccount,
    CustomerWallet,
    PaymentMethod,
    TaskerWallet,
)


class TaskerPaymentAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskerPaymentAccount
        fields = "__all__"


class TaskerWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskerWallet
        fields = "__all__"


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = "__all__"


class PaymentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTransaction
        fields = "__all__"


class CustomerWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerWallet
        fields = "__all__"
