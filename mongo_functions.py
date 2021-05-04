import pymongo

def create_subway_mongodb():
    client = pymongo.MongoClient('localhost', 27017)

    if 'SubwayChallenge' not in client.list_database_names():
        subwayDB = client.SubwayChallenge
        return subwayDB
    else:
        return client.SubwayChallenge



def insert_into_mongo(document_dict, collection, clear_db=False):
    if clear_db == True:
        collection.delete_many({})

    collection.insert_one(document_dict)

    return print(f"Inserted Document for Path {document_dict['path']} and its Statistics into {collection}")

