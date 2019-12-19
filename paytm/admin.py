from django.contrib import admin
from .models import Order, PersonInfo, PaymentHistory

class PersonInfoAdmin(admin.ModelAdmin):
    list_display=(
        'full_name',
        'payment_status',
        'created_date',
        'modified_date',
    )

class PaymentHistoryAdmin(admin.ModelAdmin):
    list_display=(
        'person',
        'STATUS',
        'TXNAMOUNT',
    )

admin.site.register(Order)
admin.site.register(PaymentHistory, PaymentHistoryAdmin)
admin.site.register(PersonInfo, PersonInfoAdmin)
