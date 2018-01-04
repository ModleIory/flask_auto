# flask_auto  

### main to build flask multiple applications frame automatical   
	* controllers:the route and control methods
	* models:database methods
	* templates:the view file 
	* static:public source file
	* app.py:execute and run server with command: python app.py
	* build.py:execute and build new project with command: python app.py  
		```
		python build.py /var/www project_name [single/multiple:default is single]
		```
	* buildsql.py:execute and build the mysql databases or update  

### show flask mysql deal
	* pip install flask-sqlalchemy==2.0.0【2.3.2】 
		* 2.3.2 when I create table , this is available  
		* 2.0.0 when I doing sql operation , this is available  
		* run command only can create db,can't update.I can add field in db and models file, this would be better
	* pip install pymysql

### does python has package manager like npm
	* pip freeze > package.txt # record the dependencies 
	* pip install -r package.txt # install the dependencies 