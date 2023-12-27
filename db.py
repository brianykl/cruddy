import sqlite3, random, datetime
from models import Movie

def new_id():
    return random.getrandbits(28)

movies = [
    {
        'available': True,
        'title': 'Trolls Band Together',
        'timestamp': None
    },
    {
        'available': True,
        'title': 'Oppenheimer',
        'timestamp': None
    },
    {
        'available': True,
        'title': 'Barbie',
        'timestamp': None
    },
    {
        'available': True,
        'title': 'Klaus',
        'timestamp': None
    },
    {
        'available': True,
        'title': 'Five Nights At Freddies',
        'timestamp': None
    },]

def connect():
    conn = sqlite3.connect('movies.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY, available BOOLEAN, title TEXT, timestamp TEXT)")
    conn.commit()
    conn.close()
    print('done')
    movie_library = []
    for i in movies:
        movie = Movie(new_id(), i['available'], i['title'], i['timestamp'])
        insert(movie)
        movie_library.append(movie.title) 
    return movie_library
    

def insert(movie):
    conn = sqlite3.connect('movies.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO movies VALUES (?, ?, ?, ?)", (
        movie.serialize()['id'],
        movie.serialize()['available'],
        movie.serialize()['title'],
        movie.serialize()['timestamp']
    ))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('movies.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM movies")
    rows = cur.fetchall()
    movies = []
    for i in rows:
        movie = Movie(i[0], i[1] == 1, i[2], i[3])
        movies.append(movie)
        print(movie.id, movie.available, movie.title)
    conn.close()
    return movies

def update(movie):
    conn = sqlite3.connect('movies.db')
    cur = conn.cursor()
    cur.execute("UPDATE movies SET available = ?, title = ? WHERE id = ?", (movie.serialize()['available'], movie.serialize()['title'], movie.serialize()['id']))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect('movies.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM movies WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def delete_all():
    conn = sqlite3.connect('movies.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM movies")
    conn.commit()
    conn.close()

