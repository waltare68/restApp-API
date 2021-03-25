from sqlite3.dbapi2 import converters
from flask import Flask,render_template,request

import sqlite3 as sql
from jinja2.utils import contextfunction

from werkzeug import exceptions

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def new_student():
    return render_template('student.html')


@app.route('/addrec',methods=['POST','GET'])
def addrec():
    if request.method =='POST':
        try:
            name=request.form['name']
            branch=request.form['branch']
            college=request.form['college']
            batch=request.form['batch']
            program=request.form['program']
            course=request.form['course']
            firstLang=request.form['firstLang']

            with sql.connect("database.db") as con:
                cur =con.cursor() 
                cur.execute("iNSERT INTO studens (name,branch,college,batch,program,course,firstlang) VALUES (?,?,?,?,?,?,?)",(name,branch,college,batch,program,course,firstlang))
                con.commit()  
                msg="Record successfully added"
        except:
            con.rollback()
            msg="error in insert operation"
        finally:
            return render_template("result.html",msg=msg)
            con.close()
@app.route('/list')
def list():
    con=sql.connect("database.db")
    con.row_factory=sql.Row

    cur =con.cursor()
    cur.execute("select * from students")

    rows =cur.fetchall()

    return render_template('list.html',rows=rows)

     

# Run Server
if __name__ == '__main__':
  app.run(debug=True) 