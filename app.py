from flask import Flask, jsonify, request
from database.db import initialize_db
from database.models import Movie
from mongoengine import NotUniqueError, DoesNotExist

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
   'host': 'mongodb+srv://testuser:testpassword@cluster0.6xtof.mongodb.net/movie-bag?retryWrites=true&w=majority'
}

initialize_db(app)

'''
REST API
Operation  Endpoint      Method
Create     /movies       POST 
Retrive    /movies       GET
Retrive 1  /movies/{id}  GET
Update     /movies/{id}  PUT 
Delete     /movies/{id}  DELETE
'''

 
@app.route('/movies')
def index():
    movies = Movie.objects().to_json()
    return movies


@app.route('/movies/<id>')
def get_movie(id):
    try:
        return Movie.objects.get(id=id).to_json()
    except DoesNotExist:
        return {"error": "Invalid Movie id"}, 404


@app.route('/movies', methods=["POST"])
def create_movie():
    body = request.get_json()
    try:
        movie = Movie(**body).save()
        return {"id": str(movie.id) }
    except NotUniqueError:
        return {"error": "Movie already exists"}, 400

@app.route('/movies/<id>', methods=["PUT"])
def update_movie(id):
    body = request.get_json()
    Movie.objects.get(id=id).update(**body)
    return {"message": "success"}

@app.route('/movies/<id>', methods=["DELETE"])
def delete_movie(id):
    Movie.objects.get(id=id).delete()
    return {"message": "success"} 

if __name__ == "__main__":
    app.run()