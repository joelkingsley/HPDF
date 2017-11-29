from flask import Flask,render_template
from urllib.request import urlopen
import json

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
			
	authors = [Author(aList[i]["name"],aList[i]["id"]) for i in range(len(aList))]
	
	print("Staring Count loop")
	for author in authors:
		for post in pList:
			if post["userId"] == author.id:
				author.pCount = author.pCount + 1
		
	return render_template("authors.html",authors=authors)

if __name__=='__main__':
	app.run(debug=True, port=8080)