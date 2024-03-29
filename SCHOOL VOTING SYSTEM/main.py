from flask import Flask, render_template
from Forms import RegistrationForm, LoginForm

app = Flask(__name__)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template("registration.html", title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template("login.html", title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)
