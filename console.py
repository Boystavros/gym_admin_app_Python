import pdb
from models.booking import Booking
from models.member import Member
from models.fit_class import Fit_class

import repositories.member_repository as member_repository
import repositories.fit_class_repository as fit_class_repository
import repositories.booking_repository as booking_repository

#Test save functions
member1 = Member("White", "Goodman", "01/01/1975", "Mr", "he/him", "Loves milk")
member_repository.save(member1)

fit_class1 = Fit_class("Dodgeball", "Sport", "Patches", "03/12/2021", "12:00", "Gym hall")
fit_class_repository.save(fit_class1)

booking1 = Booking(member1, fit_class1, "19:05_03/12/2021", "Peter")
booking_repository.save(booking1)