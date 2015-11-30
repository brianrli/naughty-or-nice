from app import app, cas
from app.models import *
from flask import render_template, redirect
from flask_cas import CAS
from forms import UserForm, EditUserForm

@app.route('/')
@app.route('/index')
def index():
    if cas.username is None:
        return redirect('/login')
    user = Player.query.filter(Player.netid==cas.username).first()
    if user is None:
        return redirect('/newuser')
    return render_template('index.html',name = user.name, naughty=user.is_naughty, message = user.message)

@app.route('/newuser', methods = ['GET', 'POST'])
def newuser():
    # not logged into CAS
    if cas.username is None:
        return redirect('login')
    
    # Already logged in
    if Player.query.filter(Player.netid==cas.username).first() is not None:
        return redirect('/index')

    form = UserForm()
    
    # validated form
    if form.validate_on_submit():
        # pre-existing user
        p = Player.query.filter(Player.email==form.email.data).first()
        if p is not None:
            p.netid = cas.username
            # db.session.add(p)
            db.session.commit()
            return redirect('/index')

    return render_template('newuser.html',form=form,validnumber=1,validname=1,validpass=1)