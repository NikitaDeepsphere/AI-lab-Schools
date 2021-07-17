"""
Ex 44.

Create a constructor for movie_list
"""

class movie:
  title = ""
  runtime = 0
  rating = 0.0
  year = 0

  def __init__(self, title, runtime, rating, year):
    self.title = title
    self.rating = rating
    self.runtime = runtime
    self.year = year

class movie_theatre:
  movie_list = []

  def __init__(self):
    return

m1 = movie_theatre()