
from sys import argv

import bottle

from bottle import*



@route('/')



def a():

    return"""

    <h2<verkefni 1</h1>

    <a href="/sida/1">LiðurA</a>

    <a href="/sida/2">LiðurB</a>

    

    """

@route("/sida/<id>")


@route("/page1")
def page(id):
    if id=="1":
        return"þetta er síða 1 <br><a href='/a'>Til baka</a>"
    if id=="2":
        return"þetta er síða 2 <br><a href='/a'>Til baka</a>"
def index():
    return template("index1.tp1")


@error(404)
def villa(error):
    return "<h2 style='color:red'>Þessi síða fannst ekki</h2>"
#run(host='localhost',port=8080)



bottle.run(host='0.0.0.0',port=argv[1])
