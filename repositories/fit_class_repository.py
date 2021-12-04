from db.run_sql import run_sql
from models.fit_class import Fit_class


#CREATE
def save(fit_class):
    sql = "INSERT INTO fit_classes (name, category, instructor, date, time, location) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [fit_class.name, fit_class.category, fit_class.instructor, fit_class.date, fit_class.time, fit_class.location]
    results = run_sql(sql, values)
    id =  results[0]['id']
    fit_class.id = id
    return fit_class

#READ
def select_all():
    fit_classes = []

    sql = "SELECT * FROM fit_classes"
    results = run_sql(sql)

    for row in results:
        name = row['name']
        category = row['category']
        instructor = row['instructor']
        date = row['date']
        time = row['time']
        location = row['location']
        id = row['id']
        fit_class = Fit_class(name, category, instructor, date, time, location, id)
        fit_classes.append(fit_class)
    return fit_classes
