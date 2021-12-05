from db.run_sql import run_sql
from models.member import Member
from models.fit_class import Fit_class
from models.booking import Booking
import repositories.fit_class_repository as fit_class_repository
import repositories.booking_repository as booking_repository

#CREATE
def save(member):
    sql = "INSERT INTO members (first_name, last_name, dob, title, pronouns, notes) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [member.first_name, member.last_name, member.dob, member.title, member.pronouns, member.notes]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
    return member

#READ
def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = Member(row['first_name'], row['last_name'], row['dob'], row['title'], row['pronouns'], row['notes'], row['id'])
        members.append(member)
    return members

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['first_name'], result['last_name'], result['dob'], result['title'], result['pronouns'], result['notes'], result['id'])
    return member

#UPDATE
def update(member):
    sql = "UPDATE members SET (first_name, last_name, dob, title, pronouns, notes) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [member.first_name, member.last_name, member.dob, member.title, member.pronouns, member.notes, member.id]
    run_sql(sql, values)

#DELETE
def delete(id):
    sql = "DELETE  FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE  FROM members"
    run_sql(sql)


        

