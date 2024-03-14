from flask_restful import Resource, reqparse
from model import *


#CRUD
class demoAPI(Resource):

    def post(self):    # Adding or sending data to the back end or data base     C
        return
    
    def get(self):     # Retrice or get data from the data base or function      R
        return
    
    def put(self):     #  Edit data base                                         U
        return 
    
    def delete(self):  # Deletes                                                 D
        return 












movie_args= reqparse.RequestParser()
movie_args.add_argument("Title" ,type=str)
movie_args.add_argument("Rating", type=float)
movie_args.add_argument("Poster", type=str)
movie_args.add_argument("Genre", type=str)

class movieAPI(Resource):
    def post(self): 
        var = movie_args.parse_args()   # Adding or sending data to the back end or data base     C
        print('comming from api => ',var["Title"])
        print('comming from api => ',var['Rating'])
        print('comming from api => ',var['Poster'])
        print('comming from api => ',var['Genre'])
        

        if not movies.query.filter(movies.title == var["Title"]).first():
            newMovie = movies(title = var["Title"],
                              rating = var['Rating'],
                              poster = var['Poster'])
            db.session.add(newMovie)
            db.session.commit()

            current_movie = movies.query.filter(movies.title == var["Title"]).first()
            genre_id = genre.query.filter(genre.type == var['Genre']).first()
            
            new_realtion = movie_g(m_id = current_movie.id,
                                g_id = genre_id.id)
            
            db.session.add(new_realtion)
            db.session.commit()
        
      
        return 'api was hit', 200
    
    def get(self):     # Retrice or get data from the data base or function      R
        return
    
    def put(self):     #  Edit data base                                         U
        return 
    
    def delete(self):  # Deletes                                                 D
        return 


