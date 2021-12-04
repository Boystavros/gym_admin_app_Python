from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.fit_class_repository as fit_class_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    return render_template("/bookings/index.html")

@bookings_blueprint.route("/bookings/new_booking")
def new_booking():
    return render_template("/bookings/new_booking.html")

@bookings_blueprint.route("/bookings/new_booking", methods=['POST'])
def create_booking():
    member = member_repository.select()
    booking_repository.save()