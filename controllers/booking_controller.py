import pdb
from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.fit_class_repository as fit_class_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def index():
    bookings = booking_repository.select_all()
    members = member_repository.select_all()
    fit_classes = fit_class_repository.select_all()
    return render_template("/bookings/index.html", bookings=bookings, members=members, fit_classes=fit_classes)

@bookings_blueprint.route("/bookings/create", methods=['POST'])
def create():
    member = member_repository.select(request.form['member_id'])
    fit_class = fit_class_repository.select(request.form['fit_class_id'])
    staff_member = request.form['staff_member']
    booking = Booking(member, fit_class, staff_member)
    booking_repository.save(booking)
    fit_class.increase_attendees()
    fit_class_repository.update(fit_class)
    return redirect("/bookings")

@bookings_blueprint.route("/bookings/<id>/delete")
def delete(id):
    booking_repository.delete(id)
    return redirect("/bookings")

@bookings_blueprint.route("/bookings/<id>/edit")
def edit(id):
    members = member_repository.select_all()
    fit_classes = fit_class_repository.select_all()
    booking = booking_repository.select(id)
    return render_template("bookings/edit.html", booking=booking, members=members, fit_classes=fit_classes)

@bookings_blueprint.route("/bookings/update/<id>", methods=['POST'])
def update(id):
    member = member_repository.select(request.form['member_id'])
    fit_class = fit_class_repository.select(request.form['fit_class_id'])
    staff_member = request.form['staff_member']
    booking = Booking(member, fit_class, staff_member, datetime.now(), id)
    booking_repository.update(booking)
    return redirect("/bookings")


@bookings_blueprint.route("/bookings/class/<id>/create", methods=['POST'])
def class_create(id):
    member = member_repository.select(request.form['member_id'])
    fit_class = fit_class_repository.select(request.form['fit_class_id'])
    staff_member = request.form['staff_member']
    booking = Booking(member, fit_class, staff_member)
    booking_repository.save(booking)
    fit_class.increase_attendees()
    fit_class_repository.update(fit_class)
    return redirect(f"/classes/{id}")

@bookings_blueprint.route("/bookings/class<class_id>/<booking_id>/delete")
def class_delete(class_id, booking_id):
    booking_repository.delete(booking_id)
    return redirect(f"/classes/{class_id}")