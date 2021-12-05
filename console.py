import pdb
import time
from datetime import datetime
from controllers.member_controller import update
from models.booking import Booking
from models.member import Member
from models.fit_class import Fit_class

import repositories.member_repository as member_repository
import repositories.fit_class_repository as fit_class_repository
import repositories.booking_repository as booking_repository

booking_repository.delete_all()

#Seed member data
member1 = Member("Justin", "Long", "1982-01-01", "Mr", "he/him", "Allergies") #date must be in yyyy-mm-dd format
member_repository.save(member1)

member2 = Member("Gordon", "Nohope", "1968-02-20", "Mr", "he/him", "Back injury") #date must be in yyyy-mm-dd format
member_repository.save(member2)

member3 = Member("Pirate", "Steve", "1657-04-25", "Captain", "he/him") #date must be in yyyy-mm-dd format
member_repository.save(member3)

member4 = Member("Kate", "Veatch", "1980-07-15", "Miss", "she/her") #date must be in yyyy-mm-dd format
member_repository.save(member4)

#Seed class data
fit_class1 = Fit_class("Dodgeball", "Sport", "Cotton McKnight", "2021-12-07", "12:00", "Dodgeball pitch")
fit_class_repository.save(fit_class1)

fit_class2 = Fit_class("Wrench Yoga", "Wellness", "Patches O'Hoolihan", "2021-12-05", "11:00", "Gym hall")
fit_class_repository.save(fit_class2)

fit_class3 = Fit_class("Balls, balls, balls", "Cardio", "Peter La Fleur", "2021-12-07", "11:00", "Gym hall")
fit_class_repository.save(fit_class3)

fit_class4 = Fit_class("Team dance", "Dance", "White Goodman", "2021-12-07", "18:00", "Dance studio")
fit_class_repository.save(fit_class4)

#Seed booking data
booking1 = Booking(member1, fit_class1, "Me'Shell")
booking_repository.save(booking1)

booking2 = Booking(member2, fit_class2, "White")
booking_repository.save(booking2)

booking3 = Booking(member3, fit_class3, "Dwight")
booking_repository.save(booking3)

booking4 = Booking(member4, fit_class4, "Patches")
booking_repository.save(booking4)


#Test select functions
# print(member_repository.select(1).__dict__)
# print(fit_class_repository.select(1))
# print(booking_repository.select_all())
# print(booking_repository.select(1))

#test update functions
# updatedMem1 = Member("Whyte", "Goodman", "01/01/1975", "Mr", "he/him", "Loves milk", 1)
# member_repository.update(updatedMem1)

# timestamp = datetime.now()
# updatedBooking = Booking(member1, fit_class1, "Sacha", timestamp, 1)
# booking_repository.update(updatedBooking)

#test delete
# booking_repository.delete(1)

#creating 'timestamp' object for bookings
# ct = datetime.now()
# print("current time = ", ct)
# print(type(ct))

#TEST booking by... functions
print(booking_repository.bookings_by_member(member1)[0].__dict__)
