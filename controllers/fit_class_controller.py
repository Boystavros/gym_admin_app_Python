from flask import Flask, render_template, request, redirect
from flask import Blueprint
from flask.helpers import url_for
from models.fit_class import Fit_class
import repositories.fit_class_repository as fit_class_repository

fit_classes_blueprint = Blueprint("fit_classes", __name__)

@fit_classes_blueprint.route("/fit_classes")
def fit_classes():
    fit_classes = fit_class_repository.select_all()
    return render_template("/classes/index.html", fit_classes=fit_classes)

@fit_classes_blueprint.route("/classes/add", methods=['POST'])
def add_class():
    name = request.form['name']
    category = request.form['category']
    instructor = request.form['instructor']
    date = request.form['date']
    time = request.form['time']
    location = request.form['location']
    fit_class = Fit_class(name, category, instructor, date, time, location)
    fit_class_repository.save(fit_class)
    return redirect(url_for('.fit_classes'))

