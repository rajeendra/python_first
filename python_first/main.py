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

def outer_function_test():
    
    def inner_function_test():
        print('This is start of the inner function')
        print('This is end of the inner function')
    
    print('This is start of the outer function')
    inner_function_test()
    print('This is end of the outer function')

def greeting(name, age=28, color="red"):
    print(f"Hello {name.capitalize()}, you will be {age+1} next birthday!")
    print(f"We hear you like the color {color.lower()}!")

def arguments_parameter_test():
    greeting(name='John')
    greeting(age=32, name='Peter')
    greeting() #// Exception: missing 1 required positional argument: 'name'

def test():        
    Movie.test_exe()
    print( add(34,67) )
    print( multiply(34,67) )
    print( math.frexp(5) )

def string_test():
    msg='welcome to Python 101: Strings'

    print(len(msg)) #// length

    print(msg+msg) #// concatinate with no space
    print(msg*2)
    print(msg,msg) #// concatinate with a space

    print(msg[2:]) #// lcome to Python 101: Strings
    print(msg[2:4]) #// lc
    print(msg[:4]) #// welc
    print(msg[:-9]) #// welcome to Python 101
    print(msg[2:-2]) #// lcome to Python 101: Strin

    #using curly braces
    name='TERRY'
    color = 'RED'
    msg = '[' + name.capitalize() + '] loves the color ' + color.lower() + '!'
    msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
    print(msg)
    print(msg1)

def input_test():
    name= input('What is your name?: ')
    age=input('What is your age?: ')
    print('Hello '+ name + '! You are '+ age + ' years old.')

def list_test():
    friends = ['John','Michael','Terry','Eric','Graham']
    
    print(len(friends)) #// 5
    print(friends.index('Eric')) #// 3
    print(friends.count('Eric')) #// 1
    
    print(friends[1],friends[4])

    #list - slicing
    print(friends[1:])  #//  ['Michael','Terry','Eric','Graham']
    print(friends[-1:]) #//  ['Graham']
    print(friends[:-1]) #//  ['John','Michael','Terry','Eric']
    print(friends[2:4]) #//  ['Terry','Eric']
    print(friends[:4])  #//  ['John','Michael','Terry','Eric']

    #list- sort
    print('-- list- sort --')
    print(friends)
    friends.sort()
    print(friends)
    friends.sort(reverse=True)
    print(friends)

    #list - reverse
    print(friends)
    friends.reverse()
    print(friends)

    #list - min/max
    cars = [911,130,328,535,740,308]
    print(max(cars))

    #list - add/insert
    print('-- list- add/insert --')
    friends = ['John','Michael','Terry','Eric','Graham']
    friends.append('TerryG')  
    friends.insert(1, 'TerryG')
    friends[2]='TerryG'
    print(friends)

    #list - extend  
    print('-- list- extend --')
    friends.extend(cars)
    print(friends)

    #list - remove
    print('-- list- remove --')
    friends.remove('TerryG')
    friends.pop()   #// last element
    friends.pop(1)  #// first index 
    #friends.clear() #// empty 
    #del friends
    del friends[2]
    print(friends)

    #list - copy
    print('-- list- copy --')
    friends = ['John','Michael','Terry','Eric','Graham']
    friends_copy = friends[:]
    friends_copy = friends.copy()
    friends_copy = list(friends)
    print(friends_copy)

def split_n_join_test():
    msg ='Welcome  to  Python  101: Split  and Join'
    csv = 'Eric,John,Michael,Terry,Graham'
    friends_list = ['Eric','John','Michael','Terry','Graham']

    print(msg.split())
    print(msg)
    print(msg.split(' '), type(msg.split(' ')))
    print('')
    print(csv.split(','))
    print(csv)
    print('')
    print('-'.join(friends_list)) #// Eric-John-Michael-Terry-Graham
    print(friends_list) #// 'Eric,John,Michael,Terry,Graham'
    print(''.join(friends_list)) #// EricJohnMichaelTerryGraham
    print(friends_list) #// 'Eric,John,Michael,Terry,Graham'
    print(''.join(friends_list + friends_list)) #// EricJohnMichaelTerryGrahamEricJohnMichaelTerryGraham
    print('')
    print(''.join(msg.split())) #// 'WelcometoPython101:SplitandJoin'
    print(msg) #// 'Welcome  to  Python  101: Split  and Join'
    print(msg.replace(' ', '')) #// 'WelcometoPython101:SplitandJoin'
  
def tupule_test():
    #a list but you can not changed, imutable list // faster than list
    #// use parentheses
    friends = ['John','Michael','Terry','Eric','Graham']
    friends_tuple = ('John','Michael','Terry','Eric','Graham')
    print(friends[2]) #// Terry
    print(friends_tuple[2]) #// Terry
    print(friends[2:4]) #// ['Terry', 'Eric']
    print(friends_tuple[2:4]) #// ('Terry', 'Eric')

def set_test():
    # remove duplicate, un orderd
    # use curly brackets
    friends = ['John','Michael','Terry','Eric','Graham','Eric']
    friends_tuple = ('John','Michael','Terry','Eric','Graham','Eric')
    friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
    print(friends)
    print(friends_tuple)
    print(friends_set)

    print('')
    #intersection, difference, union
    friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
    my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}

    print(friends_set.intersection(my_friends_set)) #// 'Eric','Graham'
    print(friends_set.difference(my_friends_set)) #// 'John','Michael','Terry'
    print(friends_set.union(my_friends_set)) #// all elements in both no duplicate

    print('')
    print('Eric' in friends)
    print('Eric' in friends and 'John' in friends)

    print(friends_set.union(my_friends_set))
    print(friends_set | my_friends_set)

    print(friends_set.intersection(my_friends_set))
    print(friends_set & my_friends_set)

    print(friends_set.difference(my_friends_set))
    print(friends_set - my_friends_set) 

    # Show only the names who only appear in one of the lists
    print(friends_set.symmetric_difference(my_friends_set))
    print(friends_set ^ my_friends_set) 

    # removing duplicates
    cars =['900','420','V70','911','996','V90','911','911','S','328','900']
    cars_no_dupl =set(cars)
    print(cars_no_dupl)          
      
    #empty Lists
    empty_list = []
    empyt_list = list()

    #empty Tuple
    empty_tuple = ()
    empty_tuple = tuple()

    #empty Set
    empty_set = {} # this is wrong, this is a dictionary
    empty_set = set()

def return_value_test(amount=7):
      tax = amount * 0.25
      total_amount = amount * 1.25
      return amount, tax, total_amount #// return tuple
      return [amount, tax, total_amount] #// return list
      return {amount, tax, total_amount} #// return set
      return f"{amount}, {tax}, {total_amount}"  #// return str

print('-- start --')
print(return_value_test())
print('-- end --')
