import requests
import json
from . models import Subscription

def get_access_token():

    data = {'grant_type': 'client-credentials'}