import requests
import json
from . models import Subscription
import configparser


def get_access_token():

    config = configparser.ConfigParser()
    config.read('config.ini', encoding="utf-8")
    var1 = config.get("secrets", "paypal_secret")
    print(var1)

    data = {'grant_type': 'client-credentials'}
    headers = {'Accesp' : 'application/json', 'Accept-Language': 'en_US'}
    client_id = "AfWI9P33RrvMnsP0OeerAriRlYOYMkGiHcN6z40KW7mDy1VF66OUUx5tNY9jsumECNbXhb74EEz0svAp"
    secret_id = var1

    url = "https://api.sandbox.paypal.com/vi/oauth2/token"
    r = requests.post(url, auth=(client_id, secret_id), headers=headers, data=data).json()

    access_token = r["access_token"]

    return access_token

def cancel_subscription_paypal(access_token, subID):
    
    bearer_token = "Bearer " + access_token
    headers = {
        'Content-Type': 'application/json',
        'Authorization': bearer_token,
    }

    url = "https://api.sandbox.paypal.com/vi/billing/subscriptions/" + subID + "/cancel"
    r = requests.post(url, headers=headers)

    print(r.status_code)