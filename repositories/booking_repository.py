from db.run_sql import run_sql
from models.booking import Booking

def save(booking):
    sql = "SELECT "