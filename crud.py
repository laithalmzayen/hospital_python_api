from sqlalchemy.exc import IntegrityError
from .models import Staff
from .database import db


def create_staff(staff_data):
    new_staff = Staff(name=staff_data.name, role=staff_data.role)
    db.session.add(new_staff)
    try:
        db.session.commit()
        return new_staff
    except IntegrityError:
        db.session.rollback()
        return None


def get_staff_by_id(staff_id):
    return Staff.query.get(staff_id)


def update_staff(staff_id, staff_data):
    staff = get_staff_by_id(staff_id)
    if staff:
        staff.name = staff_data.name
        staff.role = staff_data.role
        db.session.commit()
        return staff
    return None
