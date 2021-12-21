class Fit_class:

    def __init__(self, name, category, instructor, date, time, location, capacity, attendees = 0, id = None):
        self.name = name
        self.category = category
        self.instructor = instructor
        self.date = date
        self.time = time
        self.location = location
        self.capacity = capacity
        self.attendees = attendees
        self.id = id