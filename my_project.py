"""
Created on Wed Apr  2 21:39:47 2025

@author: alexanderfloo_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal Collection in MongoDB """
    def __init__(self, username='aacuser', password='letmelearn1'):
        # Initialize the MongoClient. This helps to access
        # the MongoDB database and collections. This is 
        # hard coded to use the AAC database, the animals
        # collection, and the aac user.
        #
        # Connection variables
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31717
        DB = 'AAC'
        COL = 'animals'
        
        # Initialize the connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        
        # target the database and collection to work on
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
    # (C)RUD
    # Creates a new document in the collection
    def create(self, data):
        """
        Insert a document into the collection.
        Returns True if insertion was acknowledged, otherwise False.
        """
        try:
            # If the data exists, attempt an insert
            if data:
                result = self.collection.insert_one(data) # data should be dictionary
                
                # Return whether the insertion ran
                return result.acknowledged
                
            # If the data doesn't exist, return false
            else:
                return False
        # Catch any exceptions and return false
        except Exception as e:
            print(f"Create error: {e}")
            return False
    
    # C(R)UD
    # Reads documents from the collection
    def read(self, query):
        """
        Query for documents that match the provided criteria.
        Returns a list of matching documents, or an empty list if none found or on error.
        """
        try:
            # Accept any dictionary including empty ones
            if isinstance(query, dict):
                result = self.collection.find(query)
                
                # Return a list of the result
                return list(result)
            # Return an empty list if there is no query
            else:
                return []
        # Catch any exceptions and return an empty list
        except Exception as e:
            print(f"Read error: {e}")
            return []
            
        # CR(U)D
    # Updates documents in the collection
    def update(self, query, new_values):
        """
        Update documents matching the query with the provided new values.
        Returns the number of documents modified.
        """
        try:
            if query and new_values:
                result = self.collection.update_many(query, {"$set": new_values})
                return result.modified_count
            else:
                return 0
        # Catch any exceptions andd return 0
        except Exception as e:
            print(f"Update error: {e}")
            return 0

    # CRU(D)
    # Deletes documents from the collection
    def delete(self, query):
        """
        Delete documents matching the query.
        Returns the number of documents deleted.
        """
        try:
            if query:
                result = self.collection.delete_many(query)
                return result.deleted_count
            else:
                return 0
        # Catch any exceptions and return 0
        except Exception as e:
            print(f"Delete error: {e}")
            return 0
