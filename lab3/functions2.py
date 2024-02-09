#1
from dict_of_movies import movies
def score(name):
    for i in movies:
        if name == i['name'] and i['imdb'] > 5.5:
            return True
    return False
print(score(input()))

#2
from dict_of_movies import movies
def list():
    all = []
    for i in movies:
        if int(i['imdb']) > 5.5:
            all.append(i)
    print(all)
list()

#3
from dict_of_movies import movies
def category(ctg):
    cat = []
    for i in movies:
        if ctg == i['category']:
            cat.append(i)
    print(cat)
category(input())

#4
from dict_of_movies import movies
def avrg():
    all = 0
    num = len(movies)
    for i in movies:
        all += i['imdb']
    print(all/num)
avrg()

#5
from dict_of_movies import movies
def category(ctg):
    cat = []
    for i in movies:
        if ctg == i['category']:
            cat.append(i)
    all = 0
    num = len(cat)
    for i in cat:
        all += i['imdb']
    print(all/num)
category(input())