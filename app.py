from flask import Flask, render_template, request, redirect
import os, db, datetime
from models import Movie

app = Flask(__name__)
movie_library = []

if not os.path.isfile('movies.db'):
    movie_library = db.connect()
    movie_library = db.view()


@app.route('/')
def index():
    movie_library = db.view()
    return render_template('index.html', movies = movie_library)
    # return render_template('index.html')
    

@app.route('/create', methods = ['POST'])
def create():
    title = request.form['title']
    print('got past here!')
    if title:
        movie = Movie(db.new_id(), True, title, datetime.datetime.now())
        db.insert(movie)
        movie_library = db.view()
        return redirect('/')
    movie_library = db.view()
    return "title not provided :c"

@app.route('/update', methods = ['POST'])
def update():
    old_title = request.form['old_title']
    new_title = request.form['new_title']
    movies = db.view()
    for m in movies:
        if m.serialize()['title'] == old_title:
            movie = Movie(m.serialize()['id'], m.serialize()['available'], new_title, m.serialize()['timestamp'])
            print('new movie: ', movie.serialize())
            db.update(movie)
            movie_library = db.view()
            return redirect('/')
    movie_library = db.view()
    return redirect('/')

@app.route('/delete', methods = ['POST'])
def delete():
    title = request.form['title']
    movies = db.view()

    
    for m in movies:
        if m.serialize()['title'] == title:
            db.delete(int(m.serialize()['id']))
    movie_library = db.view()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)