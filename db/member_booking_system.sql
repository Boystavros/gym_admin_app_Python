DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS fit_classes;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS instructors;


CREATE TABLE instructors(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE members(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    dob VARCHAR(255),
    title VARCHAR(255),
    pronouns VARCHAR(255),
    notes TEXT    
);

CREATE TABLE fit_classes(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    category VARCHAR(255),
    instructor_id INT REFERENCES instructors(id) ON DELETE CASCADE,
    date VARCHAR(255),
    time VARCHAR(255),
    location VARCHAR(255),
    capacity INT,
    attendees INT
);

CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    fit_class_id INT REFERENCES fit_classes(id) ON DELETE CASCADE,
    timestamp VARCHAR(255),
    staff_member VARCHAR(255)
);