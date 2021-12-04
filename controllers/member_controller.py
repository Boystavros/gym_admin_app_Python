from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("/members/index.html", members=members)

@members_blueprint.route("/members/add_member")
def add_member():
    return render_template("/members/add_member.html")

@members_blueprint.route("/members/show/<id>")
def select(id):
    member = member_repository.select(id)
    return render_template("/members/show.html", member=member)

@members_blueprint.route("/members/update/<id>")
# start here