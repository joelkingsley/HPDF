from flask import Flask,render_template,make_response,request,send_file,redirect,url_for
from urllib.request import urlopen
import json
from requests import get

app = Flask(__name__)

class Author:
	def __init__(self,name,id):
		self.name = name
		self.id = id
		self.pCount = 0 

@app.route('/')
def greet():
    return "Hello World - Joel Kingsley"
	
@app.route('/authors')
def fetchAndDisplay():
	urlAuthors = "https://jsonplaceholder.typicode.com/users"
	urlPosts = "https://jsonplaceholder.typicode.com/posts"
	
	with urlopen(urlAuthors) as conn:
		aList = json.loads(conn.read().decode())
	with urlopen(urlPosts) as conn:
		pList = json.loads(conn.read().decode())

	resp = requests.get(url=url, params=params)
	data = json.loads(resp.text)
			
	authors = [Author(aList[i]["name"],aList[i]["id"]) for i in range(len(aList))]
	
	print("Staring Count loop")
	for author in authors:
		for post in pList:
			if post["userId"] == author.id:
				author.pCount = author.pCount + 1
		
	return render_template("authors.html",authors=authors)

@app.route('/setcookie')
def setCookie():
        resp = make_response("Set cookie")
        resp.set_cookie('name', 'Joel')
        resp.set_cookie('age','20')
        return resp

@app.route('/getcookie')
def getCookie():
        name = request.cookies.get('name')
        age = request.cookies.get('age')
        #return render_template("getcookie.html",name=name,age=age)
        return str("Name: " + name)

@app.route('/robots.txt')
def deny():
        url = "http://httpbin.org/deny"
        return render_template("deny.html")

##@app.route('/html')
##def renderHTML():
##        return render_template("example_render.html")

@app.route('/image')
def renderImage():
        return send_file("iVHfwLc.gif", mimetype='image/gif')
        
@app.route('/input')
def displayForm():
        return render_template("input.html")


@app.route('/input', methods=['POST'])
def sendText():
##    text = request.form['text']
##    processed_text = text.upper()
        return redirect(url_for('receiveAndDisplayText'), code=307)

@app.route('/result', methods=['POST'])
def receiveAndDisplayText():
        text = request.form['text']
        print(text)
        return text

if __name__=='__main__':
	app.run(debug=True, port=8081)
