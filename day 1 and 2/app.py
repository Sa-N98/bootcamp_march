from flask import Flask, render_template
import os
from model import *



current_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+ \
os.path.join(current_dir,"Database_Bootcamp.sqlite3")

db.init_app(app)
app.app_context().push()



@app.route('/', methods=['GET'])
def home():
    
    data= movies.query.all()
    for i in data:
        print(i.id, i.title, i.rating )



    return render_template('page1.html', data = data)







if __name__ == "__main__":
    db.create_all()
    app.debug = True
    app.run(host='0.0.0.0')