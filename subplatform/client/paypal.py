import requests
import json
from . models import Subscription

def get_access_token():

    data = {'grant_type': 'client-credentials'}
    headers = {'Accesp' : 'application/json', 'Accept-Language': 'en_US'}
    client_id = "AfWI9P33RrvMnsP0OeerAriRlYOYMkGiHcN6z40KW7mDy1VF66OUUx5tNY9jsumECNbXhb74EEz0svAp"