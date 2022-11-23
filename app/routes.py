from app import app, db
from flask import render_template, redirect, url_for, flash
from app.models import Item, User
from app.forms import RegisterForm


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/inventory")
def inventory():
    items = Item.query.all()
    return render_template("inventory.html", items=items)


@app.route("/register", methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit(): # user clicked on submit button
        user_to_create = User(username=register_form.username.data, email=register_form.email.data, password=register_form.password.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for("home_page"))
    if register_form.errors:
        for form_error in register_form.errors.values():
            flash(f"Error creating user: {form_error}", category="danger")
    return render_template('register.html', register_form=register_form)