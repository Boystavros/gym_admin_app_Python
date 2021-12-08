from datetime import date
import pdb
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from flask.helpers import url_for
from controllers.member_controller import members
from models.fit_class import Fit_class
import repositories.fit_class_repository as fit_class_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository
import repositories.instructor_repository as instructor_repository

fit_classes_blueprint = Blueprint("fit_classes", __name__)

@fit_classes_blueprint.route("/fit_classes")
def fit_classes():
    fit_classes = fit_class_repository.select_all()
    return render_template("/classes/index.html", fit_classes=fit_classes)

@fit_classes_blueprint.route("/classes/add", methods=['POST'])
def add_class():
    unformatted_date = request.form['date']
    year = unformatted_date[0:4]
    month = unformatted_date[5:7]
    day = unformatted_date[8:10]
    date = f"{day}-{month}-{year}"

    name = request.form['name']
    category = request.form['category']
    instructor = request.form['instructor']
    time = request.form['time']
    location = request.form['location']
    fit_class = Fit_class(name, category, instructor, date, time, location)
    fit_class_repository.save(fit_class)
    return redirect(url_for('.fit_classes'))

@fit_classes_blueprint.route("/classes/<id>")
def show(id):
    # pdb.set_trace()
    members = member_repository.select_all()
    # instructors = 
    fit_class = fit_class_repository.select(id)
    # attendees = member_repository.attendees(fit_class)
    bookings = booking_repository.bookings_by_class(fit_class)
    return render_template("classes/show.html", fit_class=fit_class, members=members, bookings=bookings)

@fit_classes_blueprint.route("/classes/<id>/delete")
def delete(id):
    fit_class_repository.delete(id)
    return redirect(url_for(".fit_classes"))

@fit_classes_blueprint.route("/classes/<id>/edit")
def edit_details(id):
    fit_class = fit_class_repository.select_for_edit(id)
    return render_template("classes/edit.html", fit_class=fit_class)

@fit_classes_blueprint.route("/classes/update/<id>", methods=['POST'])
def update(id):
    unformatted_date = request.form['date']
    year = unformatted_date[0:4]
    month = unformatted_date[5:7]
    day = unformatted_date[8:10]
    date = f"{day}-{month}-{year}"

    name = request.form['name']
    category = request.form['category']
    instructor = request.form['instructor']
    time = request.form['time']
    location = request.form['location']
    fit_class = Fit_class(name, category, instructor, date, time, location, id)
    fit_class_repository.update(fit_class)
    return redirect("/fit_classes")


