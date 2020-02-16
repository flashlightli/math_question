from pymongo import MongoClient
from .base_func import get_config


class MongoService(object):

    def __init__(self):
        mongo_config = get_config().get('mongo_config')
        self.host = mongo_config.get("host")
        self.port = mongo_config.get("user")
        self.user = mongo_config.get("user")
        self.password = mongo_config.get("password")
        self.db = mongo_config.get("db")

    def connect_weibo(self):
        client = MongoClient(host=self.host, port=self.port)
        return client.weibo
