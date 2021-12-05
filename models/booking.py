from datetime import datetime

class Booking:

    def __init__(self, member, fit_class, staff_member, timestamp = datetime.now(), id = None):
        self.member = member
        self.fit_class = fit_class
        self.staff_member = staff_member
        self.timestamp = timestamp
        self.id = id
