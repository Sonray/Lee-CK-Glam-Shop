from rest_framework import serializers
from Items.models import Product_details
from .models import Order, Ordered_Items, Customer_Pickup_point, Pickup_stations


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product_details
        exclude = ('admin_id',)
        depth = 1

class OrderedItemSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Ordered_Items
        fields = '__all__'

    
class CustomerPickupSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Customer_Pickup_point
        fields = '__all__'

    
class PickupStationSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Pickup_stations
        fields = '__all__'

    
class TheOrderSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Order
        fields = '__all__'
    
        
class OrderSerializer(serializers.ModelSerializer):
    
    orderitems      = OrderedItemSerializer(many=True)
    customerpick    = CustomerPickupSerializer(many=True)
    
    class Meta:
        model = Order
        fields = [
            'user_id',
            'payment_id',
            'amount_paid',
            'Payment_method',
            'delivery_method',
            'orderitems',
            'customerpick',
            ]
    
    