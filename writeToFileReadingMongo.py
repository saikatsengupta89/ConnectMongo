from pymongo import MongoClient
writeFile = open ("C:/PycharmProjects/ConnectMongo/posts.txt", 'w')

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DB_NAME = 'temp'
COLLECTION_NAME = 'posts'

connection= MongoClient (MONGODB_HOST, MONGODB_PORT)
collection= connection[DB_NAME][COLLECTION_NAME]

posts = collection.find()
print(posts.count())
for p in posts:
    studentID= str(int(p['studentID']))
    name= str(p['name'])
    line= studentID + "," + name
    writeFile.write(line+"\n")
writeFile.close()