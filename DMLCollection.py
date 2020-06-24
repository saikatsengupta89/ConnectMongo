import pymongo
from pymongo import MongoClient

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DB_NAME = 'retail'
connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
# this shows you successfully connected to an active MongoDB instance
print(connection.database_names())

# list down all the collections in the database
collection = connection[DB_NAME].collection_names()
print(collection)

# query a collection with a specific condition
COLLECTION_NAME = 'purchase_orders'
coll = connection[DB_NAME][COLLECTION_NAME]

# query collection: purchases_orders where total < 200
query1 ={"total": {"$lt" : 200}}
coll_with_tot_lt200= coll.find (query1)
# query collection to get all pizza products
query2 = {"product":"pizza"}
coll_pizza = coll.find (query2)
# query collection to get all milk or pizza products
query3 ={ "$or":[{"product": "milk"},{"product":"pizza"}] }
coll_milkOrpizza = coll.find(query3)

# formulate and print the query output
print()
print("All purchases_orders where total < 200", sep="\n")
for ele in coll_with_tot_lt200:
    product = str(ele["product"])
    total   = str(ele["total"])
    customer= str(ele["customer"])
    formatted_line= customer+ " "+product+" "+total
    print(formatted_line)

print()
print("All purchases_orders where product= pizza", sep="\n")
for ele in coll_pizza:
    product = str(ele["product"])
    total   = str(ele["total"])
    customer= str(ele["customer"])
    formatted_line= customer+ " "+product+" "+total
    print(formatted_line)

print()
print("All purchases_orders where product is milk or pizza", sep="\n")
for ele in coll_milkOrpizza:
    product = str(ele["product"])
    total   = str(ele["total"])
    customer= str(ele["customer"])
    formatted_line= customer+ " "+product+" "+total
    print(formatted_line)