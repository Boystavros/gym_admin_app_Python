import pdb
import time
from datetime import datetime
from controllers.member_controller import update
from models.booking import Booking
from models.instructor import Instructor
from models.member import Member
from models.fit_class import Fit_class

import repositories.member_repository as member_repository
import repositories.fit_class_repository as fit_class_repository
import repositories.booking_repository as booking_repository
import repositories.instructor_repository as instructor_repository

booking_repository.delete_all()
member_repository.delete_all()
fit_class_repository.delete_all()
instructor_repository.delete_all()

#Seed member data
member1 = Member("Justin", "Long", "01-01-1982", "Mr", "he/him", "standard", "Allergies")
member_repository.save(member1)

member2 = Member("Gordon", "Nohope", "20-02-1968", "Mr", "he/him", "standard", "Back injury")
member_repository.save(member2)

member3 = Member("Pirate", "Steve", "25-04-1695", "Captain", "he/him", "standard")
member_repository.save(member3)

member4 = Member("Cotton", "McKnight", "15-07-1964", "Mr", "he/him", "standard")
member_repository.save(member4)

member5 = Member("Suzy", "Nakamura", "15-07-1979", "Mrs", "she/her", "standard")
member_repository.save(member5)

member6 = Member("Pepper", "Brooks", "15-07-1972", "Mr", "he/him", "standard")
member_repository.save(member6)

member7 = Member("Peter", "La Fleur", "15-07-1974", "Mr", "he/him", "standard")
member_repository.save(member7)


#Seed instructor data
instructor1 = Instructor("White Goodman")
instructor_repository.save(instructor1)

instructor2 = Instructor("Fran Stalinovskovichdavidovitchsky")
instructor_repository.save(instructor2)

instructor3 = Instructor("Me'Shell Jones")
instructor_repository.save(instructor3)

instructor4 = Instructor("Patches O'Hoolihan")
instructor_repository.save(instructor4)

instructor5 = Instructor("Bla Zer")
instructor_repository.save(instructor5)

instructor6 = Instructor("La Zer")
instructor_repository.save(instructor6)

#Seed class data
fit_class1 = Fit_class("Dodgeball", "Sport", instructor1, "07-12-2021", "12:00", "Dodgeball pitch", 10)
fit_class_repository.save(fit_class1)

fit_class2 = Fit_class("Wrench Yoga", "Wellness", instructor2, "05-12-2021", "11:00", "Gym hall", 2)
fit_class_repository.save(fit_class2)

fit_class3 = Fit_class("Balls, balls, balls", "Cardio", instructor3, "07-12-2021", "11:00", "Gym hall", 8)
fit_class_repository.save(fit_class3)

fit_class4 = Fit_class("Team dance", "Dance", instructor4, "07-12-2021", "18:00", "Dance studio", 6)
fit_class_repository.save(fit_class4)

#Seed booking data
booking1 = Booking(member1, fit_class1, "staff1")
booking_repository.save(booking1)

booking2 = Booking(member2, fit_class2, "staff2")
booking_repository.save(booking2)

booking3 = Booking(member3, fit_class3, "staff3")
booking_repository.save(booking3)

booking4 = Booking(member4, fit_class3, "staff4")
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

#format date input

# date = "2021-12-02"
# print(date)
# year = date[0:4]
# month = date[5:7]
# day = date[8:10]
# formatted_date = f"{day}-{month}-{year}"
# print(formatted_date)
# print(f"{day}-{month}-{year}")



#TEST booking by... functions
# print(booking_repository.bookings_by_member(member1)[0].__dict__)
# print(booking_repository.bookings_by_class(fit_class3))