from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

class PersonInfo(models.Model):
    full_name = models.CharField(max_length=100)
    contact_regex = RegexValidator(regex=r'^[1-9]\d{9}$',
        message="Phone number should be of 10 digits.")
    contact_no = models.CharField(validators=[contact_regex], max_length=10)
    payment_status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    amount = models.IntegerField(default=10)

    def __str__(self):
        return self.full_name

class Order(models.Model):
    order_id = models.CharField(max_length=50)
    person = models.ForeignKey(PersonInfo, related_name='persons', on_delete=models.CASCADE)

    def __str__(self):
        return self.person.full_name

class PaymentHistory(models.Model):
    person = models.ForeignKey(PersonInfo, related_name='person', on_delete=models.CASCADE)
    ORDERID = models.CharField(max_length=30)
    TXNID = models.CharField(max_length=64)
    BANKTXNID = models.CharField(max_length=100, null=True, blank=True)
    TXNAMOUNT = models.CharField(max_length=10)
    CURRENCY = models.CharField(max_length=4, null=True, blank=True)
    STATUS = models.CharField(max_length=12)
    RESPCODE = models.CharField(max_length=10)
    RESPMSG = models.TextField(max_length=250)
    TXNDATE = models.DateTimeField(default=timezone.now)
    GATEWAYNAME = models.CharField(max_length=30, null=True, blank=True)
    BANKNAME = models.CharField(max_length=50, null=True, blank=True)
    PAYMENTMODE = models.CharField(max_length=10, null=True, blank=True)
    MID = models.CharField(max_length=40)
    TXNTYPE = models.CharField(max_length=5, null=True, blank=True)
    REFUNDAMT = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.person.full_name
