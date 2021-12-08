from db.run_sql import run_sql
from models.instructor import Instructor

#CREATE
def save(instructor):
    sql = "INSERT INTO instructors (name) VALUES (%s) RETURNING *"
    values = [instructor.name]
    result = run_sql(sql, values)[0]
    id = result['id']
    instructor.id = id
    return instructor

#READ
def select_all():
    instructors = []

    sql = "SELECT * FROM instructors"
    results = run_sql(sql)

    for row in results:
        instructor = Instructor(row['name'], row['id'])
        instructors.append(instructor)
    return instructors

def select(id):
    instructor = None
    sql = "SELECT * FROM instructors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        instructor = Instructor(result['name'], result['id'])
    return instructor

#UPDATE
def update(instructor):
    sql = "UPDATE instructors SET (name) = (%s) WHERE id = %s"
    values = [instructor.name, instructor.id]
    run_sql(sql, values)

#DELETE
def delete(id):
    sql = "DELETE  FROM instructors WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE  FROM instructors"
    run_sql(sql)

    


