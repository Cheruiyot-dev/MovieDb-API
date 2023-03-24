# import unittest
# from app import app, db
# from models import Movie

# class TestMovieAPI(unittest.TestCase):
#     def setUp(self):
#         app.config['TESTING'] = True
#         app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#         self.app = app.test_client()
#         db.create_all()

#     def tearDown(self):
#         db.session.remove()
#         db.drop_all()

#     def test_movie_list_resource(self):
#         # Test GET /movies endpoint
#         response = self.app.get('/movies')
#         self.assertEqual(response.status_code, 200)

#         # Test POST /movies endpoint
#         new_movie = {
#             "title": "The Shawshank Redemption",
#             "genre": "Drama",
#             "release_year": 1994
#         }
#         response = self.app.post('/movies', json=new_movie)
#         self.assertEqual(response.status_code, 201)
#         self.assertIn('id', response.json)
#         self.assertEqual(response.json['title'], new_movie['title'])
#         self.assertEqual(response.json['genre'], new_movie['genre'])
#         self.assertEqual(response.json['release_year'], new_movie['release_year'])

#     def test_movie_resource(self):
#         # Add test movie
#         movie = Movie(title="The Godfather", genre="Crime", release_year=1972)
#         db.session.add(movie)
#         db.session.commit()

#         # Test GET /movies/:id endpoint
#         response = self.app.get(f'/movies/{movie.id}')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json['title'], movie.title)
#         self.assertEqual(response.json['genre'], movie.genre)
#         self.assertEqual(response.json['release_year'], movie.release_year)

#         # Test PUT /movies/:id endpoint
#         updated_movie = {
#             "title": "The Godfather: Part II",
#             "genre": "Crime/Drama",
#             "release_year": 1974
#         }
#         response = self.app.put(f'/movies/{movie.id}', json=updated_movie)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json['title'], updated_movie['title'])
#         self.assertEqual(response.json['genre'], updated_movie['genre'])
#         self.assertEqual(response.json['release_year'], updated_movie['release_year'])

#         # Test DELETE /movies/:id endpoint
#         response = self.app.delete(f'/movies/{movie.id}')
#         self.assertEqual(response.status_code, 204)
