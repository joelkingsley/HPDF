from urllib.request import urlopen
import json
import requests
from flask import Flask,render_template,make_response,request,send_file,redirect,url_for

class Author:
	def __init__(self,name,id):
		self.name = name
		self.id = id
		self.pCount = 0
		
app = Flask(__name__)

urlAuthors = "https://jsonplaceholder.typicode.com/users"
urlPosts = "https://jsonplaceholder.typicode.com/posts"
#with urlopen(urlAuthors) as conn:
	#aList = json.loads(conn.read().decode())
#with urlopen(urlPosts) as conn:
#	pList = json.loads(conn.read().decode())

#resp = requests.get(url=urlAuthors)
#data = json.loads(resp.text)
#with urlopen(urlAuthors) as conn:
#	aList = json.loads(conn.read().decode())
#with urlopen(urlPosts) as conn:
#	pList = json.loads(conn.read().decode())
		
#authors = [Author(aList[i]["name"],aList[i]["id"]) for i in range(len(aList))]

#print("Staring Count loop")
#for author in authors:
#	for post in pList:
#		if post["userId"] == author.id:
#			author.pCount = author.pCount + 1

#for author in authors:
#	print(author.name + ' ' + str(author.pCount))
#print(data[2]["name"])
@app.route('/getcookie')
def getCookie():
        name = request.cookies.get('mname')
        age = request.cookies.get('age')
        #return render_template("getcookie.html",name=name,age=age)
        return str("Name: " + name)
		
if __name__=='__main__':
	app.run(debug=True, port=8080)