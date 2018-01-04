# D:\python2\this.install\python
# coding:utf-8
import os 
import sys
import urllib2
import threading

# command like : Python build.py /var/www project_name [single/multiple:default is single]

params = sys.argv
try:
	path = params[1]
	name = params[2]
	mode = None
	length = len(params)
	if length==3:
		mode = 'single'
	if length==4:
		mode = params[3]
	if mode!='single' and mode!='multiple':
		print "Your mode is not right ! [single/multiple]"
		exit(0)
except Exception as e:
	print "At least two params is required ! Please check your command!"
	exit(0)
print "build path is %s , project name is %s and mode is %s" % (path,name,mode)

def single_mode_build():
	print "Single type flask application is building......"
	try:
		os.mkdir("templates")
		os.makedirs('static/js')
		os.makedirs('static/css')
		os.makedirs('static/image')
		os.makedirs('static/uploads')
	except Exception as e:
		print "FAIL : File or Directory already exists! Please check!"
		exit(0)
	with open("app.py",'wb') as file:
		content = "#!-*- coding:utf-8\r\nimport flask\r\nimport time\r\nimport json\r\n\r\n" \
				+"app = flask.Flask(__name__)\r\nreq = flask.request\r\n\r\n" \
				+"@app.route('/')\r\ndef index():\r\n\t" \
				+"return flask.render_template('index.html',data={'title':'hello!','content':'hello world!'})\r\n\r\n" \
				+"if __name__ == '__main__':\r\n\tapp.run(debug=True,host='0.0.0.0',port=5000)"
		file.write(content)
	with open("templates/index.html",'wb') as file:
		content = "<!DOCTYPE html>\r\n<html lang=\"en\">\r\n\t<head>\r\n\t\t"\
		+"<meta charset=\"UTF-8\">\r\n\t\t<title>{{data.title}}</title>"\
		+"\r\n\t\t<link href='/static/css/app.css' type='text/css' rel='stylesheet'>\r\n\t" \
		+"</head>\r\n\t<body>\r\n\t\t<h1>{{data.content}}</h1>\r\n\t</body>"\
		+"\r\n\t<script src='/static/js/jquery.js'></script>"\
		+"\r\n\t<script src='/static/js/app.js'></script>\r\n</html>"
		file.write(content)
	with open("static/css/app.css",'wb') as file:
		content = "*{padding:0;margin:0;}"
		file.write(content)
	with open("static/js/app.js",'wb') as file:
		content = "(function(){\r\n\tconsole.log('please input your code...')\r\n})()"
		file.write(content)
	with open("static/js/jquery.js",'wb') as file:
		req = urllib2.Request("https://cdn.bootcss.com/jquery/3.2.1/jquery.min.js")
		req_data = urllib2.urlopen(req)
		doc = req_data.read()
		file.write(doc)

def multiple_mode_build():
	pass

res=raw_input("Are you sure to build ? y/n : ")
if res=='y' or res=='yes':

	dir_exist = os.path.exists(path)
	if not dir_exist:
		print "The path you'v given is not exists!"
		exit(0)
	os.chdir(path)
	print "Current directory is : "+os.getcwd()

	#begin build
	if mode=="single":
		single_mode_build()
	else:
		multiple_mode_build()

	user_input = raw_input("Building ok! Run it now ? y/n : ")
	if user_input=='y' or user_input=='yes':
		os.system("python app.py")
	else:
		exit(0)

else:
	print "User canceal operation!"
	exit(0)




