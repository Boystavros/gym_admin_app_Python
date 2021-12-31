import pdb
from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.fit_class_repository as fit_class_repository

bookings_blueprint = Blueprint("bookings", __name__)

error = {
    0: "Cannot create booking as class is full. Please choose another class.",
    1: "Cannot update booking as class is full. Booking unchanged.",
    2: "Cannot create booking as class is during peak hours. Please upgrade membership category or select off-peak class.",
    3: "Cannot update booking as class is during peak hours and selected member has off-peak membership. Booking unchanged."
}

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

    if ("07:00" < fit_class.time < "0900") or ("17:00" < fit_class.time < "19:00"):
        peak_class = True
    else:
        peak_class = False

    if peak_class and member.membership == "off-peak":
        error_code = 2
        return redirect(f"/bookings/error/{error_code}")
    else:
        if fit_class.capacity > fit_class.attendees:
            booking = Booking(member, fit_class, staff_member)
            booking_repository.save(booking)
            return redirect("/bookings")
        else:
            error_code = 0
            return redirect(f"/bookings/error/{error_code}")

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
    current_fit_class_id = booking_repository.select(id).fit_class.id
    form_fit_class_id = request.form['fit_class_id']
    fit_class = fit_class_repository.select(request.form['fit_class_id'])
    staff_member = request.form['staff_member']

    if ("07:00" < fit_class.time < "0900") or ("17:00" < fit_class.time < "19:00"):
        peak_class = True
    else:
        peak_class = False

    if peak_class and member.membership == "off-peak":
        error_code = 3
        return redirect(f"/bookings/error/{error_code}")
    else:
        if current_fit_class_id != form_fit_class_id and fit_class.capacity > fit_class.attendees:
            booking = Booking(member, fit_class, staff_member, datetime.now(), id)
            booking_repository.update(booking)
            return redirect("/bookings")
        else:
            error_code = 1
            return redirect(f"/bookings/error/{error_code}")


@bookings_blueprint.route("/bookings/class/<id>/create", methods=['POST'])
def class_create(id):
    member = member_repository.select(request.form['member_id'])
    fit_class = fit_class_repository.select(request.form['fit_class_id'])
    staff_member = request.form['staff_member']
    if fit_class.capacity > fit_class.attendees:
        booking = Booking(member, fit_class, staff_member)
        booking_repository.save(booking)
        return redirect(f"/classes/{id}")
    else:
        error_code = 0
        return redirect(f"/bookings/error/{error_code}")
    

@bookings_blueprint.route("/bookings/class<class_id>/<booking_id>/delete")
def class_delete(class_id, booking_id):
    booking_repository.delete(booking_id)
    return redirect(f"/classes/{class_id}")

@bookings_blueprint.route("/bookings/error/<error_code>")
def display_error(error_code):
    error_message = error[int(error_code)]
    return render_template("/bookings/error.html", error_message=error_message)