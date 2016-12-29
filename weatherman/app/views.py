from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requestd for OpenID={}, remeber_me={}'.format(form.openid.data, str(form.remeber_me.data)))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])

