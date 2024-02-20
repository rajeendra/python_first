# main module
from numbers import Number
from pathlib import Path
import sys
import math
import platform, string, os 
from platform import python_version, system 
import platform as pl  
import random
import timeit

# math module ref can find here
# https://docs.python.org/3/py-modindex.html

from calc import add, multiply

class Movie:
    def __init__(self,title,year,imdb_score,have_seen):
        self.title = title
        self.year = year
        self.imdb_score = imdb_score
        self.have_seen = have_seen
    
    def class_method_print(self):
        print("Title: ", self.title)
        print("Year of production: ", self.year)
        print("IMDB Score: ", self.imdb_score)
        print("I have seen it: ", self.have_seen)

    def class_method_obj():
        film_1 = Movie("Life of Brian",1979,8.1,True)
        film_2 = Movie("The Holy Grail",1975,8.2,True)

        #print(film_1.title, film_1.imdb_score)
        film_2.class_method_print()
        Movie.class_method_print(film_2)
        films = [film_1,film_2]

        films = [film_1,film_2]
        print(films[1].title,films[0].title)
        films[0].class_method_print()

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

def classes_and_objects_test():        
    Movie.class_method_obj()

def import_modules_test():
    print( add(34,67) )
    print( multiply(34,67) )
    print( math.frexp(5) )

    print(dir(platform))
    print(platform.python_version())
    
    print(dir(pl))
    print(pl.python_version())
    
    print(python_version())
    
    print(system())    

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

def files_test():
    path1 = Path(__file__).parent / "./data/greeting.txt"
    path2 = Path(__file__).parent / "../data/friends.csv"

    my_file = open(path2,'r') # w, a
    #print(my_file.read())
    
    # File read always start from the where the pointer it currently have

    print(my_file.read(14)) #// read ten characters
    print(my_file.readline()) #// read first line
    print(my_file.readline()) #// read second line

    my_file.close()

    with open(path2,'r') as f:
        print(f.read()) #// John, 1939 Eric, 1943 Michael, 1943 Graham, 1941 TerryG, 1940 TerryJ, 1942

    print('')
    with open(path2,'r') as f:
        friends = f.read().splitlines()
        print(friends) #// ['John, 1939', 'Eric, 1943', 'Michael, 1943', 'Graham, 1941', 'TerryG, 1940', 'TerryJ, 1942']
        for friend in friends:
            friend = friend.split(',')
            name = friend[0]
            year = int(friend[1].strip())
            print(f'In 2030 {name} will be {2030 -year} years old')

    print('')
    with open(path2,'r') as f:
        #for line in f: #not in scrimba
        for line in f.readlines(): #Scrimba workaround
            print(line)

    print('')
    with open(path2,'r') as f:
        line_by_line = f.readlines()
    with open(path2,'r') as f:
        line_by_line1 = f.read().splitlines()
    print('readlines: ',line_by_line) #// readlines: ['Hello,', 'Welcome to Monty Pythons Flying Circus!']
    print('splitlines: ',line_by_line1) #// splitlines: ['Hello,', 'Welcome to Monty Pythons Flying Circus!']

def handle_exception_test():
    #// basic structue
    try:
        num=int(input('Enter a number: '))
        print("30 divided by",num, "is: ", 30/num)
    except:
        print("Invalid Input!")
    
    print("**Thank you for playing!**")

    #// Exception run from top to bottom
    try:
        num=int(input('Enter a number: '))
        print("30 divided by",num, "is: ", 30/num)
    except ZeroDivisionError as err:
        print(err, "You can't divide by Zero!!!")
    except ValueError as err:
        print(err, "Bad Value!")
    except:
        print("Invalid Input!")
    
    print("**Thank you for playing!**")

    #// raise customize error
    try:
        num=int(input('Enter a number between 1 and 30: '))
        num1 = 30/num
        if num1 != None:
            if num > 30:
                raise ValueError(num)
    except ZeroDivisionError as err:
        print(err, "You can't divide by Zero!!!")
    except ValueError as err:
        print(err,"Bad Value not between 1 and 30!")
    except:
        print("Invalid Input!")
    else:
        print("30 divided by",num, "is: ", 30/num)
    finally:
        print("**Thank you for playing!**")

def inheritance_test():
    class Person:
        def move(self):
            print("Moves 4 paces")
        def rest(self):
            print("Gains 4 health points")

    class Doctor(Person):
        def heal(self):
            print("Heals 10 health points")

    doc1 = Doctor()
    doc1.move()
    doc1.heal()

    #// Overide Person's move() method
    class Fighter(Person):
        def fight(self):
            print("Do 10 health points of damage")
        def move(self):
            print("Moves 6 paces")

    fighter1 = Fighter()
    fighter1.move()
    fighter1.fight()

    #// multiple inheritance
    class Wizard(Doctor,Fighter):
        def cast_spell(self):
            print("Turns invisble")
        def heal(self):
            print("Heals 15 health points")
        
    character1=Wizard()
    character1.move() #// Moves 6 paces
    character1.heal()

    print(platform.python_version()) #// python version

def zip_unzip_test():
    nums = '1234' 
    letters = ['a','b','c','d']
    names =['John','Eric','Michael','Graham','Joe']

    #// Mapping items of two collections by index and transform as a new items of colloection 
    combo = list(zip(nums,letters))
    print(combo) #// [('1', 'a'), ('2', 'b'), ('3', 'c'), ('4', 'd')]

    combo = dict(zip(nums,letters))
    print(combo) #// {'1': 'a', '2': 'b', '3': 'c', '4': 'd'}

    combo = list(zip(nums,letters,names))
    print(combo) #// [('1', 'a', 'John'), ('2', 'b', 'Eric'), ('3', 'c', 'Michael'), ('4', 'd', 'Graham')] 

    #// unzip - seperate back
    num,let,nam =zip(*combo)
    print(num,let,nam) #// ('1', '2', '3', '4') ('a', 'b', 'c', 'd') ('John', 'Eric', 'Michael', 'Graham')

    keys = 'this parrot is deceased'
    values = 'denna papegojan är avliden'
    keys = keys.split()
    values = values.split()
    print(keys,values) #// ['this', 'parrot', 'is', 'deceased'] ['denna', 'papegojan', 'är', 'avliden']

    en_sv_dict = dict(zip(keys,values))
    print(en_sv_dict) #//{'this': 'denna', 'parrot': 'papegojan', 'is': 'är', 'deceased': 'avliden'}
    new_dict = {key:value for key,value in zip(keys,values)}
    print(new_dict) #// {'this': 'denna', 'parrot': 'papegojan', 'is': 'är', 'deceased': 'avliden'}

    en,sv = list(en_sv_dict.keys()),list(en_sv_dict.values())
    print(en,sv) #// ['this', 'parrot', 'is', 'deceased'] ['denna', 'papegojan', 'är', 'avliden']

def lambda_function_test():
    # Lambda function allways return a value, not like a regular function is optional

    #// regular function
    def square(x):
        return x*x
    
    #// lambda function
    #name = lambda parameter(s): expression
    square_lam = lambda x: x*x
    print(square_lam(3))

    #// single line function
    def square2(x):return x*x
    print(square2(3))

    #//
    def name_and_alias(name,alias):
        return name.strip().title() + ':' + alias.strip().title()
    
    name_and_alias_lam = lambda name, alias : name.strip().title() + ':' + alias.strip().title()

    print(name_and_alias(' john  ClEEse  ','HECKLER'))
    print(name_and_alias_lam(' john  ClEEse  ','HECKLER')) 

    #// sort by use of a lambda function
    monty_python = ['John Marwood Cleese','Eric Idle','Michael Edward Palin','Terrence Vance Gilliam','Terry Graham Perry Jones', 'Graham Arthur Chapman']

    #key_lam = lambda name:name.split()
    #print(key_lam(monty_python[0]))
    #print(key_lam(monty_python[0])[-1])

    #monty_python.sort(key = lambda name:name.split(' ')[0]) #// sort from first name
    monty_python.sort(key = lambda name:name.split(' ')[1]) #// sort from middle name
    #monty_python.sort(key = lambda name:name.split(' ')[-1]) #// sort from last name
    print(monty_python)
    
    #// sort by use of a function
    def sort_names(name):
        return name.split(' ')
    monty_python.sort(key= sort_names)
    print(monty_python)

    #// return type <class 'function'> - lambda a: a*n
    def func(n):
      return n
    print(type(func(3))) #// <class 'int'> - 3

    def func(n):
      return lambda a: a*n
    print(type(func(3))) #// <class 'function'> - lambda a: a*3
    
    doubler = func(2) #// This return lambda function 'lambda a: a*2'
    print(doubler(3)) #// This return 6
    quintipler = func(5) #// This return lambda function 'lambda a: a*2'
    print(quintipler(3)) #// This return 15

    #//
    def price_calc(start,hourly_rate):
        return lambda hours: start + hourly_rate * hours
        
    walkin_cost = price_calc(10,30)
    premium_cost = price_calc(1,25)
    print(walkin_cost(2)) #// 70
    print(premium_cost(2)) #// 51

    #// call lambda function at the same time declaration
    print((lambda a,b,c: a+b+c)(2,3,4)) #// 9
    print(price_calc(1,25)(2)) #//51

    #// use default values (c=2) for lambda paraeters
    #// Note: place defaulted in the last
    print((lambda a,b,c=2: a+b+c)(2,3))

    #// name your arguments
    print((lambda a,b,c=2: a+b+c)(2,c=3,b=4))

    #//unpacking arguments
    print((lambda *args: sum(args))(2,3,4,50))

    #// divide this by integer
    signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
    print(sorted(signups)) # Lexicographic sort
    #write sorting by integer
    print(sorted(signups,key = lambda a:int(a[3:]))) # Integer sort

    #// sort object
    class Player:
      def __init__(self, name, score):
          self.name = name
          self.score =  score

    Eric = Player('Eric', 116700)
    John = Player('John', 24327)
    Terry = Player('Terry', 150000)
    player_list = [Eric, John, Terry]

    #Exercise: Sort this by score using lambda!
    player_list.sort(key = lambda playyer: playyer.score, reverse=True)
    print([ {player.name,  player.score} for player in player_list])

def comprehensions_test():
    #// Comprehensions lists
    
    numbers = [1,2,3,4,5,6,7,8,9]
    # give me a list with num squared for each num in numbers
    new_list = []
    for num in numbers:
        new_list.append(num*num)
    print(new_list)

    #// Do above in short way
    new_list = [num*num for num in numbers]
    print(new_list)

    #// use if condition to select items from the list
    # give me a list with num for each num in numbers if num is even 
    new_list = [num for num in numbers if num % 2 == 0]
    print(new_list)

    #// use filter
    new_list = filter(lambda num: num % 2 ==0, numbers)
    print(list(new_list))

    #// nested loop
    # I want a (letter, num) pair for each letter in 'spam' and each number in '0123'
    new_list = []
    for letter in 'spam':
      for num in range(3):
          new_list.append((letter,num))
    print(new_list)

    new_list = [(letter,num) for letter in'spam' for num in range(3)]
    print(new_list)

    #// Comprehensions - dictionary
    movies = ["And Now for Something Completely Different","Monty Python and the Holy Grail",
    "Monty Python's Life of Brian","Monty Python Live at the Hollywood Bowl","Monty Python's The Meaning of Life","Monty Python Live (Mostly)"]
    year =[1971,1975,1979,1982,1983,2014]
    names = ['John','Eric','Michael','Graham','Terry','TerryG']

    print(list(zip(movies, year))) #// [ ('movie n', 19nn), (), ()  ]

    # give me a dict('movies': year) for each movies, year in zip(movies, year)
    new_dict = dict()
    for movie, yr in zip(movies,year):
        new_dict[movie] = yr
    print(new_dict) #// { 'movie n':19nn, '':'', '',''  }

    new_dict = {movie:yr for movie,yr in zip(movies,year)}
    print(new_dict) #// exactly same result as above

    #// movies yr < 1983
    new_dict = {movie:yr for movie,yr in zip(movies,year) if yr < 1983}
    print(new_dict)  

def randomness_test():
    for i in range(5):
        print(random.random())
        #// between 1 and 6
        print(random.uniform(1,6))
        print(random.randint(1,6))
        print(random.randrange(1,100,2)) #// 1, 3, 5 .. 99
        print('')

    friends_list =  ['John', 'Eric', 'Michael', 'Terry', 'Graham']
    print(random.choice(friends_list))
    print(random.sample(friends_list,3)) #// [ randomly choic 3 items ]
    print(random.shuffle(friends_list)) #// shuffle
    x=random.shuffle(friends_list) #// shuffle
    print(x) #// shuffle

    #smallcaps = 'abcdefghijklmnopqrstuvwxyz'
    #largecaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #digits = '0123456789'
    letters_numbers = string.ascii_letters + string.digits
    word = ''
    for i in range(7):
        word = word + random.choice(letters_numbers)
    print(word)

def test1():
    [x for x in range(1, 151) if not any([x % y == 0 for y in range(2, x)]) and not x == 1]
    return(1)

def test2():
    [x for x in range(2, 151) if not any([x % y == 0 for y in range(2, x)])]

def test3():
    # Initialize a list
    primes = []
    for possiblePrime in range(2, 151):
    # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)

def performance_and_timeit_module_test():
    #import timeit

    def is_prime_number(x):
        print([y for y in range(2, x)])
        print([ f'{x} % {y} == { x % y}' for y in range(2, x)])
        print([x % y == 0 for y in range(2, x)])
        print( any([x % y == 0 for y in range(2, x)]) )
        print( f' {x} is not a prime number' if any([x % y == 0 for y in range(2, x)]) else f'{x} is a prime number')
    
    is_prime_number(7)
    
    print('')
    print(timeit.timeit('test1()', globals=globals(), number=10))
    print(timeit.timeit('test2()', globals=globals(), number=10))
    print(timeit.timeit('test3()', globals=globals(), number=10))  

print('-- start --')
performance_and_timeit_module_test()
print('-- end --')
