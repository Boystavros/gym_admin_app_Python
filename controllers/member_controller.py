from flask import Flask, render_template, request, redirect
from flask import Blueprint
from flask.helpers import url_for
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("/members/index.html", members = members)

@members_blueprint.route("/members/add_member", methods=['POST'])
def create_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    dob = request.form['dob']
    title = request.form['title']
    pronouns = request.form['pronouns']
    notes = request.form['notes']
    member = Member(first_name, last_name, dob, title, pronouns, notes)
    member_repository.save(member)
    return redirect(url_for('.members'))

@members_blueprint.route("/members/show/<id>")
def select(id):
    member = member_repository.select(id)
    return render_template("/members/show.html", member = member)

@members_blueprint.route("/members/<id>/edit")
def edit_details(id):
    member = member_repository.select(id)
    return render_template("members/edit.html", member = member)

@members_blueprint.route("/update/<id>", methods=['POST'])
def update(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    dob = request.form['dob']
    title = request.form['title']
    pronouns = request.form['pronouns']
    notes = request.form['notes']
    member = Member(first_name, last_name, dob, title, pronouns, notes, id)
    member_repository.update(member)
    return redirect(f"/members/show/{id}")

@members_blueprint.route("/members/<id>/delete")
def delete(id):
    member_repository.delete(id)
    return redirect(url_for('.members'))