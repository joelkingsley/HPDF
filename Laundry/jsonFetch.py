from urllib.request import urlopen
import json

class Author:
	def __init__(self,name,id):
		self.name = name
		self.id = id
		self.pCount = 0

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

for author in authors:
	print(author.name + ' ' + str(author.pCount))