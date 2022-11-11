from connection import Connectionection


SELECTION_STR = 'What type of query would you like to run? (select the number)\n\
    (1) Select\n\
    (2) Insert\n\
    (3) Update\n\
    (4) Delete\n\n\
    (5) Run Pre-made\n\
    (-1) Quit'


QUERY_PROMT = 'Insert your query to run:'



def main():
    db = Connectionection('mongodb+srv://fouchb:test@cluster0.y3lhg1a.mongodb.net/?retryWrites=true&w=majority', 'test').get_db()

    selection = 'start'

    # get selection
        # check valid
    while selection not in '1,2,3,4,5,-1'.split(','):
        selection = input(SELECTION_STR)
    

    if selection in '1,2,3,4'.splt(','):


   

        
    # get query
        # check valid



    # perform query based on selection




    # run premade queries
        # 3. List the number of videos for each video category.
        # 4. List the number of videos for each video category where the inventory is non-zero.
        # 5. For each actor, list the video categories that actor has appeared in.
        # 6. Which actors have appeared in movies in different video categories?
        # 7. Which actors have not appeared in a comedy?
        # 8. Which actors have appeared in both a comedy and an action adventure movie?
    
    # quit option


if __name__ == '__main__':
    main()