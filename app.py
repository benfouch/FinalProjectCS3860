import collections
from datetime import datetime
from http import client
import os
from readline import insert_text
from typing import Collection
import bson

from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()
MONGODB_URI = os.environ['MONGODB_URI']

client = MongoClient(MONGODB_URI)

# for db_info in client.list_database_names():
#     print(db_info)

db = client['sample_mflix']

# collections = db.list_collection_names()
# for c in collections:
#     print(c)

movies = db['movies']

insert_result = movies.insert_one({
    "title": "Parasite",
    "year": 2020,
    "plot": "A poor family, the Kims, con their way into becoming the servants of a rich family, the Parks. "
    "But their easy life gets complicated when their deception is threatened with exposure.",
    "released": datetime(2020, 2, 7, 0, 0, 0),
})

#parasite_id = insert_result.inserted_id
# print('_id of inserted document {parasite_id}'.format(parasite_id=parasite_id))

#print(movies.find_one({'_id': bson.ObjectId(parasite_id)}))

movies = db['movies']

parasite_id = insert_result.inserted_id

update_result = movies.update_one(
    { '_id': parasite_id }, 
    {'$set': 
        {
        "year": 2019
        }
    })

#print(movies.find_one({'_id': bson.ObjectId(parasite_id)}))

movies.delete_many(
   {"title": "Parasite",}
)

title = 'Parasite'
count = len([d for d in movies.find({"title": title})])
print(f'{count} number of results found for movie {title}')