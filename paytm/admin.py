from django.contrib import admin
from .models import Order, PlayersInfo, PaymentHistory

admin.site.register(Order)
admin.site.register(PaymentHistory)
admin.site.register(PlayersInfo)
