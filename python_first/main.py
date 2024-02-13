# main module

import math    
# math module ref can find here
# https://docs.python.org/3/py-modindex.html

from calc import add, multiply

class Movie:
    def __init__(self,title,year,imdb_score,have_seen):
        self.title = title
        self.year = year
        self.imdb_score = imdb_score
        self.have_seen = have_seen
    
    def nice_print(self):
        print("Title: ", self.title)
        print("Year of production: ", self.year)
        print("IMDB Score: ", self.imdb_score)
        print("I have seen it: ", self.have_seen)

    def test_exe():
        film_1 = Movie("Life of Brian",1979,8.1,True)
        film_2 = Movie("The Holy Grail",1975,8.2,True)

        #print(film_1.title, film_1.imdb_score)
        film_2.nice_print()
        Movie.nice_print(film_2)
        films = [film_1,film_2]

        films = [film_1,film_2]
        print(films[1].title,films[0].title)
        films[0].nice_print()
        
        
print('-- start --')
Movie.test_exe()
print( add(34,67) )
print( multiply(34,67) )
print( math.frexp(5) )
print('-- end --')
