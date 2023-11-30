from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecretkey"


class LoginForm(FlaskForm):
    username = StringField(label="UserName")
    password = PasswordField(label="Password")
    birthday = DateField(label="Birthday", format='%m/%d/%Y')
    submit = SubmitField(label="Log In")


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        login_form = LoginForm()
        return render_template('login.html', form=login_form)
    if request.method == "POST":
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
