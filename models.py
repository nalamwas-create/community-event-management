from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Member(db.Model):
    __tablename__ = "members"

    member_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))

    registrations = db.relationship(
        "Registration",
        back_populates="member",
        cascade="all, delete-orphan"
    )


class Staff(db.Model):
    __tablename__ = "staff"

    staff_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))

    events = db.relationship(
        "Event",
        back_populates="staff",
        cascade="all, delete-orphan"
    )


class Venue(db.Model):
    __tablename__ = "venues"

    venue_id = db.Column(db.Integer, primary_key=True)
    venue_name = db.Column(db.String(100), nullable=False)
    floor_number = db.Column(db.Integer)
    seating_capacity = db.Column(db.Integer, nullable=False)

    events = db.relationship(
        "Event",
        back_populates="venue",
        cascade="all, delete-orphan"
    )


class Event(db.Model):
    __tablename__ = "events"

    event_id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(150), nullable=False)
    event_date = db.Column(db.Date, nullable=False)

    venue_id = db.Column(
        db.Integer,
        db.ForeignKey("venues.venue_id"),
        nullable=False
    )

    staff_id = db.Column(
        db.Integer,
        db.ForeignKey("staff.staff_id"),
        nullable=False
    )

    venue = db.relationship("Venue", back_populates="events")
    staff = db.relationship("Staff", back_populates="events")

    registrations = db.relationship(
        "Registration",
        back_populates="event",
        cascade="all, delete-orphan"
    )


class Registration(db.Model):
    __tablename__ = "registrations"

    registration_id = db.Column(db.Integer, primary_key=True)

    member_id = db.Column(
        db.Integer,
        db.ForeignKey("members.member_id"),
        nullable=False
    )

    event_id = db.Column(
        db.Integer,
        db.ForeignKey("events.event_id"),
        nullable=False
    )

    registration_date = db.Column(
        db.DateTime,
        server_default=db.func.current_timestamp()
    )

    member = db.relationship("Member", back_populates="registrations")
    event = db.relationship("Event", back_populates="registrations")
