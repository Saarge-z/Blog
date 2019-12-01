from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug import secure_filename
from flask_mail import Mail
import json
import os
import math
from datetime import datetime

with open("config.json", "r") as c:
    params = json.load(c)["params"]
#local_server=True

app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['UPLOAD_FOLDER'] = params['upload_location']
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD = params['gmail-password']
)
mail = Mail(app)
if (params["local_server"]):
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]

db = SQLAlchemy(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    email = db.Column(db.String(30), nullable = False)
    phone_num = db.Column(db.String(12), nullable = False)
    msg = db.Column(db.String(120), nullable = False)
    date = db.Column(db.String(12), nullable = True)
    

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80), nullable = False)
    slug = db.Column(db.String(21), nullable = False)
    content = db.Column(db.String(150), nullable = False)
    tagline = db.Column(db.String(150), nullable = False)
    date = db.Column(db.String(12), nullable = True)
    img_file = db.Column(db.String(12), nullable = True)


class Notice(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    note = db.Column(db.String(80), nullable = False)
    date = db.Column(db.String(12), nullable = True)


@app.route('/')
def home():
    posts = Posts.query.filter_by().all()
    last = math.ceil(len(posts)/int(params['no_of_posts']))
    #[0:params['no_of_posts']]
    

    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page-1)*int(params['no_of_posts']) : (page-1)*int(params['no_of_posts']) + int(params['no_of_posts'])]
    #pagination logic
    #First
    if (page ==1):
        prev='#'
        next = "/?page=" + str(page + 1)
    elif(page == last):
        prev="/?page=" + str(page - 1)
        next = '#'
    else:
        prev = "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)

    return render_template('index.html', params = params, posts = posts, prev=prev, next=next)

@app.route('/post/<string:post_slug>', methods = ["GET"])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params = params, post=post)

@app.route('/about')
def about():
    return render_template('about.html', params = params)

@app.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():
    if ('user' in session and session['user'] == params['admin_user']):
        posts = Posts.query.all()
        return render_template('dashboard.html', params = params, posts = posts) 


    if request.method=="POST":
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if (username == params['admin_user'] and userpass ==params['admin_password']):
            #set session variable
            session['user'] = username

            posts = Posts.query.all()
            return render_template('dashboard.html', params = params, posts = posts)

    return render_template('login.html', params = params)

@app.route("/edit/<string:sno>/", methods = ['GET', 'POST'])
def edit(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == "POST":            
            box_title = request.form.get('title')
            tline = request.form.get('tline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            date = datetime.now()
            
            
            post = Posts.query.filter_by(sno=sno).first()
            post.title = box_title
            post.slug = slug
            post.content = content
            post.tagline = tline
            post.img_file = img_file
            post.date = date
            db.session.commit()
            return redirect('/edit/' + sno)
        post = Posts.query.filter_by(sno = sno).first()
        return render_template('edit.html', params = params, post = post)


@app.route("/addpost", methods = ['GET', 'POST'])
def addpost():
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == "POST":
            box_title = request.form.get('title')
            tline = request.form.get('tline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            date = datetime.now()
            
            post = Posts(title = box_title, slug = slug, content = content, tagline = tline, img_file = img_file, date = date)
            db.session.add(post)
            db.session.commit()    
        return render_template('addpost.html', params = params)


@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
    if ('user' in session and session['user'] == params['admin_user']):
        if (request.method == "POST"):
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename) ))
            return "Upload Successfully"



@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashboard')


@app.route('/delete/<string:sno>', methods = ['GET', 'POST'])
def delete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        post = Posts.query.filter_by(sno = sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')



@app.route('/deletenotice/<string:sno>', methods = ['GET', 'POST'])
def deletenotice(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        notice = Notice.query.filter_by(sno = sno).first()
        db.session.delete(notice)
        db.session.commit()
    return redirect('/addnotice')



@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    if (request.method == 'POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        entry = Contacts(name = name,  email = email, phone_num = phone, msg = message, date = datetime.now())
        db.session.add(entry)
        db.session.commit()
        mail.send_message('ADC blog update from '+ name, 
                          sender = email, 
                          recipients = [params['gmail-user']], 
                          body = message + "\n" + phone
                          )
    return render_template('contact.html', params = params)


#This is jugaad Fix it
@app.route('/notice/<string:pageno>', methods = ['GET'])
def noticeloop(pageno):
    notice = Notice.query.filter_by().all()
    last = math.ceil(len(notice)/int(params['no_of_posts']))
    #[0:params['no_of_posts']]
    
    pageno = int(pageno)
    notice = notice[(pageno-1)*int(params['no_of_posts']) : (pageno-1)*int(params['no_of_posts']) + int(params['no_of_posts'])]
    #pagination logic
    #First
    if (pageno ==1):
        prev='#'
        next = "/notice/" + str(pageno + 1)
    elif(pageno == last):
        prev="/notice/" + str(pageno - 1)
        next = '#'
    else:
        prev = "/notice/" + str(pageno - 1)
        next = "/notice/" + str(pageno + 1)
    return render_template('notice.html', params = params, notice = notice, prev=prev, next=next)

@app.route('/notice', methods = ['GET'])
def noticedisp():
    notice = Notice.query.filter_by().all()
    last = math.ceil(len(notice)/int(params['no_of_posts']))
    #[0:params['no_of_posts']]
    

    pageno = request.args.get('pageno')
    if (not str(pageno).isnumeric()):
        pageno = 1
    pageno = int(pageno)
    notice = notice[(pageno-1)*int(params['no_of_posts']) : (pageno-1)*int(params['no_of_posts']) + int(params['no_of_posts'])]
    #pagination logic
    #First
    if (pageno ==1):
        prev='#'
        next = "/notice/" + str(pageno + 1)
    elif(pageno == last):
        prev="/notice/" + str(pageno - 1)
        next = '#'
    else:
        prev = "/notice/" + str(pageno - 1)
        next = "/notice/" + str(pageno + 1)

    return render_template('notice.html', params = params, notice = notice, prev=prev, next=next)
#Jugaad ends it - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

@app.route('/addnotice', methods = ['GET', 'POST'])
def notice():
    if ('user' in session and session['user'] == params['admin_user']):
        notice = Notice.query.filter_by().all()
        
        if request.method == "POST":
            note = request.form.get('note')
            date = datetime.now()
            entry = Notice(note = note, date = date)
            db.session.add(entry)
            db.session.commit()
            return redirect('/addnotice')
        return render_template('addnotice.html', params = params, notice=notice)


app.run(debug=True)