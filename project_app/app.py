'''
Jenifer Madigan & Benjamin Fouch
CS 3860
Term Project 
Due: 11-11-2022
'''


from connection import Connection
from dotenv import load_dotenv
import os

load_dotenv()
MONGODB_URI = os.environ['MONGO_STR']

with open('promt_str.txt') as file:
    SELECTION_STR = file.read()

def main():
    mongo = Connection(MONGODB_URI, 'test')

    selection = 'start'
    while selection not in '-1,3,4,5,6,7,8,9'.split(','):
        selection = input(SELECTION_STR)
        match selection:
            case '-1':
                print('all')
            case '3':
                mongo.get_num_vids_per_cat()
                print('query 3')
            case '4':
                mongo.get_nonzero_num_vids_per_cat()
                print('query 4')
            case '5':
                mongo.get_actors_vid_cats()
                print('query 5')
            case '6':
                mongo.get_actor_in_dif_movie_cats()
                print('query 6')
            case '7':
                mongo.get_actors_not_in_comedy()
                print('query 7')
            case '8':
                mongo.get_actor_in_comedy_adventure()
                print('query 8')
            case '9':
                quit('Bye!')
    

if __name__ == '__main__':
    main()
    quit('Bye!')
