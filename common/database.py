import pymongo

# client = pymongo.MongoClient(["mongodb://j84077200345:jack6114@ds139920.mlab.com:39920/movies"])
# DATABASE = client['movies']

class Database(object):
    URI = ["mongodb://j84077200345:jack6114@ds139920.mlab.com:39920/movies"]
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['movies']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def remove(collection, query):
        Database.DATABASE[collection].remove(query)
