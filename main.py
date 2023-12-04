from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecretkey"


class LoginForm(FlaskForm):
    username = StringField(label="UserName", validators=[DataRequired(), Length(min=-1, max=8, message="8 max")])
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
    if request.method == "POST":
        if login_form.email.data == "matthew@gmail.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    if login_form.validate_on_submit():
        print(login_form.email.data)
        return render_template('index.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
