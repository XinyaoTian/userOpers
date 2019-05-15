from app import app


# get user by user id
@app.route('/users/uid/<int:uid>', methods=['GET'])
def get_user_by_uid(uid):
    pass


# get user by username
@app.route('/users/username/<string:username>', methods=['GET'])
def get_user_by_username(username):
    pass


# get user by phone_number
@app.route('/users/username/<string:phone_number>', methods=['GET'])
def get_user_by_phone_number(phone_number):
    pass


# get all users
@app.route('/users', methods=['GET'])
def get_all_users():
    pass


# create new user
@app.route('/users', methods=['POST'])
def create_new_user():
    pass


# update user info
@app.route('/users', methods=['PUT'])
def update_user():
    pass


# bad requests holder
def bad_request():
    pass
