
import string
import random
from .models import Order

def generator(instance):
    all_chars = list(string.digits + string.ascii_letters)
    random.shuffle(all_chars)
    
    randomnumber = ''.join(random.sample(all_chars, 20))
    print (randomnumber)

    id_exists = Order.objects.filter(order_id=randomnumber).exists()
    
    if id_exists:
        return generator(instance)
    return randomnumber