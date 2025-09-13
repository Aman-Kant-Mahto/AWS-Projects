import json
import pymongo
import os

def lambda_handler(event, context):
    # MongoDB connection string from environment variables
    mongo_uri = os.getenv('MONGO_URI')

    # Connect to MongoDB
    client = pymongo.MongoClient(mongo_uri)

    # Select database and collection
    db = client['your_database_name']  # Replace with your database name
    collection = db['your_collection_name']  # Replace with your collection name

    # Example: Insert a document
    document = {
        "name": "Sample Document from Lambda",
        "type": "Demo"
    }
    result = collection.insert_one(document)

    # Example: Query the inserted document
    inserted_document = collection.find_one({"_id": result.inserted_id})

    return {
        'statusCode': 200,
        'body': json.dumps(f'Document inserted: {inserted_document}')
    }
