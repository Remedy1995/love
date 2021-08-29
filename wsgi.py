import json
import requests
from flask import Flask, request,render_template
import sys
import http.client


app = Flask(__name__)
app = Flask(__name__, static_url_path='')
def footer():
    information='Enjoy all about love'
    return information
@app.route('/')
def index():
    return render_template('search.html',header='Love Calculator',footer=footer())
if __name__=='__main__':
 app.run(debug=True)

@app.route('/',methods=['POST'])
def postdata():
 fname=request.form['fname'] 
 lname=request.form['lname'] 
 if not fname:
    return render_template('search.html',header='Love Calculator',footer=footer())
 elif not lname:
     return render_template('search.html',header='Love Calculator',footer=footer()) 
 conn = http.client.HTTPSConnection("love-calculator.p.rapidapi.com")

 headers = {
    'x-rapidapi-host': "love-calculator.p.rapidapi.com",
    'x-rapidapi-key': "f57711721emsh7ff04b13e522dacp10a7a4jsn4863b56feff4"
    }

 conn.request("GET", "/getPercentage?fname="+fname+"&sname="+lname, headers=headers)

 res = conn.getresponse()
 data = res.read()
#load the json to a string
 resp = json.loads(data)
 percentage= (str(resp['percentage']))
 fname=(str(resp['fname']))
 lname=(str(resp['sname']))
 result=(str(resp['result']))
#  return result
 return render_template('index.html',percentage=percentage,fname=fname,lname=lname,result=result)
