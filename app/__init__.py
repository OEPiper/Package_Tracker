from flask import Flask, render_template, redirect
from .config import Config
from .shipping_form import PackageForm

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def index():
    return "<h1>Package Tracker</h1>"

@app.route("/new_package", methods=["GET", "POST"])
def create_new_package():
    form = PackageForm()
    if form.validate_on_submit():
        return redirect("/")
    if form.errors:
        print(form.errors)
        return render_template("shipping_request.html", form=form, errors=form.errors)

    return render_template('shipping_request.html', form=form, errors=None)
