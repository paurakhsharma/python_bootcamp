from flask import Flask, jsonify, request

app = Flask(__name__)

'''
REST API
Operation  Endpoint      Method
Create     /movies       POST 
Retrive    /movies       GET
Retrive 1  /movies/{id}  GET
Update     /movies/{id}  PUT 
Delete     /movies/{id}  DELETE
'''

movies = [
    {
        "name": "Forest Gump",
        "casts": ['Tom Hanks'],
        "genres": ["Comedy", "Drama"]
    },
    {
        "name": "Hackshaw Ridge",
        "casts": ["Andrew Garfield"],
        "genres": ["War"]
    }
]
 
@app.route('/movies')
def index():
    return jsonify(movies)


@app.route('/movies/<int:index>')
def get_movie(index):
    try:
        return movies[index]
    except IndexError:
        return {"error": "Invalid Movie id"}, 404


@app.route('/movies', methods=["POST"])
def create_movie():
    movie = request.get_json()
    movies.append(movie)
    return {"id": len(movies) - 1 }

@app.route('/movies/<int:index>', methods=["PUT"])
def update_movie(index):
    movie = request.get_json()
    movies[index] = movie
    return {"message": "success"}

@app.route('/movies/<int:index>', methods=["DELETE"])
def delete_movie(index):
    del movies[index]
    return {"message": "success"} 





if __name__ == "__main__":
    app.run()