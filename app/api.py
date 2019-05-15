from app import app, db
from app.models import User
from flask import jsonify
from flask import request, url_for
from werkzeug.http import HTTP_STATUS_CODES


# get user by user id
@app.route('/users/uid/<int:uid>', methods=['GET'])
def get_user_by_uid(uid):
    data = list()
    data.append(User.query.get_or_404(uid).to_dict())
    return jsonify(data)


# get user by username
@app.route('/users/username/<string:username>', methods=['GET'])
def get_user_by_username(username):
    data = list()
    data.append(User.query.filter(User.username == username).first_or_404().to_dict())
    return jsonify(data)


# get user by phone_number
@app.route('/users/phone_number/<phone_number>', methods=['GET'])
def get_user_by_phone_number(phone_number):
    data = list()
    data.append(User.query.filter(User.phone_number == phone_number).first_or_404().to_dict())
    return jsonify(data)


# get all users
@app.route('/users', methods=['GET'])
def get_all_users():
    data = list()
    for user in User.query.all():
        data.append(user.to_dict())
    return jsonify(data)


# create new user
@app.route('/users', methods=['POST'])
def create_new_user():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    phone_number = request.form.get('phone_number')

    # check faults
    if password is None or username is None:
        return bad_request('This post must include both username and password fields.')
    if email is None or phone_number is None:
        return bad_request('This post must include both email and phone_number fields.')
    if User.query.filter_by(username=username).first():
        return bad_request('please use a different username.')
    if User.query.filter_by(email=email).first():
        return bad_request('please use a different email address.')
    if User.query.filter_by(phone_number=phone_number).first():
        return bad_request('please use a different phone number.')

    # db operations
    new_user = User(username=username, email=email, phone_number=phone_number)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    # response
    response = jsonify(new_user.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('get_user_by_uid', uid=new_user.id)

    return response


# update user info
@app.route('/users', methods=['PUT'])
def update_user():
    username = request.form.get('username')
    if username is None:
        return bad_request('This post must include username field.')

    # get PUT data
    password = request.form.get('password') or None
    email = request.form.get('email') or None
    phone_number = request.form.get('phone_number') or None

    # take out data form db
    user = User.query.filter_by(username=username).first()

    # update procedure
    if password is not None:
        user.set_password(password)
    if email is not None:
        user.email = email
    if phone_number is not None:
        user.phone_number = phone_number

    # update db
    db.session.add(user)
    db.session.commit()

    # response
    response = jsonify(user.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('get_user_by_uid', uid=user.id)

    return response


# verify username and password
@app.route('/users/validation/', methods=['POST'])
def validate_password():
    username = request.form.get('username')
    password = request.form.get('password')

    # if there is no password field in post
    if password is None or username is None:
        return bad_request('This post must include both username and password fields.')
    user = User.query.filter(User.username == username).first()
    if user is None:
        return jsonify({'username': username, 'validation': 'False'})
    validate = user.check_password(password)

    # authentication verify success.
    if validate is True:
        return jsonify({'username': username, 'validation': 'True'})
    # authentication verify failed.
    return jsonify({'username': username, 'validation': 'False'})


# bad requests holder
def bad_request(message):
    return error_response(400, message)


# error response
def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response
