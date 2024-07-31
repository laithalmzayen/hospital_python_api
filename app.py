from flask import Flask, request, jsonify
from pydantic import ValidationError
from functools import wraps
from app.database import db
from app.schemas import StaffModel
from app.crud import create_staff, get_staff_by_id, update_staff

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    'postgresql://postgres:000@localhost:5432/hospital_db'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.headers.get('X-Staff-Name') != 'admin':
            return jsonify({'message': 'Forbidden'}), 403
        return f(*args, **kwargs)
    return decorated_function


@app.route('/staff', methods=['POST'])
@admin_required
def add_staff():
    try:
        data = request.get_json()
        staff_data = StaffModel(**data)
        new_staff = create_staff(staff_data)
        if new_staff:
            return jsonify({'message': 'Staff added successfully'}), 201
        else:
            return jsonify({'message': 'Staff member already exists'}), 409
    except ValidationError as e:
        return jsonify(e.errors()), 400


@app.route('/staff/<int:id>', methods=['GET'])
def get_staff(id):
    staff = get_staff_by_id(id)
    if staff:
        return jsonify({'id': staff.id, 'name': staff.name, 'role': staff.role})
    else:
        return jsonify({'message': 'Staff member not found'}), 404


@app.route('/staff/<int:id>', methods=['PUT'])
@admin_required
def modify_staff(id):
    try:
        data = request.get_json()
        staff_data = StaffModel(**data)
        updated_staff = update_staff(id, staff_data)
        if updated_staff:
            return jsonify({'message': 'Staff updated successfully'})
        else:
            return jsonify({'message': 'Staff member not found'}), 404
    except ValidationError as e:
        return jsonify(e.errors()), 400


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
