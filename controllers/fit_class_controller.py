from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.fit_class import Fit_class
import repositories.fit_class_repository as fit_class_repository

fit_classes_blueprint = Blueprint("fit_classes", __name__)

@fit_classes_blueprint.route("/fit_classes")
def fit_classes():
    fit_classes = fit_class_repository.select_all()
    return render_template("/classes/index.html", fit_classes=fit_classes)

@fit_classes_blueprint.route("/fit_classes/add_fit_class")
def add_fit_class():
    return render_template("/classes/add_fit_class.html")