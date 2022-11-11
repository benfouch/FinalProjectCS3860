'''
Jenifer Madigan & Benjamin Fouch
CS 3860
Term Project 
Due: 11-11-2022
'''

import bson
from pymongo import MongoClient


class Connection:
    '''
    Gives a basic connection object for querying and manipulating a given database\n
    attrs:\n
        db -> the name of the database\n
    funtions:\n
        get_db()\n
        insert()\n
        update()\n
        find()\n
        delete()\n
    '''

    def __init__(self, url, database_name) -> None:
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


    def get_num_vids_per_cat(self):
        '''
        List the number of videos for each video category.

        SELECT category, COUNT(recording_id) AS count
        FROM video_recordings
        GROUP BY category;
        '''
        col = self.db["video_info"]
        
        categories = self.db.video_info.distinct("category") # list of category names
        
        for c in categories:
            query = { "category": c }
            doc = col.find(query) # doc of all results

            counter = 0
            for x in doc: # count results
                counter += 1
                
            print("Category ", c, " has ", counter, " videos.")


        counter = 0
        for x in doc:
            counter += 1
        print(counter)
        '''
        self.db.video_info.aggregate([
            # Stage 1: Only find documents that have more than 1 like
            {
                $match: { likes: { $gt: 1 } }
            },
            # Stage 2: Group documents by category and sum each categories likes
            {
                $group: { _id: "$category", totalLikes: { $sum: "$likes" } }
            }
        ])
        '''
        '''
        categories = self.db.col.distinct("category")
        '''
        return counter
    
    def get_nonzero_num_vids_per_cat(self):
        '''
        List the number of videos for each video category where the inventory (stock_count) is non-zero.


        '''
        pass

    def get_actors_vid_cats(self):
        '''
        For each actor, list the video categories that actor has appeared in.


        '''
        pass

    def get_actor_in_dif_movie_cats(self):
        '''
        Which actors have appeared in movies in different video categories?

        
        '''
        pass

    def get_actors_not_in_comedy(self):
        '''
        Which actors have not appeared in a comedy?


        '''
        pass
    
    def get_actor_in_comedy_adventure(self):
        '''
        Which actors have appeared in both a comedy and an action adventure movie?


        '''
        pass

