from db.run_sql import run_sql
from models.fit_class import Fit_class
from models.instructor import Instructor
import repositories.instructor_repository as instructor_repository


#CREATE
def save(fit_class):
    sql = "INSERT INTO fit_classes (name, category, instructor_id, date, time, location, capacity, attendees) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [fit_class.name, fit_class.category, fit_class.instructor.id, fit_class.date, fit_class.time, fit_class.location, fit_class.capacity, fit_class.attendees]
    results = run_sql(sql, values)
    id =  results[0]['id']
    fit_class.id = id
    return fit_class

#READ
def select_all():
    fit_classes = []

    sql = "SELECT * FROM fit_classes ORDER BY date ASC, time ASC"
    results = run_sql(sql)

    for row in results:
        name = row['name']
        category = row['category']
        instructor = instructor_repository.select(row['instructor_id'])
        date = row['date']
        time = row['time']
        location = row['location']
        capacity = row['capacity']
        attendees = row['attendees']
        id = row['id']
        fit_class = Fit_class(name, category, instructor, date, time, location, capacity, attendees, id)
        fit_classes.append(fit_class)
    return fit_classes

def select(id):
    fit_class = None

    sql = "SELECT * FROM fit_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        instructor = instructor_repository.select(result['instructor_id'])
        fit_class = Fit_class(result['name'], result['category'], instructor, result['date'], result['time'], result['location'], result['capacity'], result['attendees'], id)
    return fit_class

def select_for_edit(id):
    fit_class = None

    sql = "SELECT * FROM fit_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        display_date = result['date']
        day = display_date[0:2]
        month = display_date[3:5]
        year = display_date[6:10]
        picker_date = f"{year}-{month}-{day}"
        
        instructor = instructor_repository.select(result['instructor_id'])
        
        fit_class = Fit_class(result['name'], result['category'], instructor, picker_date, result['time'], result['location'], result['capacity'], result['attendees'], id)
    return fit_class

#UPDATE
def update(fit_class):
    sql = "UPDATE fit_classes SET (name, category, instructor_id, date, time, location, capacity, attendees) = (%s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [fit_class.name, fit_class.category, fit_class.instructor.id, fit_class.date, fit_class.time, fit_class.location, fit_class.capacity, fit_class.attendees, fit_class.id]
    run_sql(sql, values)

#DELETE
def delete(id):
    sql = "DELETE  FROM fit_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
def delete_all():
    sql = "DELETE  FROM fit_classes"
    run_sql(sql)
