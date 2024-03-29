# Meta: The Full Stack's Final Project

This repository serves as my personal submission for the Final Project in [The Full Stack Course](https://www.coursera.org/learn/the-full-stack?specialization=meta-back-end-developer) offered by Meta through Coursera in the [Back-End Developer Professional Certificate](https://www.coursera.org/professional-certificates/meta-back-end-developer).



![Little Lemon](./littlelemon.png)


## Project Structure

```
thefullstack-final-project-meta
    │
    littlelemon/
    │    ├───littlelemon/
    │    │       ├───asgi.py
    │    │       ├───settings.py
    │    │       ├───urls.py
    │    │       └───wsgi.py
    │    ├───restaurant/
    │    │       ├───migrations/
    |    |       |    └───...
    │    │       ├───static/
    |    |       |    └───...
    │    │       ├───templates/
    |    |       |    └───...
    │    │       ├───admin.py
    │    │       ├───apps.py
    │    │       ├───forms.py
    │    │       ├───models.py
    │    │       ├───tests.py
    │    │       ├───urls.py
    │    │       └───views.py
    │    └───manage.py
    │
    README.md
```





## Getting Started

```bash
$ cd thefullstack-final-project-meta/littlelemon

$ pipenv shell

$ pipenv install

$ python3 manage.py makemigrations 

$ python3 manage.py migrate

$ python3 manage.py runserver
```

Navigate to the **Book page** and **Reservations page** and perform the form actions required to grade the assessment where required. 





## MySQL User Credentials

**User:** `admindjango`

**Password:** `employee@123!`





## `superuser` Credentials

**Username:** `admin`

**Email:** `admin@littlelemon.com`

**Password:** `admin@123!`





## Grading Criteria

1. [x] Is the app added to the installed apps list in the settings file?
2. [x] Is the database configuration updated inside the settings file?
3. [x] Were migrations performed?
4. [x] Are there three fields in the booking form: First name, Reservation date and Reservation slot?
5. [ ] Does a date selector open up when you click on the reservation date field on the booking form?
6. [x] Are all the bookings available as JSON data on the reservations page?
7. [x] Is duplicate booking prohibited on a specific date if the time is already booked?
8. [x] Does changing the date refresh the booking data?
9. [x] Is a duplicate booking on a specific date and time unavailable if the slot is already booked? 
10. [x] Can you display bookings for a specific date using the API?
11. [x] If there is no booking, does a No Booking message show for that date?
12. [x] Was fetch API used to retrieve data from the API?
13. [x] Is the current date automatically selected when you open the booking form?