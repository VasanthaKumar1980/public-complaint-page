from flask import Flask, render_template, request, redirect, url_for
from model import db,Login, Complaint
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Vasanth%40123@localhost:3306/complaint'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

migrate = Migrate(app, db)

@app.route('/', methods=['POST','GET'])
def index():
      if request.method == 'POST':
          # Handle form submission
          pass
      return render_template('index.html')
@app.route('/login', methods=['POST','GET'])
def login():
   
   if request.method == 'POST':
        email = request.form['login_email']
        password = request.form['login_password']
        print(email, password)

        new_details = Login(email=email, password=password)
        db.session.add(new_details)
        db.session.commit()

        # ✅ POST success → redirect
        return redirect(url_for('complaint'))

   # ✅ GET request → show login page
   return render_template('login.html')




@app.route('/complaint', methods=['POST','GET'])
def complaint():
     if request.method == 'POST':

        complaint = request.form['complaint_name']
        email = request.form['complaint_email']
        category = request.form['complaint_category']
        description = request.form['complaint_description']


        complaint_1 = Complaint( complaint = complaint ,email=email,category=category,description=description)
        db.session.add(complaint_1)
        db.session.commit()
 
     return render_template('complaint.html')


@app.route('/pendings')
def pendings():

    pending_details =Complaint.query.all()
    return render_template('pendings.html', pending_details = pending_details)


@app.route('/edit/<int:id>', methods=['POST','GET'])
def edit(id):
    edit = Complaint.query.get(id)

    if request.method == 'POST':
        edit.complaint = request.form['complaint_name']
        edit.email = request.form['complaint_email']
        db.session.commit()
        return redirect(url_for('pendings'))

    return render_template('edit.html', edit=edit)


if __name__ == '__main__':
     app.run(debug=True)