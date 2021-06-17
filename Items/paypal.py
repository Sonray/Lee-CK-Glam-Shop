import  sys
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment

class PayPalClient:
    def __init__(self):
        self.client_id = 'ATBe1DBUfD4hi2pNAIo4fq16dp20ZANS8VbRI57wcH_MT0Cew1yH5dzFCWIH_jmJmAL2ix-beZFJe7Cw'
        self.client_secret = 'EJsD1QSulOa7JI09_tO4JGCxaHZdRbpDa4r9NW_cD-_JWFCaXfZfP7OggAFv4Jt5j1zT8ILiEu8Rg8OZ'
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)