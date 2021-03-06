import pdb
from db.run_sql import run_sql
from models.booking import Booking
import repositories.member_repository as member_repository
import repositories.fit_class_repository as fit_class_repository

#CREATE
def save(booking):
    sql = "INSERT INTO bookings (member_id, fit_class_id, timestamp, staff_member) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [booking.member.id, booking.fit_class.id, booking.timestamp, booking.staff_member]
    result = run_sql(sql, values)
    id = result[0]['id']
    booking.id = id
    fit_class = fit_class_repository.select(booking.fit_class.id)
    fit_class.increase_attendees()
    fit_class_repository.update(fit_class)
    return booking

#READ
def select_all():
    bookings = []

    sql = "SELECT bookings.id, bookings.member_id, bookings.fit_class_id, bookings.staff_member, bookings.timestamp FROM bookings INNER JOIN members ON bookings.member_id = members.id INNER JOIN fit_classes ON bookings.fit_class_id = fit_classes.id ORDER BY bookings.timestamp DESC"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        fit_class = fit_class_repository.select(row['fit_class_id'])
        booking = Booking(member, fit_class, row['staff_member'], row['timestamp'], row['id'])
        bookings.append(booking)
    return bookings

def select(id):
    booking = None

    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = member_repository.select(result['member_id'])
        fit_class = fit_class_repository.select(result['fit_class_id'])
        booking = Booking(member, fit_class, result['staff_member'], result['timestamp'], result['id'])
    return booking

#UPDATE
def update(booking):
    sql = "UPDATE bookings SET (member_id, fit_class_id, staff_member, timestamp) = (%s, %s, %s, %s) WHERE id = %s RETURNING *"
    values = [booking.member.id, booking.fit_class.id, booking.staff_member, booking.timestamp, booking.id]
    run_sql(sql, values)
    
#DELETE
def delete_all():
    sql = "DELETE  FROM bookings"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM bookings WHERE id = %s"
    values = [id]
    booking = select(id)
    fit_class = fit_class_repository.select(booking.fit_class.id)
    fit_class.decrease_attendees()
    fit_class_repository.update(fit_class)
    run_sql(sql, values)

#BOOKINGS BY MEMBER OR CLASS
def bookings_by_member(member):
    bookings = []
    
    sql = "SELECT bookings.id, fit_classes.date, fit_classes.time, fit_classes.name FROM bookings INNER JOIN fit_classes ON bookings.fit_class_id = fit_classes.id WHERE bookings.member_id = %s ORDER BY fit_classes.date ASC, fit_classes.time ASC, fit_classes.name ASC;"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        booking = select(row['id'])
        bookings.append(booking)
    return bookings

def bookings_by_class(fit_class):
    bookings = []
    
    sql = "SELECT bookings.id, members.last_name, members.first_name FROM bookings INNER JOIN members ON bookings.member_id = members.id WHERE fit_class_id = %s ORDER BY members.first_name ASC, members.last_name ASC"
    values = [fit_class.id]
    results = run_sql(sql, values)

    for row in results:
        booking = select(row['id'])
        bookings.append(booking)
    return bookings