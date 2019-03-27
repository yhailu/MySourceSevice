from flask import Flask, jsonify
from db_operations import db_operations

app = Flask(__name__)


@app.route('/get_all_users')
def get_all_users():
    """get_all_users: will return all users in the db"""
    return "get_all_users"


@app.route('/update_user')
def update_user():
    return 'update_user()'

@app.route('/get_user/<userid>')
def get_user(userid):
    """get_user: gets a user from service using an user_id"""
    db = db_operations()
    result = db.get_student(1)
    t = ' '

    for row in result:
        print(row)

@app.route('/add_user')
def test():
    """add_user: will add a user to app"""
    return "add_user"

@app.route('/')
def welcome():
    return "Welcome to mySource api v1.0"
if __name__ == '__main__':
    app.run()
