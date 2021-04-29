from flask import Flask,render_template,request
import subprocess,os
from subprocess import PIPE

app = Flask(__name__)

@app.route('/')
def Compiler():
	check=''
	return render_template('home.html',check=check)

@app.route('/submit',methods=['GET','POST'])
def submit():
	if request.method=='POST':
		inp=request.form['input']
		output=complier_output(inp)
	return render_template('home.html',input=inp,output=output)

def complier_output(inp):
	s=subprocess.run(['g++','-o','new.exe','Try.cpp'],stderr=PIPE,)
	check=s.returncode
	if check==0:
		r=subprocess.run(["new.exe"],input=inp.encode(),stdout=PIPE)
		return r.stdout.decode("utf-8")
	else:
		return s.stderr.decode("utf-8")


if __name__=='__main__':
	app.run(debug=True)
