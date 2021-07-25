from flask import Flask, render_template, request,redirect
import pandas as pd
import pickle
import os
from werkzeug.utils import secure_filename

def function(data,con,var):
   pi=[]
   if con=='1':
      if var!='all':
         for name in var:
            mean_value=data[name].mean()
            data[name].fillna(value=mean_value, inplace=True)
         pi=data
      else:
         mean_value3=data.mean()
         data.fillna(value=mean_value3, inplace=True)
         pi=data
   elif con=='2': 
      if var!='all':
         for name in var:
             mean_value1=data[name].max()
             data[name].fillna(value=mean_value1, inplace=True)
         pi=data
      else:
         mean_value2=data.max()
         data.fillna(value=mean_value2, inplace=True)
         pi=data
   elif con=='3': 
      if var!='all':
         for name in var:
            data[name].fillna(value=0, inplace=True)
         pi=data
      elif var=='all':
         data.fillna(value=0, inplace=True)
         pi=data
   elif con=='4': 
      if var!='all':
         for name in var:
            data=data
         pi=data
      elif var=='all':
         data=data
         pi=data
   else:
      print('no input')
   return pi


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "C:\\Users\\SVMY\\Downloads\\project\\part2\\static"

@app.route('/')
def student():
   return render_template('index.html')


@app.route('/success',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.files['file']
      df=pd.read_csv(result, error_bad_lines=False)
      outfile = open("test",'wb')
      pickle.dump(df,outfile)
      outfile.close()
      null=df.isnull().sum()
      null2=df.shape
      return render_template("result.html", name = df.to_html(),null=null,null2=null2)  

@app.route('/success2')      
def result2():
   infile = open("test",'rb')
   new_dict = pickle.load(infile)
   new_dict.dropna(inplace=True)
   return render_template("result2.html",result2=new_dict.to_html())

@app.route('/from')
def from45():
   infile = open("test",'rb')
   data = pickle.load(infile)
   cl=list(data.columns)
   return render_template('from.html',cl=cl)



@app.route('/final',methods = ['POST', 'GET'])
def final():
   infile = open("test",'rb')
   data = pickle.load(infile)
   if request.method == 'POST':
      select = request.form.get("select")
      select4 = request.form.get("group1")
      select2 = request.form.getlist("sel[]")
      select3 = request.form.getlist("sel5[]")
      
      ft=function( data,select, select2)
      if select4=='all':
         function( data,select, select4)
      gf=['']
      if select3==gf:
         return render_template('final.html',null=ft.to_html(),null2=select3)
      else:
         lp=ft.drop(select3, axis = 1)
         return render_template('final.html',null=lp.to_html(),null2=select3)
if __name__ == '__main__':
   app.run(debug=True)
