<h1>Gym Admin Application</h1>

A full-stack gym membership and class booking application built in Python and SQL using Flask, Psycopg2, PostgreSQL and VS Code. 

<h3>The brief:</h3>

Build a piece of software to help a local gym to manage memberships, and register members for classes.

The application allows users to:

- create/edit/delete members 
- create/edit/delete classes
- book members onto classes 
- display a list of upcoming classes 
- display all members booked onto a particular class

<!-- <h3> Application demonstration:</h3> -->



<h2>Set up and run application </h2>
(Please note, instructions below are for Mac users, different commands may be required by Windows users)

<h3>Software requirements:</h3>
Download the following software in the order shown:

- Git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git 
- Python(version 3 or later): https://www.python.org/downloads/
- Flask: (from anywhere in Terminal) enter ``` pip install -U Flask ```
- Postgres: https://www.postgresql.org/download/
- Psycopg2: (from anywhere in Terminal) enter ``` pip install psycopg2 ```

<h3>Set up:</h3>

- Clone this repository: (navigate to the desired local directory in Terminal) enter ``` git clone XXXXXX ```
- Create the database: (from anywhere in Terminal) enter ``` dropdb member_booking_system ```,
  followed by ``` createdb member_booking_system ```
- Add the database tables: (from within this project's directory in Terminal) enter ``` psql -d member_booking_system -f db/member_booking_system.sql ```
- Add seed data (optional): (from within this project's directory in Terminal) enter ``` python3 console.py ```

<h3>Run:</h3>

- Launch Flask: (from within this project's directory in Terminal) enter ``` Flask run ```
- Access homepage: (in browser) enter url ``` localhost:5000/ ```
