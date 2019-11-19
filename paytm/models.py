from django.db import models
from django.utils import timezone

class PlayersInfo(models.Model):
    leader = models.CharField(max_length=100)
    participant_1 = models.CharField(max_length=100)
    participant_2 = models.CharField(max_length=100)
    participant_3 = models.CharField(max_length=100)

    def __str__(self):
        return self.leader

class Order(models.Model):
    order_id = models.CharField(max_length=50)
    player = models.ForeignKey(PlayersInfo, related_name='players', on_delete=models.CASCADE)

class PaymentHistory(models.Model):
    players = models.ForeignKey(PlayersInfo, related_name='players', on_delete=models.CASCADE)
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
        return self.players
