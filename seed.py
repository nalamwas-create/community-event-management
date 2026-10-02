from datetime import date
from app import app
from models import db, Member, Staff, Venue, Event, Registration

with app.app_context():

    # Prevent duplicate seeding
    if Member.query.first():
        print("Database is already seeded.")
    else:
        # Members
        member1 = Member(
            name="John Kamau",
            email="john@example.com",
            phone="0712345678"
        )

        member2 = Member(
            name="Mary Wanjiku",
            email="mary@example.com",
            phone="0723456789"
        )

        member3 = Member(
            name="Peter Otieno",
            email="peter@example.com",
            phone="0734567890"
        )

        # Staff
        staff1 = Staff(
            name="David Mwangi",
            email="david@communityevents.com",
            phone="0745678901"
        )

        staff2 = Staff(
            name="Sarah Njeri",
            email="sarah@communityevents.com",
            phone="0756789012"
        )

        # Venues
        venue1 = Venue(
            venue_name="Community Hall",
            floor_number=1,
            seating_capacity=200
        )

        venue2 = Venue(
            venue_name="Main Conference Room",
            floor_number=2,
            seating_capacity=100
        )

        venue3 = Venue(
            venue_name="Outdoor Event Ground",
            floor_number=0,
            seating_capacity=500
        )

        db.session.add_all([
            member1, member2, member3,
            staff1, staff2,
            venue1, venue2, venue3
        ])

        db.session.commit()

        # Events
        event1 = Event(
            event_name="Community Health Awareness Day",
            event_date=date(2026, 10, 15),
            venue_id=venue1.venue_id,
            staff_id=staff1.staff_id
        )

        event2 = Event(
            event_name="Youth Skills Workshop",
            event_date=date(2026, 11, 5),
            venue_id=venue2.venue_id,
            staff_id=staff2.staff_id
        )

        event3 = Event(
            event_name="Community Sports Day",
            event_date=date(2026, 12, 10),
            venue_id=venue3.venue_id,
            staff_id=staff1.staff_id
        )

        db.session.add_all([event1, event2, event3])
        db.session.commit()

        # Registrations
        registration1 = Registration(
            member_id=member1.member_id,
            event_id=event1.event_id
        )

        registration2 = Registration(
            member_id=member1.member_id,
            event_id=event2.event_id
        )

        registration3 = Registration(
            member_id=member2.member_id,
            event_id=event1.event_id
        )

        registration4 = Registration(
            member_id=member3.member_id,
            event_id=event3.event_id
        )

        db.session.add_all([
            registration1,
            registration2,
            registration3,
            registration4
        ])

        db.session.commit()

        print("Database seeded successfully!")
