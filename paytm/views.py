import random
import string
import json
import requests

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import PlayersInfo, Order, PaymentHistory
from .forms import PlayersInfoForm
from . import Checksum


# def __id_generator__(size=6, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
#     return ''.join(random.choice(chars) for _ in range(size))

def random_string_generator(size=15, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return "".join(random.choice(chars) for _ in range(size))

def unique_order_id_generator(Klass):
    new_order_id = random_string_generator()

    qs_exists = Klass.objects.filter(ORDERID=new_order_id).exists()
    if qs_exists:
        return unique_order_id_generator(Klass)
    return new_order_id

def get_details(request):
    
    if request.method == 'POST':
        form = PlayersInfoForm(request.POST)

        if form.is_valid():
            player_instance = form.save()
            print("payment")
            
            MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
            MERCHANT_ID = settings.PAYTM_MERCHANT_ID
            CALLBACK_URL = settings.HOST_URL + settings.PAYTM_CALLBACK_URL

            order_id = unique_order_id_generator(PaymentHistory)
            Order.objects.create(order_id=order_id, player=player_instance)
            
            cust_id = str(player_instance.pk)
            print("OREDER ID", order_id)
            print("CUST ID", cust_id)

            amount = 120

            data_dict = {
                'MID': MERCHANT_ID,
                'ORDER_ID': order_id,
                'CUST_ID': cust_id,
                'TXN_AMOUNT': str(amount),
                'CHANNEL_ID': 'WEB',
                'WEBSITE': settings.PAYTM_WEBSITE,
                'INDUSTRY_TYPE_ID': 'Retail',
                'CALLBACK_URL': CALLBACK_URL
            }

            param_dict = data_dict
            param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(data_dict, MERCHANT_KEY)
            
            return render(request, "payment.html", {'paytmdict': param_dict})
            
    else:
        form = PlayersInfoForm()

    return render(request, 'details.html', {'form': form})

@csrf_exempt
def response(request):
    if request.method == 'POST':
        MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
        data_dict = {}
        for key in request.POST:
            data_dict[key] = request.POST[key]
        # Verify checksumhash
        verify = Checksum.verify_checksum(data_dict, MERCHANT_KEY, data_dict['CHECKSUMHASH'])
        if verify:
            oid = request.POST.get('ORDERID')
            player = Order.objects.get(order_id=oid).player
            assert isinstance(player, PlayersInfo)
            
            if data_dict['STATUS'] == 'TXN_SUCCESS':
                # Re-verify transaction status from paytm server.

                # initialize a dictionary
                paytmParams = dict()

                paytmParams["MID"] = settings.PAYTM_MERCHANT_ID

                # Enter your order id which needs to be check status for
                paytmParams["ORDERID"] = oid

                # Generate checksum by parameters we have in body
                checksum = Checksum.generate_checksum(paytmParams, MERCHANT_KEY)

                # put generated checksum value here
                paytmParams["CHECKSUMHASH"] = checksum

                # prepare JSON string for request
                post_data = json.dumps(paytmParams)

                # for Staging
                url = "https://securegw-stage.paytm.in/order/status"

                # for Production
                # url = "https://securegw.paytm.in/order/status"

                verify_res = requests.post(url, data=post_data, headers={"Content-type": "application/json"}).json()
                print("VERIFY RES", verify_res)
                if verify_res["RESPCODE"] == "01":
                    player.payment_status = True
                    player.save()
                    PaymentHistory.objects.create(team=player, **verify_res)
                    return render(request, "response.html", {'status': True, 'msg': data_dict['RESPMSG']})
                else:
                    return render(request, "response.html", {'status': False, 'msg': data_dict['RESPMSG']})                
            else:
                # return HttpResponse("Payment unsuccesful.")
                PaymentHistory.objects.create(team=player, **data_dict)
                return render(request, "response.html", {'status': False, 'msg': data_dict['RESPMSG']})
        else:
            return HttpResponse("Checksum verification failed")
    return HttpResponse(status=200)
