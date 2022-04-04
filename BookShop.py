import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["bookshop"]
print(myclient.list_database_names())
mycol = mydb["book"]
for b in mycol.find():
    print(b)
    print(b["title"])