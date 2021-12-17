<h1>Gym Admin Application</h1>

(Please note, instructions below are for Mac users, different commands may be required by Windows users)

<h3>Software requirements:</h3>
Donwload the following software in the order shown:

- Git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git 
- Python(version 3 or later): https://www.python.org/downloads/
- Flask: (enter the following from anywhere in Terminal) **'pip install -U Flask'**
- Postgres: https://www.postgresql.org/download/
- Psycopg2: (enter the following from anywhere in Terminal) **'pip install psycopg2'**



To contain:
- running instructions for your applications (so other people can clone it and run it)
- your brief
- the technologies you used
- it can also contain screenshots!

The brief:
- A local gym has asked you to build a piece of software to help them to manage memberships, and register members for classes.

- MVP
The app should allow the gym to create and edit Members
The app should allow the gym to create and edit Classes
The app should allow the gym to book members on specific classes
The app should show a list of all upcoming classes
The app should show all members that are booked in for a particular class

- Possible Extensions
Classes could have a maximum capacity, and users can only be added while there is space remaining.
The gym could be able to give its members Premium or Standard membership. Standard members can only be signed up for classes during off-peak hours.
The Gym could mark members and classes as active/deactivated. Deactivated members/classes will not appear when creating bookings.

Running instructions:
- Clone this repo using git
- To run: Set up DB - enter 'dropdb member_booking_system' , 'createdb member_booking_system'
- To populate DB tables - enter 'psql -d member_booking_system -f db/member_booking_system.sql' from within the member_booking_system folder from this repo.
- Run console.py to add seed data
- Enter 'Flask run' to launch Flask server
- Navigate to 'localhost5000/' to access the home page
