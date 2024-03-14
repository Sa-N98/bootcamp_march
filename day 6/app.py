from flask import Flask, render_template, request, redirect, url_for 
import os
import requests
from model import *
from api import *
from flask_restful import Api

current_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+ \
os.path.join(current_dir,"Database_Bootcamp.sqlite3")

db.init_app(app)
app.app_context().push()


appApi = Api(app)
appApi.add_resource(movieAPI, '/api/movieAPI')





@app.route('/', methods=['GET','POST'])
def user():
    if request.method == 'GET':
        return render_template('user.html' )
    
    if request.method == 'POST':
        if request.form['type'] == 'signup':
           username =request.form['username']
           email = request.form['email']
           password = request.form['password']

           if not users.query.filter(users.Email== email).all():
               newUser = users(Username = username, Email =email ,Password = password)
               db.session.add(newUser)
               db.session.commit()

           return render_template('user.html', massage=' User Exists, Please LogIn or Create a new account.')

        if request.form['type'] == 'login':
            email = request.form['email']
            password = request.form['password']

            user = users.query.filter(users.Email== email).first()

            if user:
                if user.Password == password:
                    return redirect(url_for('home'))
            return render_template('user.html', massage=' User Does Not Exists, Please SignUP')
    




@app.route('/home', methods=['GET'])
def home():
    
    data= movies.query.all()
    # for i in data:
    #     print(i.id, i.title, i.rating,  )
    #     for j in i.genre:
    #         print(j.type)
    #     print('________________')

    return render_template('page1.html', data = data)

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/filter', methods=['GET','POST'])
def booking():
    if request.method == 'POST':
        search_Key = request.form['searchKey']
        filter_tag= request.form['tag']
        
        if filter_tag == 'title':
            data= movies.query.filter(movies.title.like('%'+search_Key+'%')).all()

        elif filter_tag == 'rating':
            data= movies.query.filter(movies.rating.like(search_Key+'%')).all()
        
        elif filter_tag == 'genre':
            search_Key = search_Key.title()
            data= movies.query.filter(movies.genre.any(type=search_Key)).all()

        return render_template('filter.html' , searchResult=data)

@app.route("/api/add", methods=['GET','POST'])
def api():
    if request.method == "POST":
        title = request.form['title']
        rating = request.form['rating']
        poster = request.form['poster']
        genre = request.form['genre']
        
        data = {
                'Title': request.form['title'],
                'Rating': rating,
                'Poster': poster,
                'Genre': genre
                }
        
        response = requests.post('http://192.168.47.141:5000/api/movieAPI', json=data)

        if response.status_code == 200:
            print(response.json())
            return "aip worked "

        # print(title ,rating ,poster, genre)

        return 'data recived'
    return render_template('api.html')






if __name__ == "__main__":
    db.create_all()
    app.debug = True
    app.run(host='0.0.0.0')