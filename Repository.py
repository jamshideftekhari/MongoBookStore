from ast import Pass
import pymongo

# myAtlasClient = "mongodb+srv://jamshid:<password>@jamshidcluster.mdng7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

class Repository(object):
    def __init__(self, hostname):
        self.MoClient = pymongo.MongoClient(hostname)
        print("List of databases: ")
        print(self.MoClient.list_database_names())
    
    def Connet2DataBase(self, DBName):
        self.MoDatabase = self.MoClient[DBName]
        print("List of collections: ")
        print(self.MoDatabase.list_collection_names())

    def ListAllDocuments(self, collection):
        self.MoCollection = self.MoDatabase[collection]
        print("All Documents: ")
        for doc in self.MoCollection.find():
            print(doc)
    
    def FindDocumentByName(self, name):
        Pass

Repo = Repository("mongodb://localhost:27017")

print("*****Bookstore content***********")
Repo.Connet2DataBase("bookshop")
Repo.ListAllDocuments("book")

print("*****Recipes content***********")
Repo.Connet2DataBase("cookbook")
Repo.ListAllDocuments("Recipes")

