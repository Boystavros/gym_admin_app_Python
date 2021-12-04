import pdb
from controllers.member_controller import update
from models.booking import Booking
from models.member import Member
from models.fit_class import Fit_class

import repositories.member_repository as member_repository
import repositories.fit_class_repository as fit_class_repository
import repositories.booking_repository as booking_repository

booking_repository.delete_all()

#Test save functions
member1 = Member("White", "Goodman", "1975-01-01", "Mr", "he/him", "Loves milk") #date must be in yyyy-mm-dd format
member_repository.save(member1)

member2 = Member("Jones", "Me'Shell", "1979-02-20", "Mr", "he/him") #date must be in yyyy-mm-dd format
member_repository.save(member2)

fit_class1 = Fit_class("Dodgeball", "Sport", "Cotton McKnight", "2021-12-07", "12:00", "Dodgeball pitch")
fit_class_repository.save(fit_class1)

fit_class2 = Fit_class("Wrench Yoga", "Wellness", "Patches O'Hoolihan", "2021-12-05", "11:00", "Gym hall")
fit_class_repository.save(fit_class2)

booking1 = Booking(member1, fit_class1, "19:05_03/12/2021", "Peter")
booking_repository.save(booking1)

booking2 = Booking(member2, fit_class2, "21:30_04/12/2021", "Justin")
booking_repository.save(booking2)

#Test select functions
# print(member_repository.select(1).__dict__)
# print(fit_class_repository.select(1))
# print(booking_repository.select_all())
# print(booking_repository.select(1))

#test update functions
# updatedMem1 = Member("Whyte", "Goodman", "01/01/1975", "Mr", "he/him", "Loves milk", 1)
# member_repository.update(updatedMem1)

# updatedBooking = Booking(member1, fit_class1, "20:05_03/12/2021", "Peter", 1)
# booking_repository.update(updatedBooking)

#test delete
# booking_repository.delete(1)