import configparser

config = configparser.ConfigParser()
config.read('config.ini', encoding="utf-8")

var1 = config.get("secrets", "paypal_key")