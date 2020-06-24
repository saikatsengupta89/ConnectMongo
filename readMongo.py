from pymongo import MongoClient
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DB_NAME = 'retail'
connection= MongoClient (MONGODB_HOST, MONGODB_PORT)
coll_list=[coll for coll in connection[DB_NAME].collection_names()]
print(coll_list)
