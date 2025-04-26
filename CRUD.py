from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.erros import PyMongoError

class AnimalShelter:
    """ CRUD operations for the Animal collection in MongoDB """
    
    def __init_(self, username, password, host"nv-desktop-services.apporto.com", port=31580):
        """
        Initialize the AnimalShelter with MongoDB connection.
        :param username: USername for authentication
        :param password: Password for authentication
        :param host: MongoDB Host 
        :param port: MongoDB Port
        """
        
        try:
            self.client = MongoClient(f"mongodb://{username}:{password}@{port}")
            self.database = self.client['AAC']
            self.collection = self.database['animals']
        except PyMongoError as e:
            print(f"Error connecting to MongoDB: {e}")
            
        def create(self, data):
            """
            Insert document into the animals collection.
            :param data: A dictionary representing the documents to insert.
            :return: True if insert, else False.
            """
            
            try:
                if data:
                    result = self.collection.insert.one(data)
                    return True if result.insert_id else False
                
                else:
                    rasie ValueError("Data parameter is empty. Cannot insert into database.")
            except Exception as e:
                print(f"Error creating document:{e}")
                return False
            
            def read(self, query):
                """
                Query documents from the animal collection.
                :param: A dictionary representing the key value lookup pair.
                :return: A list of documents if successful, else an empty list.
                """
                
                try:
                    cursor = self.collection.find(query)
                    return list(cursor)
                except Exception as e:
                    print(f"Error reading documents: {e}")
                    return []