import pdb
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from flask.helpers import url_for
from models.member import Member
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("/members/index.html", members = members)

@members_blueprint.route("/members/add_member", methods=['POST'])
def create_member():
    unformatted_dob = request.form['dob']
    year = unformatted_dob[0:4]
    month = unformatted_dob[5:7]
    day = unformatted_dob[8:10]
    dob = f"{day}-{month}-{year}"
    
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    title = request.form['title']
    pronouns = request.form['pronouns']
    membership = request.form['membership']
    notes = request.form['notes']
    member = Member(first_name, last_name, dob, title, pronouns, membership, notes)
    member_repository.save(member)
    return redirect(url_for('.members'))

@members_blueprint.route("/members/<id>")
def select(id):
    member = member_repository.select(id)
    bookings = booking_repository.bookings_by_member(member)
    return render_template("/members/show.html", member = member, bookings=bookings)

@members_blueprint.route("/members/<id>/edit")
def edit_details(id):
    member = member_repository.select_for_edit(id)
    return render_template("members/edit.html", member = member)

@members_blueprint.route("/members/update/<id>", methods=['POST'])
def update(id):
    unformatted_dob = request.form['dob']
    year = unformatted_dob[0:4]
    month = unformatted_dob[5:7]
    day = unformatted_dob[8:10]
    dob = f"{day}-{month}-{year}"

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    title = request.form['title']
    pronouns = request.form['pronouns']
    membership = request.form['membership']
    notes = request.form['notes']
    member = Member(first_name, last_name, dob, title, pronouns, membership, notes, id)
    member_repository.update(member)
    return redirect(f"/members/{id}")

@members_blueprint.route("/members/<id>/delete")
def delete(id):
    member_repository.delete(id)
    return redirect(url_for('.members'))