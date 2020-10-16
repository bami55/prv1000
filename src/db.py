import os
from pymongo import MongoClient


class DBManager():
    """Database管理
    """

    def __init__(self):
        self.client = MongoClient(
            "mongodb+srv://mongo:{password}@cluster0.7zwnv.mongodb.net/{dbname}?retryWrites=true&w=majority".format(dbname=os.environ['DB_USER'], password=os.environ['DB_PASSWORD']))
        self.db = self.client[os.environ['DB_NAME']]
        self.guilds = self.db.get_collection('guilds')
        print(self.db.list_collection_names())

    def add_guild(self, guild):
        document = {
            id: guild.id,
            name: guild.name
        }
        self.guilds.insert_one(document)

    def get_guilds(self, filter=None, sort=None):
        return self.guilds.find(filter=filter, sort=sort)
