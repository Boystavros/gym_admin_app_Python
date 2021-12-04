from db.run_sql import run_sql
# from models.booking import Booking

def save(booking):
    sql = "INSERT INTO bookings (member_id, fit_class_id, timestamp, staff_member) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [booking.member.id, booking.fit_class.id, booking.timestamp, booking.staff_member]
    result = run_sql(sql, values)
    id = result[0]['id']
    booking.id = id
    return booking