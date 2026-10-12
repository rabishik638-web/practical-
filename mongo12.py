import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create database and collection
db = client["Emp"]
col = db["emp1"]

# Insert one document
doc = {"name": "raman", "age": 20, "dept": "IT"}
col.insert_one(doc)

print("Read a Single Document after inserted")
print("--------------------------------------")
print(col.find_one())

# Insert many documents
docs = [
    {"name": "Raja", "age": 21, "dept": "IT"},
    {"name": "Bala", "age": 22, "course": "IT", "gender": "Male"},
    {"name": "Saran", "age": 19, "address": "New St, VPM"},
    {"name": "raman", "designation": "Manager", "dept": "Mech"}
]

col.insert_many(docs)

print()
print("Read all Documents after inserted")
print("----------------------------------")

for x in col.find():
    print(x)

# Delete one document
col.delete_one({"name": "raman"})

print()
print("Document deleted...")
print("Read Documents after deleting a document")
print("------------------------------------------")

for x in col.find():
    print(x)

# Delete many documents
col.delete_many({"name": "raman"})

print()
print("Documents deleted successfully")
print("Read Documents after deleting many documents")
print("---------------------------------------------")

for x in col.find():
    print(x)

# Drop collection
col.drop()
print("Collection is deleted...")