from flask import Flask, render_template,request
from flask import make_response

app =  Flask(__name__)

@app.route('/setcookie')
def setcookie():
	resp=make_response('Setting Cookie')
	resp.set_cookie('myname1','joel')
	resp.set_cookie('age1','20')
	return resp

@app.route('/getcookie')
def getcookie():
	myname = request.cookies.get('myname1')
	age=request.cookies.get('age1')
	return render_template('getcookie.html',myname=myname,age=age)
	
if __name__=="__main__":
	app.run(debug=True)