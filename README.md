# Bincomx

Status Badge: [![Deploy to Firebase Hosting on merge](https://github.com/jamesconfy/bincomx/actions/workflows/firebase-hosting-merge.yml/badge.svg)](https://github.com/jamesconfy/bincomx/actions/workflows/firebase-hosting-merge.yml)

## Setting Up

To run this locally on your system, clone the repo to your local machine and start by doing a `python -m venv venv`. Note: You need to have python installed on your system already. After it has finishing creating your virtual environment, you activate it by doing a `. venv/bin/activate` and you use pip to install the packages `pip install --upgrade pip && pip install -r requirements.txt`.

After that has done processing, you create a .env file and copy the values from the [dummy.env](dummy.env) file and paste it into the .env file

## Run App

After doing that you can run the app by typing `python run.py`, it will show something like this:

```terminal
* Serving Flask app 'bincom'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://localhost:80
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 132-891-021
```

After that, you can activate the app on [localhost](http://localhost:80)

## Routes

You have 4 routes, which include:

- [Home](http://localhost:80): Every web server needs a home page, this is just formality, and it returns `Hello`.
- [polling_unit_result](http://localhost:80/polling_unit_result): This returns the result of all the polling units.
- [polling_unit_result/{id}](http://localhost:80/polling_unit_result/8): This returns the result for a specific polling unit.
- [polling_unit](http://localhost:80/polling_unit): This accepts both a GET and POST methods, if it is a GET method a form is return where you are meant to input the details of the result you are meant to add. While if it is a POST method, it returns `Result added successfully`.
