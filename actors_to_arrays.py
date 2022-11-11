from pymongo import MongoClient

client = MongoClient('mongodb+srv://fouchb:test@cluster0.y3lhg1a.mongodb.net/?retryWrites=true&w=majority')
result = client['test']['actors'].aggregate([
    {
        '$group': {
            '_id': '$recording_id', 
            'actors': {
                '$addToSet': '$name'
            }
        }
    }
])

# client['test']['actors_array'].insert_many(result)

i = 0
for r in result:
    response = client['test']['actors_array'].insert_one(r).inserted_id
    print(i := i + 1, response, r)

i = 0
for c in client['test']['actors_array'].find():
    print(i := i + 1, c)

