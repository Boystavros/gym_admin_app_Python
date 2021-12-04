from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member

import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    # select all function for members from repo
    return render_template("/members/index.html")

@members_blueprint.route("/members/add_member")
def add_member():
    return render_template("/members/add_member.html")