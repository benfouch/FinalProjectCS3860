import bson
from dotenv import load_dotenv
from pymongo import MongoClient


class Conn:
    '''
    Gives a basic connection abject for querying and manipulating a given database
    attrs:
        db -> the name of the database
    funtions:
        get_db()
        insert()
        update()
        find()
        delete()
    '''
    def __init__(self, url, database_name) -> None:
        # mongodb+srv://fouchb:test@cluster0.y3lhg1a.mongodb.net/?retryWrites=true&w=majority
        load_dotenv()
        client = MongoClient(url)
        self.db = client[database_name]
    
    def get_db(self):
        '''
        returns the connected database
        '''
        return self.db

    def insert(self, obj):
        '''
        inserts a json obj to the database
        returns: the id of the inserted object
        '''
        return self.db.insert_one(obj).inserted_id

    def update(self, id, update):
        '''
        updates a json obj in the database
        id: the id the object to update
        update: the json object of fields and new values
        returns: the update result
        '''
        return self.db.update_one({'_id': id}, {'$set': update})

    def find(self, id):
        '''
        id: the id of the object you want the information of 
        returns: the information
        '''
        return self.db.find_one({'_id': bson.ObjectId(id)})

    def delete(self, obj):
        '''
        delets an obj from the db
        obj: the key value pair for refrencing the object you want to delete 
        '''
        self.db.delete(obj)
