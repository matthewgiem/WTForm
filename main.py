from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SubmitField
from wtforms.validators import DataRequired, InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecretkey"


class LoginForm(FlaskForm):
    username = StringField(label="UserName", validators=[DataRequired()])
    email = StringField(label="Email", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    birthday = DateField(label="Birthday", format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField(label="Log In")


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    print("not inside")
    if login_form.validate_on_submit():
        print("inside")
        return render_template('index.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
