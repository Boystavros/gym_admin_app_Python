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

