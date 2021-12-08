from db.run_sql import run_sql
from models.member import Member
from models.fit_class import Fit_class
from models.booking import Booking
import repositories.fit_class_repository as fit_class_repository
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository

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

    sql = "SELECT * FROM members ORDER BY last_name ASC, first_name ASC"
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

def select_for_edit(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        display_dob = result['dob']
        day = display_dob[0:2]
        month = display_dob[3:5]
        year = display_dob[6:10]
        picker_dob = f"{year}-{month}-{day}"
        member = Member(result['first_name'], result['last_name'], picker_dob, result['title'], result['pronouns'], result['notes'], result['id'])
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


# #MEMBERS BOOKED ON CLASS
# def attendees(fit_class):
#     attendees = []
    
#     sql = "SELECT * FROM bookings WHERE fit_class_id = %s"
#     values = [fit_class.id]
#     results = run_sql(sql, values)

#     for row in results:
#         member = member_repository.select(row['member_id'])
#         attendees.append(member)
#     return attendees

