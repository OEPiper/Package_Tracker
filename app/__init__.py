from flask import Flask, render_template, redirect
from .config import Config
from .shipping_form import PackageForm
from flask_migrate import Migrate
from .models import db, Package
from map.map import advance_delivery, DELIVERED

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)



@app.route("/")
def index():
    packages = Package.query.all()
    return render_template('package_status.html', packages=packages)

@app.route("/new_package", methods=["GET", "POST"])
def create_new_package():
    form = PackageForm()
    if form.validate_on_submit():
        data = form.data
        new_package = Package(sender=data["sender"],
                              recipient=data["recipient"],
                              origin=data["origin"],
                              destination=data["destination"],
                              location=data["origin"])
        db.session.add(new_package)
        db.session.commit()
        Package.advance_all_locations()
        return redirect('/')
    if form.errors:
        print(form.errors)
        return render_template("shipping_request.html", form=form, errors=form.errors)

    return render_template('shipping_request.html', form=form, errors=None)
