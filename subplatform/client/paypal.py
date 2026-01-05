import requests
import json
from . models import Subscription
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

def get_access_token():

    data = {'grant_type': 'client-credentials'}
    headers = {'Accesp' : 'application/json', 'Accept-Language': 'en_US'}
    client_id = "AfWI9P33RrvMnsP0OeerAriRlYOYMkGiHcN6z40KW7mDy1VF66OUUx5tNY9jsumECNbXhb74EEz0svAp"
    secret_id = config["secrets"]["paypal_secret"]

    url = "https://api.sandbox.paypal.com/vi/oauth2/token"
    r = requests.post(url, auth=(client_id, secret_id), headers=headers, data=data).json()

    access_token = r["access_token"]

    return access_token