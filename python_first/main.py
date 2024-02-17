# main module
import sys
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

def comparison_n_boolean_test():
    # == , <=, >=, in, not in
    print('o' in 'John')
    print('o' not in 'John')

    a = [3,7,42]
    b = [3,7,42]
    print(a == b) #// true
    print(a is b) #// false
    print(id(a), id(b)) #// 4339752000 , 4340107264

    #Empty objects or zeros valuate to False 
    print(int(True)) #// 1
    print(int(False)) #// 0
    print(bool('Parrot')) #// true
    print(bool(' ')) #// true
    print(bool('')) #// false
    print(bool(1)) #// True
    print(bool(0)) #// False
    print(bool([1,2])) #// True
    print(bool([])) #// False
    print(42 + True) #// 43
    print(42 + False) #// 42

def conditional_test():
    is_raining = False
    is_cold = True

    if is_raining and is_cold:
        print("Bring Umbrella and jacket")
    elif is_raining and not(is_cold):
        print("Bring Umbrella")
    elif not(is_raining) and is_cold:
        print("Bring Jacket")
    else:
        print("Shirt is fine!")

def while_loop_test():
    # loop controller and loop body
    i = 1
    while i <= 5:
        print("loop statment 1")
        print("loop statment 2")
        i = i + 1
        print("loop statment 3")
        print("loop statment 4")
    print("exited from loop")

def for_loop_test():
    print('')
    for letter in 'Norwegian blue':
        print(letter)
    
    #//range
    print('')
    for furgle in range(8): #// 0 to 7
        print(furgle, end =" ")
    
    print('')
    for furgle in range(2,8): #// 2 to 7
        print(furgle, end =" ")
    
    print('')
    for furgle in range(1,13,3): #// 1,4,7,10
        print(furgle, end =" ")
    
    print('')
    friends = ['John','Terry','Eric','Michael','George']
    for index in range(len(friends)):
       print(friends[index], end =" ") 

    print('')
    #// break, continue
    for friend in friends:
      if friend == 'Eric':
          print('Found ' + friend + '!')
          #break
          continue
      print(friend)          
    
    print('')
    #// nested
    for friend in friends:
      for number in [1,2,3]:
        print(friend, number)
    
    print('')

def enumerated_test(): 
    friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']   
    print('')
    #// starting from default 0
    for num, friend in enumerate(friends):
      print(num, friend) #// 0 Brian, 1 Judith .. 4. Colin
    
    print('')
    #// stating from 5
    for num, friend in enumerate(friends,5): #// 5 Brian, 6 Judith .. 9. Colin
      print(num, friend)

    print('')
    #// stating from 5, returns list of tuples
    x = []
    for num, friend in enumerate(friends,5): #// (5 Brian), (6 Judith) .. (9. Colin)
      #print((num,friend))
      x.append((num,friend))
    print(x, type(x[0]), type(x)) 

    print('')
    #// list of tuples enumerate begin with 51 .. 
    friends = [(151,'Brian'), (152,'Judith'), (153,'Reg'), (154,'Loretta'), (155,'Colin')]
    for friend in enumerate(friends,51):
        print(friend)   

    print('')
    #// list of tuples enumerate first begin with 51 .. 
    #// ..then agin resulted list of tuples enumerate begin with -100
    efriends = [(151,'Brian'), (152,'Judith'), (153,'Reg'), (154,'Loretta'), (155,'Colin')]
    for friend in enumerate(enumerate(efriends,51),-100):
        print(friend)   

    print('')

def sort_test():    
    my_list = [1,5,3,7,2]
    my_dict = {'car':4,'dog':2,'add':3,'bee':1}
    my_tuple = ('d','c','e','a','b')
    my_string = 'python'
    
    #// original list changed
    print(my_list,'original') #// [1, 5, 3, 7, 2] original
    print(my_list.sort())     #// None
    print(my_list,'original') #// [1, 2, 3, 5, 7] original 

    print('')
    #// original list not changed
    print(my_list,'original') #//  [1, 5, 3, 7, 2] original
    print(sorted(my_list))     #// [1, 2, 3, 5, 7]
    print(my_list,'original') #//  [1, 5, 3, 7, 2] original

    #// tuple - sorted returns a list (not tuple)

    print('')
    #// dictionary
    print(my_dict,'original') #// {'car': 4, 'dog': 2, 'add': 3, 'bee': 1} original
    print(sorted(my_dict)) #// ['add', 'bee', 'car', 'dog']
    print(my_dict,'new') #// {'car': 4, 'dog': 2, 'add': 3, 'bee': 1} new

    print('')
    #// dictionary - returns tuples inside list
    print(my_dict,'original')         #// {'car': 4, 'dog': 2, 'add': 3, 'bee': 1} original
    print(sorted(my_dict.items()))    #// [('add', 3), ('bee', 1), ('car', 4), ('dog', 2)]
    print(my_dict,'new')              #// {'car': 4, 'dog': 2, 'add': 3, 'bee': 1} new

    print('')
    print(my_dict,'original')         #// {'car': 4, 'dog': 2, 'add': 3, 'bee': 1} original
    print(sorted(my_dict.values()))   #// [1, 2, 3, 4]
    print(my_dict,'new')              #// {'car': 4, 'dog': 2, 'add': 3, 'bee': 1} new

    print('')
    print(my_dict,'original')                     #// {'car': 4, 'dog': 2, 'add': 3, 'bee': 1} original
    print(sorted(my_dict.values(), reverse=True)) #//[4, 3, 2, 1]
    print(my_dict,'new')                          #// {'car': 4, 'dog': 2, 'add': 3, 'bee': 1} new

    print('')
    my_list = [1,5,3,7,2]
    print(my_list,'original')       #// [1, 5, 3, 7, 2] original
    print(list(reversed(my_list)))  #// [2, 7, 3, 5, 1]
    print(my_list,'new')            #// [1, 5, 3, 7, 2] new

    print('')
    my_list = [1,5,-3,7,-2]
    print(sorted(my_list)) #// [-3, -2, 1, 5, 7]
    print(sorted(my_list, key = abs)) #// 1, -2, -3, 5, 7]

    print('')
    #// nested list
    my_llist=[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]
    print(sorted(my_llist))                             #// [['add', 3, 10], ['bee', 1, 24], ['car', 4, 65], ['dog', 2, 30]]
    print(sorted(my_llist, key = lambda item :item[0])) #// [['add', 3, 10], ['bee', 1, 24], ['car', 4, 65], ['dog', 2, 30]]
    print(sorted(my_llist, key = lambda item :item[1])) #// [['bee', 1, 24], ['dog', 2, 30], ['add', 3, 10], ['car', 4, 65]]
    print(sorted(my_llist, key = lambda item :item[2])) #// [['add', 3, 10], ['bee', 1, 24], ['dog', 2, 30], ['car', 4, 65]]

def dictionaries_test():
    # Dictionaries are inheritly not sorted or orded

    movie = {
      'title' : 'Life of Brian',
      'year' : 1979,
      'cast' : ['John','Eric','Michael','George','Terry']
    }

    print(len(movie)) #// 3

    #// keys
    print( movie.keys()) #// dict_keys(['title','year','cast'])
    print(movie.values()) #// dict_values(['Life of Brian',1979,['John', 'Eric', 'Michael', 'George', 'Terry']])

    for key in movie:
      print(key)

    for key, value in movie.items():
      print(key, value)

    print('')
    print(movie) #// {'title': 'Life of Brian', 'year': 1979, 'cast': ['John', 'Eric', 'Michael', 'George', 'Terry']}
    print(movie['title']) #// 'Life of Brian'
    #print(movie['budget']) #// Error
    print(movie.get('budget')) #// None
    print(movie.get('budget','Not found')) #// 'Not found'

    print('')
    #// update
    movie['title'] = 'The Holy Grail'
    print(movie.get('title')) #// 'The Holy Grail'

    movie['budget'] = 250000
    print(movie.get('budget')) #// 250000

    movie.update({'title' : 'The Holy Grail','year':1975,'cast':['John','Eric','Michael','George','Terry']})
    print(movie)

    #// delete
    #del movie['year']
    #print(movie)

    #// delete (pop)
    year = movie.pop('year')
    print(movie)
    print(year)

    print('')
    #// more..
    python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
    holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
    life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}

    #membership test
    print('Arthur' in holy_grail)
    if 'Arthur' not in python:
        print('He\'s not here!')

    print('')
    people = {}
    people1 = {}
    people2 = {}

    #method 1 update
    people.update(python)

    print(people) #// {'TerryG': 34, 'Graham': 37, 'Terry': 38, 'Michael': 35, 'Eric': 36, 'John': 35}

    people.update(holy_grail)
    people.update(life_of_brian) #// {'TerryG': 34, 'Graham': 37, 'Terry': 38, 'Michael': 35, 'Eric': 36, 'John': 35, 'Zoot': 17, 'Knight of NI': 40, 'Lancelot': 39, 'Galahad': 35, 'Arthur': 40, 'Biccus Diccus': 45, 'Stan/Loretta': 32, 'Reg': 35, 'Brian': 33}
    print(people)

    print('')
    #method 2 comprehension
    for groups in (python,holy_grail) : people1.update(groups)
    print(people1) #// {'TerryG': 34, 'Graham': 37, 'Terry': 38, 'Michael': 35, 'Eric': 36, 'John': 35, 'Zoot': 17, 'Knight of NI': 40, 'Lancelot': 39, 'Galahad': 35, 'Arthur': 40}

    print('')
    #method 3 unpacking 3.5 later
    people2 = {**python,**holy_grail,**life_of_brian}
    print(people2)
    print(people2.items())

    print('')
    #// sort
    print(sorted(people2))
    print( sorted(people2.items()))

    print('')
    #// sum
    print('The sum of the ages: ', sum(people.values()))


print('-- start --')
#print(sys.version)
#list_test()
#split_n_join_test()
dictionaries_test()
print('-- end --')
