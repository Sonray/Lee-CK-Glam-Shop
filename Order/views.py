from rest_framework.response import Response
from rest_framework.views import APIView
from  Items.models import  Product_details
from .models import Order, Ordered_Items, Customer_Pickup_point, Pickup_stations
from Authentication.models import  Account
from .serializers import OrderSerializer
from rest_framework.decorators import permission_classes
from rest_framework import permissions, status
from Items.mpesa_payments import Lipa_na_mpesa
import json
from paypalcheckoutsdk.orders import OrdersGetRequest
from Items.paypal import PayPalClient
# Create your views here.

@permission_classes((permissions.AllowAny,)) 
class  Order_Product_MPESA(APIView):
    
    serializer_class = OrderSerializer

    def post(self, request, format=None):
        
        review = request.data
        data = request.data
        serializers = self.serializer_class(data=review)

        if serializers.is_valid(raise_exception=True):
            
            phone_number = str( review['order_phone_number'])
            amount_1 = str(review['price'])
            
            mpesa_dict = Lipa_na_mpesa( phone_number, amount_1)
            
            print(mpesa_dict)
            
            ResultCode      = mpesa_dict['ResponseCode']
            payment_id      = mpesa_dict['MerchantRequestID']
            Ordered_Item    = data['orderitems']
            pickup_point    = data['customerpick']
            
            if ResultCode != 0:
                
                order = Order.objects.create(user_id=Account.objects.get(id=data['user_id']), payment_id = payment_id, amount_paid=amount_1,
                                    Payment_method='M-Pesa',delivery_method=data['delivery_method'] )
                
                order_ids = order.pk
                
                for item in Ordered_Item:
                    
                    Ordered_Items.objects.create(order_id = Order.objects.get(id=order_ids), product = Product_details.objects.get(id=item['product']), quantity = item['quantity'], price = item['price'])
                
                for pickup in pickup_point:
                    
                    Customer_Pickup_point.objects.create(order_id = Order.objects.get(id=order_ids), user_id=Account.objects.get(id=data['user_id']),Station_id = Pickup_stations.objects.get(id=pickup['Station_id']),
                                                        first_name=pickup['user_id'], last_name=pickup['last_name'], phone_number=pickup['phone_number'],
                                                        Delivery_address=pickup['Delivery_address'], County=pickup['County'], City=pickup['City'] )
                
            else:
                
                order = Order.objects.create(user_id=Account.objects.get(id=data['user_id']), payment_id = payment_id, amount_paid=amount_1,
                                    Payment_method='M-Pesa',delivery_method=data['delivery_method'], payment_status = True )
                
                order_ids = order.pk
                
                for item in Ordered_Item:
                    
                    Ordered_Items.objects.create(order_id = Order.objects.get(id=order_ids), product = Product_details.objects.get(id=item['product']), quantity = item['quantity'], price = item['price'])
                
                for pickup in pickup_point:
                    
                    Customer_Pickup_point.objects.create(order_id = Order.objects.get(id=order_ids), user_id=Account.objects.get(id=data['user_id']),Station_id = Pickup_stations.objects.get(id=pickup['Station_id']),
                                                        first_name=pickup['first_name'], last_name=pickup['last_name'], phone_number=pickup['phone_number'],
                                                        Delivery_address=pickup['Delivery_address'], County=pickup['County'], City=pickup['City'] )
                 
                
            return Response(
                serializers.data, status=status.HTTP_201_CREATED
                )
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@permission_classes((permissions.AllowAny,)) 
class  Order_Product_Paypal(APIView):
    
    serializer_class = OrderSerializer

    def post(self, request, format=None):
                
        data = request.data
        serializers = self.serializer_class(data=data)
        
        PPClient = PayPalClient()
        
        body = json.loads(request.body)
        paypaldata = body["orderID"]
        
        requestorder = OrdersGetRequest(paypaldata)
        response_data = PPClient.client.execute(requestorder)
        
        total_paid = response_data.result.purchase_units[0].amount.value
        Ordered_Item    = data['Ordered_Items']
        pickup_point    = data['Customer_Pickup_point']
        
        
        if serializers.is_valid(raise_exception=True):
                        
            order = Order.objects.create(user_id=Account.objects.get(id=data['user_id']), payment_id = response_data.result.id, amount_paid=total_paid,
                                Payment_method='Paypal',delivery_method=data['delivery_method'], payment_status = True )
            
            order_ids = order.pk
            
            for item in Ordered_Item:
                
                Ordered_Items.objects.create(order_id = Order.objects.get(id=order_ids), product = Product_details.objects.get(id=item['product']), quantity = item['quantity'], price = item['price'])
            
            for pickup in pickup_point:
                
                Customer_Pickup_point.objects.create(order_id = Order.objects.get(id=order_ids), user_id=Account.objects.get(id=data['user_id']),Station_id = Pickup_stations.objects.get(id=pickup['Station_id']),
                                                    first_name=pickup['first_name'], last_name=pickup['last_name'], phone_number=pickup['phone_number'],
                                                    Delivery_address=pickup['Delivery_address'], County=pickup['County'], City=pickup['City'] )
                
            return Response(
                serializers.data, status=status.HTTP_201_CREATED
                )
    
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    