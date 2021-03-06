from django.contrib import admin
from .models import (
    PaymentTransaction,
    TaskerPaymentAccount,
    CustomerWallet,
    PaymentMethod,
    TaskerWallet,
)

admin.site.register(TaskerPaymentAccount)
admin.site.register(TaskerWallet)
admin.site.register(PaymentMethod)
admin.site.register(PaymentTransaction)
admin.site.register(CustomerWallet)

# Register your models here.
