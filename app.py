import os
from flask import Flask, request
from datetime import datetime
from flask_migrate import Migrate
from models import db, Member, Staff, Venue, Event, Registration

app = Flask(__name__)

database_path = os.path.join(app.root_path, "community_event.db")

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{database_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def home():
    return {"message": "Community Event Management System API"}


@app.route("/members", methods=["GET"])
def get_members():
    members = Member.query.all()
    return [
        {
            "member_id": member.member_id,
            "name": member.name,
            "email": member.email,
            "phone": member.phone
        }
        for member in members
    ]


@app.route("/members/<int:member_id>", methods=["GET"])
def get_member(member_id):
    member = db.session.get(Member, member_id)

    if not member:
        return {"error": "Member not found"}, 404

    return {
        "member_id": member.member_id,
        "name": member.name,
        "email": member.email,
        "phone": member.phone
    }


@app.route("/members", methods=["POST"])
def create_member():
    data = request.get_json()

    member = Member(
        name=data["name"],
        email=data["email"],
        phone=data.get("phone")
    )

    db.session.add(member)
    db.session.commit()

    return {
        "message": "Member created successfully",
        "member_id": member.member_id
    }, 201


@app.route("/staff", methods=["GET"])
def get_staff():
    staff_members = Staff.query.all()

    return [
        {
            "staff_id": staff.staff_id,
            "name": staff.name,
            "email": staff.email,
            "phone": staff.phone
        }
        for staff in staff_members
    ]


@app.route("/staff/<int:staff_id>", methods=["GET"])
def get_one_staff(staff_id):
    staff = db.session.get(Staff, staff_id)

    if not staff:
        return {"error": "Staff member not found"}, 404

    return {
        "staff_id": staff.staff_id,
        "name": staff.name,
        "email": staff.email,
        "phone": staff.phone
    }


@app.route("/staff", methods=["POST"])
def create_staff():
    data = request.get_json()

    staff = Staff(
        name=data["name"],
        email=data["email"],
        phone=data.get("phone")
    )

    db.session.add(staff)
    db.session.commit()

    return {
        "message": "Staff member created successfully",
        "staff_id": staff.staff_id
    }, 201


@app.route("/venues", methods=["GET"])
def get_venues():
    venues = Venue.query.all()

    return [
        {
            "venue_id": venue.venue_id,
            "venue_name": venue.venue_name,
            "floor_number": venue.floor_number,
            "seating_capacity": venue.seating_capacity
        }
        for venue in venues
    ]


@app.route("/venues/<int:venue_id>", methods=["GET"])
def get_venue(venue_id):
    venue = db.session.get(Venue, venue_id)

    if not venue:
        return {"error": "Venue not found"}, 404

    return {
        "venue_id": venue.venue_id,
        "venue_name": venue.venue_name,
        "floor_number": venue.floor_number,
        "seating_capacity": venue.seating_capacity
    }


@app.route("/venues", methods=["POST"])
def create_venue():
    data = request.get_json()

    venue = Venue(
        venue_name=data["venue_name"],
        floor_number=data.get("floor_number"),
        seating_capacity=data["seating_capacity"]
    )

    db.session.add(venue)
    db.session.commit()

    return {
        "message": "Venue created successfully",
        "venue_id": venue.venue_id
    }, 201


@app.route("/events", methods=["GET"])
def get_events():
    events = Event.query.all()

    return [
        {
            "event_id": event.event_id,
            "event_name": event.event_name,
            "event_date": event.event_date.isoformat(),
            "venue_id": event.venue_id,
            "staff_id": event.staff_id
        }
        for event in events
    ]


@app.route("/events/<int:event_id>", methods=["GET"])
def get_event(event_id):
    event = db.session.get(Event, event_id)

    if not event:
        return {"error": "Event not found"}, 404

    return {
        "event_id": event.event_id,
        "event_name": event.event_name,
        "event_date": event.event_date.isoformat(),
        "venue_id": event.venue_id,
        "staff_id": event.staff_id
    }


@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()

    event = Event(
        event_name=data["event_name"],
        event_date=datetime.strptime(data["event_date"], "%Y-%m-%d").date(),
        venue_id=data["venue_id"],
        staff_id=data["staff_id"]
    )

    db.session.add(event)
    db.session.commit()

    return {
        "message": "Event created successfully",
        "event_id": event.event_id
    }, 201


@app.route("/registrations", methods=["GET"])
def get_registrations():
    registrations = Registration.query.all()

    return [
        {
            "registration_id": registration.registration_id,
            "member_id": registration.member_id,
            "event_id": registration.event_id,
            "registration_date": registration.registration_date.isoformat()
            if registration.registration_date else None
        }
        for registration in registrations
    ]


@app.route("/registrations/<int:registration_id>", methods=["GET"])
def get_registration(registration_id):
    registration = db.session.get(Registration, registration_id)

    if not registration:
        return {"error": "Registration not found"}, 404

    return {
        "registration_id": registration.registration_id,
        "member_id": registration.member_id,
        "event_id": registration.event_id,
        "registration_date": registration.registration_date.isoformat()
        if registration.registration_date else None
    }


@app.route("/registrations", methods=["POST"])
def create_registration():
    data = request.get_json()

    registration = Registration(
        member_id=data["member_id"],
        event_id=data["event_id"]
    )

    db.session.add(registration)
    db.session.commit()

    return {
        "message": "Registration created successfully",
        "registration_id": registration.registration_id
    }, 201


if __name__ == "__main__":
    app.run(debug=True)
