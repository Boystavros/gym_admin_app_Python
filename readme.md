<h1>Gym Admin Application</h1>

A full-stack gym membership and class booking admin application built in Python and SQL using Flask, Psycopg2, PostgreSQL and VS Code. 

## The brief

Build a piece of software to help a local gym to manage memberships, and register members for classes.

The application allows users to:

- create/edit/delete members 
- create/edit/delete classes
- book members onto classes 
- display a list of upcoming classes 
- display all members booked onto a particular class
- view class availability (bookings can only be made for classes with available spaces)
- set membership category (off-peak members can only be booked on to classes at off-peak times)

## Click on any of the screenshots below for a video demonstration of the app

[!["Blogogym home page"](static/md_images/homepage.png)](https://youtu.be/Q5v3C94UklA)

[!["Classes page"](static/md_images/classes.png)](https://youtu.be/Q5v3C94UklA)

[!["Members page"](static/md_images/members.png)](https://youtu.be/Q5v3C94UklA)

[!["Bookings page"](static/md_images/bookings.png)](https://youtu.be/Q5v3C94UklA)

## Set up and run application
(Please note, instructions below are for Mac users, different commands may be required by Windows users)

<h3>Software requirements:</h3>
Download the following software in the order shown:

- Git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git 
- Python(version 3 or later): https://www.python.org/downloads/
- Flask: (from anywhere in Terminal) enter ``` pip install -U Flask ```
- Postgres: https://www.postgresql.org/download/
- Psycopg2: (from anywhere in Terminal) enter ``` pip install psycopg2 ```

<h3>Set up:</h3>

- Clone this repository: (navigate to the desired local directory in Terminal) enter ``` git clone https://github.com/Boystavros/solo_project_gym_app.git ```
- Create the database: (from anywhere in Terminal) enter ``` dropdb member_booking_system ```,
  followed by ``` createdb member_booking_system ```
- Add the database tables: (from within this project's directory in Terminal) enter ``` psql -d member_booking_system -f db/member_booking_system.sql ```
- Add seed data (optional): (from within this project's directory in Terminal) enter ``` python3 console.py ```

<h3>Run:</h3>

- Launch Flask: (from within this project's directory in Terminal) enter ``` Flask run ```
- Access homepage: (in browser) enter url ``` localhost:5000/ ```
