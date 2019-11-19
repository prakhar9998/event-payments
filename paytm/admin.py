from django.contrib import admin
from .models import Order, PlayersInfo, PaymentHistory

class PlayersInfoAdmin(admin.ModelAdmin):
    list_display=(
        'leader_fullname',
        'payment_status',
        'created_date',
        'modified_date',)

class PaymentHistoryAdmin(admin.ModelAdmin):
    list_display=(
        'team',
        'STATUS',
    )

admin.site.register(Order)
admin.site.register(PaymentHistory, PaymentHistoryAdmin)
admin.site.register(PlayersInfo, PlayersInfoAdmin)
