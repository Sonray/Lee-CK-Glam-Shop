import requests
from  decouple import config
from  datetime import datetime
import base64

the_time = datetime.now()
formatted_time = the_time.strftime('%Y%m%d%H%M%S')

data_to_encode = config('Lipa_Na_Mpesa_Shortcode') + config('Lipa_Na_Mpesa_Passkey')+ formatted_time
encoded_string = base64.b64encode(data_to_encode.encode())
decode_password = encoded_string.decode('utf-8')

  
def  Lipa_na_mpesa(self, phone_number, amount):
    access_token = "Access-Token"
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
        "BusinessShortCode": config('Lipa_Na_Mpesa_Shortcode'),
        "Password": decode_password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": config ('Lipa_Na_Mpesa_Shortcode'),
        "PhoneNumber": phone_number,
        "CallBackURL": "https://ip_address:port/callback",
        "AccountReference": config ('paybillNO'),
        "TransactionDesc": "Make payment to LeeGlam"
    }
    
    response = requests.post(api_url, json = request, headers=headers)
    
    mpesa_infomation = response.json()
    MerchantRequestID = mpesa_infomation['MerchantRequestID']
    print (MerchantRequestID)
    
    CheckoutRequestID = mpesa_infomation['CheckoutRequestID']
    print (CheckoutRequestID)
    
    return (MerchantRequestID,CheckoutRequestID)