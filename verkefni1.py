from bottle import route, run

@route('/')

def index():
    return"""
    <h2<verkefni 1</h1>
    <a href="/about">About</a>
    <a href="/bio">Biography</a>
    <a href="/pic">Pitcures</a>
    """
        
@route("/about")
def jobs():
    return "Hér eru upplýsngar um Steve Jobs"

def bio():
    return "Hér eru upplýsngar um Steve Jobs"
def pic():
    return "Hér eru myndir af Steve Jobs"

run(host='localhost',port=8080)


