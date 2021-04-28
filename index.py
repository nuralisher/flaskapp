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

		# code=request.form['code']
		inp=request.form['input']
		# chk=request.form.get('check')

		# if  not chk=='1':
		# 	inp=""
		# 	check=''
		# else:
		# 	check='checked'	

		output=complier_output(inp)
	return render_template('home.html',input=inp,output=output)

def complier_output(inp):
	# if not os.path.exists('Try.cpp'):
	# 	os.open('Try.cpp',os.O_CREAT)
	# fd=os.open("Try.cpp",os.O_WRONLY)
	# os.truncate(fd,0)
	# fileadd=str.encode(code)
	# os.write(fd,fileadd)
	# os.close(fd)
	s=subprocess.run(['g++','-o','new.exe','Try.cpp'],stderr=PIPE,)
	check=s.returncode
	if check==0:
		# if chk=='1':
		# 	r=subprocess.run(["new.exe"],input=inp.encode(),stdout=PIPE)
		# else:
		# 	r=subprocess.run(["new.exe"],stdout=PIPE)
		r=subprocess.run(["new.exe"],input=inp.encode(),stdout=PIPE)
		return r.stdout.decode("utf-8")
	else:
		return s.stderr.decode("utf-8")


if __name__=='__main__':
	app.run(debug=True)
